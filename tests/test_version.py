#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs - Tests."""

from netboxlabs.diode.sdk.version import (
    __commit_hash__,
    __track__,
    __version__,
    version_display,
    version_semver,
)


def test_version_display_returns_correct_format():
    """Check the format of the version display."""
    expected = f"v{__version__}-{__track__}-{__commit_hash__}"
    assert version_display() == expected


def test_version_display_returns_string():
    """Check that version display returns a string."""
    assert isinstance(version_display(), str)


def test_version_semver_returns_correct_version():
    """Check that version semver returns the correct version."""
    assert version_semver() == __version__


def test_version_semver_returns_string():
    """Check that version semver returns a string."""
    assert isinstance(version_semver(), str)
