#!/usr/bin/env python
# Copyright 2026 NetBox Labs Inc
"""
Message chunking utilities for Diode SDK.

This module provides utilities for chunking large lists of entities into
size-appropriate chunks for gRPC ingestion, ensuring no chunk exceeds
the gRPC message size limit.
"""

from collections.abc import Iterable

from .diode.v1 import ingester_pb2


def create_message_chunks(
    entities: Iterable[ingester_pb2.Entity], max_chunk_size_mb: float = 3.0
) -> list[list[ingester_pb2.Entity]]:
    """
    Create size-aware chunks from entities using greedy bin-packing.

    This function chunks entities to ensure each chunk stays under the specified
    size limit. It uses a greedy bin-packing algorithm that accumulates entities
    until adding the next entity would exceed the limit, then starts a new chunk.

    The default chunk size of 3.0 MB provides a safe margin below the gRPC 4 MB
    message size limit, accounting for protobuf serialization overhead.

    Args:
        entities: Iterable of Entity protobuf messages to chunk
        max_chunk_size_mb: Maximum chunk size in MB (default 3.0)

    Returns:
        List of entity chunks, each under max_chunk_size_mb. Returns at least
        one chunk even if the input is empty.

    Examples:
        >>> entities = [entity1, entity2, entity3, ...]
        >>> chunks = create_message_chunks(entities)
        >>> for chunk in chunks:
        ...     client.ingest(chunk)

        >>> # Use a custom chunk size
        >>> chunks = create_message_chunks(entities, max_chunk_size_mb=3.5)

    """
    # Convert iterable to list if necessary for size estimation
    if not isinstance(entities, list):
        entities = list(entities)

    if not entities:
        return [entities]

    # Convert MB to bytes
    max_chunk_size_bytes = int(max_chunk_size_mb * 1024 * 1024)

    # Quick check: if all entities fit in one chunk, return early
    total_size = estimate_message_size(entities)
    if total_size <= max_chunk_size_bytes:
        return [entities]

    # Greedy bin-packing: accumulate entities until limit reached
    base_overhead = ingester_pb2.IngestRequest().ByteSize()
    chunks = []
    current_chunk: list[ingester_pb2.Entity] = []
    current_chunk_size = base_overhead  # Start with overhead for the chunk

    for entity in entities:
        entity_size = entity.ByteSize()
        projected_size = current_chunk_size + entity_size

        # Check if adding this entity would exceed limit
        if current_chunk and projected_size > max_chunk_size_bytes:
            # Finalize current chunk and start new one
            chunks.append(current_chunk)
            current_chunk = [entity]
            current_chunk_size = base_overhead + entity_size
        else:
            # Add entity to current chunk
            current_chunk.append(entity)
            current_chunk_size = projected_size

    # Add final chunk if not empty
    if current_chunk:
        chunks.append(current_chunk)

    return chunks if chunks else [entities]


def estimate_message_size(entities: Iterable[ingester_pb2.Entity]) -> int:
    """
    Estimate the serialized size of entities in bytes.

    Calculates the total size by summing individual entity sizes plus the
    IngestRequest protobuf overhead.

    Args:
        entities: Iterable of Entity protobuf messages

    Returns:
        Estimated size in bytes including IngestRequest overhead

    Examples:
        >>> entities = [entity1, entity2, entity3]
        >>> size_bytes = estimate_message_size(entities)
        >>> size_mb = size_bytes / (1024 * 1024)
        >>> print(f"Estimated size: {size_mb:.2f} MB")

    """
    # Convert iterable to list if necessary
    if not isinstance(entities, list):
        entities = list(entities)

    base_overhead = ingester_pb2.IngestRequest().ByteSize()
    entity_sizes_sum = sum(entity.ByteSize() for entity in entities)
    return base_overhead + entity_sizes_sum
