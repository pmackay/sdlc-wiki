---
source_urls:
  - https://modelcontextprotocol.io/specification/2026-07-28
  - https://modelcontextprotocol.io/specification/2026-07-28/changelog
  - https://modelcontextprotocol.io/community/governance
collected: 2026-10-11
published: 2026-07-28
authors: Model Context Protocol, a Series of LF Projects, LLC (MCP Steering Group)
publication: modelcontextprotocol.io — specification revision 2026-07-28
---

# Model Context Protocol — specification 2026-07-28

> Source assembly (2026-10-11): the specification's landing page, its Key Changes page for revision 2026-07-28 (against the previous revision, 2025-11-25), and the project's Governance page, each fetched verbatim as Markdown. The Mintlify "Documentation Index" banner was stripped from each page. The detailed sub-pages (architecture, base protocol, server and client features, transports, authorization) are not reproduced and remain at the source.

## Specification

<div id="enable-section-numbers" />

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open protocol that
enables seamless integration between LLM applications and external data sources and
tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating
custom AI workflows, MCP provides a standardized way to connect LLMs with the context
they need.

This specification defines the authoritative protocol requirements, based on the
TypeScript schema in
[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2026-07-28/schema.ts).

For implementation guides and examples, visit
[modelcontextprotocol.io](https://modelcontextprotocol.io).

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD
NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14)
\[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)]
\[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)] when, and only when, they
appear in all capitals, as shown here.

### Overview

MCP provides a standardized way for applications to:

* Share contextual information with language models
* Expose tools and capabilities to AI systems
* Build composable integrations and workflows

The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish
communication between:

* **Hosts**: LLM applications that initiate connections
* **Clients**: Connectors within the host application
* **Servers**: Services that provide context and capabilities

MCP takes some inspiration from the
[Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which
standardizes how to add support for programming languages across a whole ecosystem of
development tools. In a similar way, MCP standardizes how to integrate additional context
and tools into the ecosystem of AI applications.

### Key Details

#### Base Protocol

* [JSON-RPC](https://www.jsonrpc.org/) message format
* Stateless, self-contained requests
* Per-request capability negotiation

#### Features

Servers offer any of the following features to clients:

* **Resources**: Context and data, for the user or the AI model to use
* **Prompts**: Templated messages and workflows for users
* **Tools**: Functions for the AI model to execute

Clients may offer the following features to servers:

* **Elicitation**: Server-initiated requests for additional information from users

#### Additional Utilities

* Configuration
* Progress tracking
* Cancellation
* Error reporting

#### Extensions

Beyond the core protocol, MCP defines optional [extensions](/extensions/overview)
that add modular, specialized, or experimental functionality. Extensions
are always opt-in and require explicit support from both client and server, negotiated
during initialization. Notable extensions include:

* **[Tasks](/extensions/tasks/overview)**: Asynchronous execution of long-running
  operations, with polling, mid-flight input, and durable handles
* **[Skills over MCP](/community/working-groups/skills-over-mcp)**: Rich, structured
  instructions for agent workflows, discovered and consumed through MCP
* **[MCP Apps](/extensions/apps/overview)**: Interactive UI elements (charts, forms,
  video players) rendered inline within conversations

### Security and Trust & Safety

The Model Context Protocol enables powerful capabilities through arbitrary data access
and code execution paths. With this power comes important security and trust
considerations that all implementors must carefully address.

#### Key Principles

1. **User Consent and Control**
   * Users must explicitly consent to and understand all data access and operations
   * Users must retain control over what data is shared and what actions are taken
   * Implementors should provide clear UIs for reviewing and authorizing activities

2. **Data Privacy**
   * Hosts must obtain explicit user consent before exposing user data to servers
   * Hosts must not transmit resource data elsewhere without user consent
   * User data should be protected with appropriate access controls

3. **Tool Safety**
   * Tools represent arbitrary code execution and must be treated with appropriate
     caution.
     * In particular, descriptions of tool behavior such as annotations should be
       considered untrusted, unless obtained from a trusted server.
   * Hosts must obtain explicit user consent before invoking any tool
   * Users should understand what each tool does before authorizing its use

#### Implementation Guidelines

While MCP itself cannot enforce these security principles at the protocol level,
implementors **SHOULD**:

1. Build robust consent and authorization flows into their applications
2. Provide clear documentation of security implications
3. Implement appropriate access controls and data protections
4. Follow security best practices in their integrations
5. Consider privacy implications in their feature designs

### Learn More

Explore the detailed specification for each protocol component:

<CardGroup cols={5}>
  <Card title="Architecture" icon="sitemap" href="/specification/2026-07-28/architecture" />

  <Card title="Base Protocol" icon="code" href="/specification/2026-07-28/basic" />

  <Card title="Server Features" icon="server" href="/specification/2026-07-28/server" />

  <Card title="Client Features" icon="user" href="/specification/2026-07-28/client" />

  <Card title="Contributing" icon="pencil" href="/community/contributing" />
</CardGroup>

## Key Changes

<div id="enable-section-numbers" />

This document lists changes made to the Model Context Protocol (MCP) specification since
the previous revision, [2025-11-25](/specification/2025-11-25).

### Major changes

1. Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport. List endpoints (`tools/list`, `resources/list`, `prompts/list`) no longer vary per-connection. Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments ([SEP-2567](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2567)).

2. Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake. Every request now carries its protocol version and client capabilities in `_meta` (`io.modelcontextprotocol/protocolVersion`, `io.modelcontextprotocol/clientCapabilities`). Clients SHOULD identify themselves on each request (`io.modelcontextprotocol/clientInfo`), and servers SHOULD identify themselves in each result's `_meta` (`io.modelcontextprotocol/serverInfo`). Version mismatches return `UnsupportedProtocolVersionError` ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575)).

3. Add `server/discover`: servers MUST implement this RPC to advertise their supported protocol versions, capabilities, and identity. Clients MAY call it before any other request for up-front version selection, or use it as a backward-compatibility probe on STDIO ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575)).

