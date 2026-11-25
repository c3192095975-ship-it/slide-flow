# Capability Verification

## Capability states
- `declared`: metadata/documentation claims the capability.
- `discovered`: capability is currently available in this environment.
- `smoke_tested`: a minimal representative task completed successfully.
- `verified`: input/output contract, error behavior, compatibility and a representative artifact were checked.

Prefer the highest verified capability that fits task and scope. If only declared/discovered, treat it as unverified and run a minimal safe test when practical. Do not claim verification based only on name, description, repository popularity or installation.

Record `skill_id`, `capability_slot`, `state`, `test_case`, `tested_at`, `environment`, `result`, `known_limits`, and `artifact_reference`. Verification is environment-specific and may expire after major version, dependency or platform changes.
