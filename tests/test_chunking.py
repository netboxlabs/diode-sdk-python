#!/usr/bin/env python
# Copyright 2026 NetBox Labs Inc
"""Tests for message chunking utilities."""

from unittest.mock import patch

from netboxlabs.diode.sdk.chunking import create_message_chunks, estimate_message_size
from netboxlabs.diode.sdk.diode.v1 import ingester_pb2


def test_create_message_chunks_empty_list():
    """Test create_message_chunks with an empty entity list."""
    entities = []
    chunks = create_message_chunks(entities)

    assert len(chunks) == 1
    assert chunks[0] == []


def test_create_message_chunks_single_chunk():
    """Test create_message_chunks when entities fit in a single chunk."""
    # Create small mock entities that will fit in one chunk
    entities = []
    for i in range(5):
        entity = ingester_pb2.Entity()
        entity.device.name = f"test_device_{i}"
        entities.append(entity)

    # Mock size to be small (under 3 MB default)
    with patch("netboxlabs.diode.sdk.chunking.estimate_message_size", return_value=1024):
        chunks = create_message_chunks(entities)

    assert len(chunks) == 1
    assert len(chunks[0]) == 5
    assert chunks[0] == entities


def test_create_message_chunks_multiple_chunks():
    """Test create_message_chunks when entities need to be split into multiple chunks."""
    # Create entities that will exceed the target size
    entities = []
    for i in range(10):
        entity = ingester_pb2.Entity()
        entity.device.name = f"test_device_{i}"
        entities.append(entity)

    # Mock size to be larger than target (3MB default)
    with patch("netboxlabs.diode.sdk.chunking.estimate_message_size", return_value=5 * 1024 * 1024):
        # Also need to mock ByteSize for individual entities and base overhead
        with patch.object(ingester_pb2.Entity, "ByteSize", return_value=600000):  # ~600KB each
            with patch.object(ingester_pb2.IngestRequest, "ByteSize", return_value=100):
                chunks = create_message_chunks(entities)

    # Should have multiple chunks
    assert len(chunks) > 1

    # All entities should be present across chunks
    total_entities = sum(len(chunk) for chunk in chunks)
    assert total_entities == 10

    # Each chunk should have at least 1 entity
    for chunk in chunks:
        assert len(chunk) >= 1


def test_create_message_chunks_one_entity_per_chunk():
    """Test create_message_chunks when each entity needs its own chunk."""
    entities = []
    for i in range(3):
        entity = ingester_pb2.Entity()
        entity.device.name = f"large_device_{i}"
        entities.append(entity)

    # Mock very large size to force one entity per chunk
    # Each entity is 3.5 MB, forcing one per chunk with 3 MB limit
    with patch("netboxlabs.diode.sdk.chunking.estimate_message_size", return_value=20 * 1024 * 1024):
        with patch.object(ingester_pb2.Entity, "ByteSize", return_value=3 * 1024 * 1024 + 500000):
            with patch.object(ingester_pb2.IngestRequest, "ByteSize", return_value=100):
                chunks = create_message_chunks(entities)

    # Should have 3 chunks with 1 entity each
    assert len(chunks) == 3
    for chunk in chunks:
        assert len(chunk) == 1


def test_estimate_message_size():
    """Test estimate_message_size method."""
    # Create mock entities
    entities = []
    for i in range(3):
        entity = ingester_pb2.Entity()
        entity.device.name = f"test_device_{i}"
        entities.append(entity)

    # Call the function
    size = estimate_message_size(entities)

    # Should return a positive integer
    assert isinstance(size, int)
    assert size > 0


def test_estimate_message_size_empty_list():
    """Test estimate_message_size with an empty entity list."""
    entities = []

    size = estimate_message_size(entities)

    # Should return base overhead (positive value for protobuf header)
    assert isinstance(size, int)
    assert size >= 0


def test_create_message_chunks_custom_chunk_size():
    """Test create_message_chunks with a custom chunk size."""
    # Create entities
    entities = []
    for i in range(10):
        entity = ingester_pb2.Entity()
        entity.device.name = f"test_device_{i}"
        entities.append(entity)

    # Use 3.5 MB chunk size (like orb-discovery)
    # Mock size estimation to return 5 MB (exceeds 3.5 MB limit)
    with patch("netboxlabs.diode.sdk.chunking.estimate_message_size", return_value=5 * 1024 * 1024):
        with patch.object(ingester_pb2.Entity, "ByteSize", return_value=600000):  # ~600KB each
            with patch.object(ingester_pb2.IngestRequest, "ByteSize", return_value=100):
                chunks = create_message_chunks(entities, max_chunk_size_mb=3.5)

    # Should have multiple chunks due to size limit
    assert len(chunks) > 1

    # All entities should be present
    total_entities = sum(len(chunk) for chunk in chunks)
    assert total_entities == 10


def test_create_message_chunks_preserves_order():
    """Test that create_message_chunks preserves entity order."""
    # Create entities with identifiable names
    entities = []
    for i in range(20):
        entity = ingester_pb2.Entity()
        entity.device.name = f"device_{i:03d}"
        entities.append(entity)

    # Mock to force multiple chunks
    with patch("netboxlabs.diode.sdk.chunking.estimate_message_size", return_value=10 * 1024 * 1024):
        with patch.object(ingester_pb2.Entity, "ByteSize", return_value=600000):
            with patch.object(ingester_pb2.IngestRequest, "ByteSize", return_value=100):
                chunks = create_message_chunks(entities)

    # Flatten chunks and verify order
    flattened = []
    for chunk in chunks:
        flattened.extend(chunk)

    assert len(flattened) == 20
    for i, entity in enumerate(flattened):
        assert entity.device.name == f"device_{i:03d}"


def test_create_message_chunks_with_iterable():
    """Test create_message_chunks with a generator/iterator input."""
    # Create generator
    def entity_generator():
        for i in range(5):
            entity = ingester_pb2.Entity()
            entity.device.name = f"test_device_{i}"
            yield entity

    # Should work with generator (converted to list internally)
    chunks = create_message_chunks(entity_generator())

    assert len(chunks) >= 1
    total_entities = sum(len(chunk) for chunk in chunks)
    assert total_entities == 5


def test_create_message_chunks_single_large_entity():
    """
    Test create_message_chunks with a single entity that exceeds chunk size.

    This edge case verifies the function doesn't fail when a single entity
    is larger than the chunk size limit.
    """
    entity = ingester_pb2.Entity()
    entity.device.name = "huge_device"
    entities = [entity]

    # Mock a very large entity (5 MB) that exceeds 3 MB limit
    with patch("netboxlabs.diode.sdk.chunking.estimate_message_size", return_value=5 * 1024 * 1024):
        with patch.object(ingester_pb2.Entity, "ByteSize", return_value=5 * 1024 * 1024):
            with patch.object(ingester_pb2.IngestRequest, "ByteSize", return_value=100):
                chunks = create_message_chunks(entities)

    # Should still return one chunk with the single entity
    assert len(chunks) == 1
    assert len(chunks[0]) == 1
    assert chunks[0][0].device.name == "huge_device"
