# Capability Verification

## Declared vs verified

- `declared`: skill metadata says it supports a capability.
- `smoke_tested`: a minimal command/import/output path was actually run.
- `verified`: expected input/output contract and failure behavior were exercised.

Discovery alone never proves a skill is fully operational.

## Smoke tests

For critical skills, prefer:

- command exists;
- help/version runs;
- minimal fixture produces expected artifact;
- missing dependency fails visibly;
- generated file opens;
- output can be consumed by the next stage.

## Selection

Prefer verified skills when stakes are high. If unverified, state uncertainty and use a fallback or request user input.
