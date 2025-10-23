#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs, Diode - SDK."""

from netboxlabs.diode.sdk.client import (
    DiodeClient,
    DiodeDryRunClient,
    OtlpClient,
    load_dryrun_entities,
)

assert DiodeClient
assert DiodeDryRunClient
assert OtlpClient
assert load_dryrun_entities
