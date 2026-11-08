# 0. Record Architecture Decisions

Date: 2026-11-07

## Status
Accepted

## Context
We need a structured, auditable method to record architectural choices, trade-offs, and technical rationale across the homelab infrastructure lifecycle.

## Decision
We will use Architecture Decision Records (ADRs) stored directly within the repository in Markdown format (`docs/adr/NNNN-title.md`).

## Consequences
- Every non-trivial architectural change (DNS strategy, hypervisor choices, storage topology, ingress) will require a dedicated ADR.
- Rationale and trade-offs remain transparent and historical context is preserved over time.
