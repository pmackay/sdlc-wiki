---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd federation

`bd federation` — *"manage peer-to-peer federation"* (requires CGO): sharing beads across repositories and organizations without a central server.

The quickstart case is the striking one: federate two machines through a **GCS or S3 bucket**, *"with no server to run."* Push and pull go through object storage, so two agents on two machines in two organizations can share a work graph with nothing but a bucket and credentials. `federation.exclude_types` defaults to `[wisp]`, so ephemeral operational work stays local by design and only durable beads cross the boundary ([[beads-mol]]).

Federation is the point at which this layer stops being per-project. A framework is per-repo by nature, a harness is per-machine, a runtime is per-deployment — but state can be *shared*, and beads is the only tool here that treats the work graph as something that spans organizational boundaries. Its sibling [[beads-repo]] handles the intra-organization case (multi-repo routing, cross-repo dependencies).

The `bead` gate type is the visible casualty of an earlier iteration of this idea: it waits on *"a bead in another rig to close"* and *"cannot be checked because multi-rig routing was removed"*, so those gates must be resolved by hand ([[beads-gate]]). Worth recording as evidence that cross-boundary coordination is the hard part, not cross-boundary storage.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-repo]] — multi-repo within one organization.
- [[beads-mol]] — wisps, excluded from federation by default.
- [[beads-dolt]] — the single-remote sync federation generalizes.