4. Replace the HTTP GET endpoint and `resources/subscribe`/`resources/unsubscribe` with `subscriptions/listen`: a single long-lived POST-response stream for opted-in server-to-client change notifications. Clients opt in to specific types (`toolsListChanged`, `promptsListChanged`, `resourcesListChanged`, `resourceSubscriptions`); the server acknowledges and tags notifications with `io.modelcontextprotocol/subscriptionId`. Request-scoped notifications such as `notifications/progress` and `notifications/message` continue to flow on the response stream of the request they relate to, not the `subscriptions/listen` stream ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575)).

5. Remove `ping`, `logging/setLevel`, and `notifications/roots/list_changed`. Log level is now set per-request via `io.modelcontextprotocol/logLevel` in `_meta`; servers MUST NOT emit `notifications/message` for requests that did not include this field ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575)).

6. Move experimental tasks out of the core protocol and into an official extension (`io.modelcontextprotocol/tasks`). The redesigned extension replaces the blocking `tasks/result` method with polling via `tasks/get` and a new `tasks/update` for client-to-server input, removes `tasks/list`, and allows servers to return task handles unsolicited without per-request opt-in ([SEP-2663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663)).

7. Multi Round-Trip Requests (MRTR) pattern introduced which replaces the previous approach of sending server-initiated requests, such as `roots/list`, `sampling/createMessage`, or `elicitation/create`. Servers return an `InputRequiredResult` (`resultType: "input_required"`) whose `inputRequests` field carries the requests for the additional information needed to process the request. Clients respond with `inputResponses` on a retry of the original request providing the requested information. ([SEP-2322](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2322)).

8. All results now carry a required `resultType` field: `"complete"` for ordinary results and `"input_required"` for [multi round-trip request](/specification/2026-07-28/basic/patterns/mrtr) interim results. Clients **MUST** treat results from earlier-protocol servers that omit the field as `"complete"` ([SEP-2322](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2322)).

9. Remove SSE stream resumability and message redelivery (the `Last-Event-ID` header and SSE event IDs) from the Streamable HTTP transport. A broken response stream loses the in-flight request; clients **MUST** re-issue it as a new request with a new request ID ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575)).

### Minor changes

