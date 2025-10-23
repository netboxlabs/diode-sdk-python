#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs, Diode - SDK."""

from netboxlabs.diode.sdk.client import (
    DiodeClient,
    DiodeDryRunClient,
    DiodeOTLPClient,
    load_dryrun_entities,
)

assert DiodeClient
assert DiodeDryRunClient
assert DiodeOTLPClient
assert load_dryrun_entities