1. Add `extensions` field to `ClientCapabilities` and `ServerCapabilities` to support optional [extensions](/docs/extensions/overview) beyond the core protocol.
2. Document OpenTelemetry trace context propagation conventions for `_meta` keys (`traceparent`, `tracestate`, `baggage`) ([SEP-414](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/414)).
3. Servers **SHOULD** return tools from `tools/list` in a deterministic order to enable client-side caching and improve LLM prompt cache hit rates.
4. Require standard MCP request headers (`Mcp-Method`, `Mcp-Name`) on Streamable HTTP POST requests, and add support for custom headers from tool parameters via `x-mcp-header` ([SEP-2243](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2243)).
5. Require `ttlMs` and `cacheScope` fields on results returned by `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list` via a new `CacheableResult` interface. `ttlMs` is a freshness hint (in milliseconds) allowing clients to cache responses and reduce polling; `cacheScope` (`"public"` or `"private"`) controls whether shared intermediaries may cache the response. Both fields complement existing `listChanged` notifications ([SEP-2549](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2549)).
6. Change resource not found error code from `-32002` to `-32602` (Invalid Params) to align with JSON-RPC specification.
7. Authorization servers **SHOULD** include the `iss` parameter in authorization responses per
   [RFC 9207](https://datatracker.ietf.org/doc/html/rfc9207), and MCP clients **MUST** validate a
   present `iss` against the recorded issuer before redeeming the authorization code
   ([SEP-2468](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2468)).
8. Require MCP clients to specify an appropriate `application_type` during Dynamic Client
   Registration to avoid OpenID Connect redirect URI conflicts
   ([SEP-837](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/837)).
9. Clarify that client credentials are bound to the authorization server that issued them:
   clients **MUST** key persisted credentials by the issuer identifier, **MUST NOT** reuse them
   with a different authorization server, and **MUST** re-register when the authorization server
   changes ([SEP-2352](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2352)).
10. Loosen `inputSchema` and `outputSchema` to allow any JSON Schema 2020-12 keywords, and
    `structuredContent` to allow any JSON value. Add `$ref` resolution requirements and
    composition-keyword resource bounds
    ([SEP-2106](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2106)).
11. Remove the `notifications/elicitation/complete` notification and the
    `elicitationId` field of URL mode elicitation requests, both introduced in
    `2025-11-25`. Under the
    [Multi Round-Trip Requests](/specification/2026-07-28/basic/patterns/mrtr) pattern, the
    client learns the outcome of an out-of-band interaction by retrying the original
    request, so a server-initiated completion signal — and the identifier used to
    correlate it — no longer fit the protocol. Servers needing to correlate an
    elicitation across retries encode their own identifier in `requestState`.
12. Define an [error code allocation policy](/specification/2026-07-28/basic/index#error-codes)
    partitioning the JSON-RPC server-error range: `-32000` to `-32019` remains
    implementation-defined (existing SDK usage is grandfathered), `-32020` to `-32099` is
    reserved for the MCP specification. Renumber the error codes introduced in this draft
    accordingly — `HeaderMismatch` `-32001` → `-32020`, `MissingRequiredClientCapability`
    `-32003` → `-32021`, `UnsupportedProtocolVersion` `-32004` → `-32022` — and add
    `HeaderMismatchError` to the schema, which previously existed only in transport prose.

### Deprecated

Features listed here remain part of the specification but are scheduled for removal under the [feature lifecycle and deprecation policy](/community/feature-lifecycle). New implementations should not adopt them. The [deprecated features registry](/specification/2026-07-28/deprecated) tracks every feature currently in the Deprecated state.

1. Deprecate the Roots, Sampling, and Logging features
   ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)).
   These features remain fully functional during the deprecation window but new
   implementations should not add support for them. Suggested migrations: pass
   directories or files via tool parameters, resource URIs, or server
   configuration instead of Roots; integrate directly with LLM provider APIs
   instead of Sampling; log to `stderr` (stdio) or use OpenTelemetry instead of
   Logging.

2. Reclassify the HTTP+SSE transport (deprecated since protocol version
   `2025-03-26`) as Deprecated under the feature lifecycle policy
   ([SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596)).
   Migrate to [Streamable HTTP](/specification/2026-07-28/basic/transports/streamable-http).

3. Reclassify the `includeContext` values `"thisServer"` and `"allServers"`
   (soft-deprecated since protocol version `2025-11-25`) as Deprecated
   ([SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596)).
   Omit the field or use `"none"`; these values will be removed no later than
   the Sampling feature itself.

4. Deprecate the OAuth 2.0 Dynamic Client Registration Protocol
   ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)) as a client registration
   mechanism in favor of
   [Client ID Metadata Documents](/specification/2026-07-28/basic/authorization/client-registration#client-id-metadata-documents)
   ([PR #2858](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2858)).
   It remains available for backwards compatibility with authorization servers that do
   not support Client ID Metadata Documents.

### Other schema changes

1. `schema.json` now correctly reflects that the Typescript definition of minimum/maximum/default are `number`'s and not just `integers`. This was caused by running the generator using `--defaultNumberType integer` ([PR#2710](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2710)).

### Governance and process updates

1. Adopt a specification
   [feature lifecycle and deprecation policy](/community/feature-lifecycle)
   defining the Active, Deprecated, and Removed feature states, a minimum
   twelve-month deprecation window, and a
   [registry of deprecated features](/specification/2026-07-28/deprecated)
   ([SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596)).

### Process changes

1. Formalize PR-based SEP workflow with markdown files in `seps/` directory, PR-derived numbering, sponsor responsibilities, and status management via PR labels ([SEP-1850](https://github.com/modelcontextprotocol/specification/pull/1850)).

### Full changelog

For a complete list of all changes that have been made since the last protocol revision,
[see GitHub](https://github.com/modelcontextprotocol/specification/compare/2025-11-25...2026-07-28).

## Governance and Stewardship

> Learn about the Model Context Protocol's governance structure and how to participate in the community

The Model Context Protocol (MCP) follows a formal governance model to ensure transparent decision-making and community participation. This document outlines how the project is organized and how decisions are made.

### General Project Policies

Model Context Protocol has been established as **Model Context Protocol a Series of LF Projects, LLC**. Policies applicable to Model Context Protocol and participants in Model Context Protocol, including guidelines on the usage of trademarks, are located at [https://www.lfprojects.org/policies/](https://www.lfprojects.org/policies/). Governance changes approved as per the provisions of this governance document must also be approved by LF Projects, LLC.

Model Context Protocol participants acknowledge that the copyright in all new contributions will be retained by the copyright holder as independent works of authorship and that no contributor or copyright holder will be required to assign copyrights to the project.

Except as described below, all code and specification contributions to the project must be made using the Apache License, Version 2.0 (available here: [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)) (the "Project License").

All outbound code and specifications will be made available under the Project License. The Core Maintainers may approve the use of an alternative open license or licenses for inbound or outbound contributions on an exception basis.

All documentation (excluding specifications) will be made available under Creative Commons Attribution 4.0 International license, available at: [https://creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0).

### Technical Governance

The MCP project adopts a hierarchical structure, similar to Python, PyTorch, and other open source projects:

| Role | Scope |
| - | - |
| **Lead Maintainers (BDFL)** | Final decision authority |
| **Core Maintainers** | Overall project direction |
| **Maintainers** | Working Groups, SDKs, components |
| **Contributors** | Issues, PRs, discussions |

* **Contributors** file issues, make pull requests, and contribute to the project.
* **Maintainers** drive components within the MCP project, such as SDKs, documentation, and Working Groups.
* **Core Maintainers** drive the overall project direction and oversee contributors and maintainers.
* **Lead Maintainers** are the final decision makers (also known as BDFL - Benevolent Dictator for Life).

Together, Maintainers, Core Maintainers, and Lead Maintainers form the **MCP Steering Group**.

All maintainers are expected to have a strong bias towards MCP's design philosophy. Membership in the technical governance process is for individuals, not companies. That is, there are no seats reserved for specific companies, and membership is associated with the person rather than the company employing that person.

#### Communication Channels

Technical governance is facilitated through a shared [Discord server](https://discord.gg/6CSzBmMkjX) for all maintainers. Each maintainer group can choose additional communication channels, but all decisions and their supporting discussions must be recorded and made transparently available on the Discord server.

#### Roles

The [Contributor Ladder](/community/contributor-ladder) is the canonical definition of each role — its requirements, responsibilities, privileges, advancement process, and inactivity policy. This section gives a conceptual overview of how the roles relate to governance.

**Maintainers** steward specific areas such as SDKs, documentation, or [Working Groups](/community/working-interest-groups). They make decisions for their area independently and escalate to Core Maintainers when needed. Maintainers have write access to their respective repositories.

**Core Maintainers** steer the MCP specification and overall project direction. They can veto Maintainer decisions by majority vote, resolve disputes, and appoint or remove Maintainers. Core Maintainers have admin access to all MCP repositories but use the same pull-request workflow as outside contributors.

**Lead Maintainers** hold final authority and can veto any decision by Core Maintainers or Maintainers — the role commonly known as Benevolent Dictator for Life (BDFL). Lead Maintainers appoint and remove Core Maintainers, and are administrators on all project infrastructure. They are part of the Core Maintainer group and are expected to publicly articulate their reasoning.

The [Contributor Ladder](/community/contributor-ladder) also defines the **Member** and **Community Moderator** roles, which sit outside the Steering Group.

#### Decision Process

The Core Maintainer group meets every two weeks to discuss and vote on proposals, as well as discuss any topics needed. The shared Discord server can be used to discuss and vote on smaller proposals if needed.

The Lead Maintainer, Core Maintainer, and Maintainer group should attempt to meet in person every three to six months.

### Processes

Core Maintainers and Lead Maintainers are responsible for all aspects of Model Context Protocol, including documentation, issues, suggestions for content, and all other parts under the [MCP project](https://github.com/modelcontextprotocol). Maintainers are responsible for documentation, issues, and suggestions of content for their area of the MCP project, but are encouraged to partake in general maintenance of the MCP projects.

Maintainers, Core Maintainers, and Lead Maintainers should use the same contribution process as external contributors, rather than making direct changes to repos. This provides insight into intent and opportunity for discussion.

#### Working Groups and Interest Groups

MCP collaboration and contributions are organized around two structures: [Working Groups and Interest Groups](/community/working-interest-groups).

* **Interest Groups** identify and articulate problems that MCP should address through open discussions
* **Working Groups** develop concrete solutions by producing deliverables like SEPs or implementations

For details on how to create, participate in, and facilitate these groups, see the [Working and Interest Groups](/community/working-interest-groups) documentation.

#### Specification Enhancement Proposals (SEPs)

Proposed changes to the specification must be submitted as [Specification Enhancement Proposals (SEPs)](/community/sep-guidelines). SEPs are the primary mechanism for proposing major new features, collecting community input, and documenting design decisions.

For the complete SEP process, format requirements, and status workflow, see the [SEP Guidelines](/community/sep-guidelines).

#### Maintenance Responsibilities

Components without dedicated maintainers (such as documentation) fall under Core Maintainer responsibility. These follow standard contribution guidelines through pull requests, with maintainers handling reviews and escalating to Core Maintainer review for any significant changes.

Core Maintainers and Maintainers are encouraged to improve any part of the MCP project, regardless of formal maintenance assignments.

### Communication

#### Core Maintainer Meetings

The Core Maintainer group meets on a bi-weekly basis to discuss proposals and the project. Notes on proposals should be made public. The Core Maintainer group will strive to meet in person every 3-6 months.

#### Public Chat

The MCP project maintains a [public Discord server](https://discord.gg/6CSzBmMkjX) with open chats for interest groups. The MCP project may have private channels for certain communications.

### Nominating, Confirming, and Removing Maintainers

Membership in maintainer groups is given to **individuals** on a merit basis after demonstrated expertise and alignment with MCP's direction. Membership is associated with the person, not their employer, and has no term limit.

The nomination process, sponsorship requirements, review timeline, and inactivity criteria for each role are defined in the [Contributor Ladder's Advancement Process](/community/contributor-ladder#advancement-process).

### Current Lead Maintainers

* David Soria Parra
* Den Delimarsky

### Current Core Maintainers

* Peter Alexander
* Caitie McCaffrey
* Kurtis Van Gent
* Clare Liguori
* Paul Carleton
* Nick Cooper

### Emeritus

* Justin Spahr-Summers (Co-Inventor, Lead Maintainer Emeritus)
* Basil Hosmer (Core Maintainer Emeritus)
* Che Liu (Core Maintainer Emeritus)
* Nick Aldridge (Core Maintainer Emeritus)

### Current Maintainers and Working Groups

Refer to [the maintainer list](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md).
