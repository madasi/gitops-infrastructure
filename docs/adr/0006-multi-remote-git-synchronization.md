# ADR 0006: Multi-Remote Git Synchronization

**Date:** 2026-11-08
**Status:** Accepted

## Context
Following the hybrid hosting strategy (ADR 0004), the repository exists across GitHub (Primary/Portfolio), GitLab SaaS (Secondary), and Forgejo (Internal). We need a mechanism to ensure all remotes remain synchronized so ArgoCD can pull the latest state regardless of upstream availability.

## Decision
We will utilize a two-phased synchronization approach:
* **Phase 1 (Bootstrap):** The local Git configuration on the management workstation will be modified to include multiple push URLs under the `origin` remote. A single `git push` command will push commits to both GitHub and GitLab simultaneously.
* **Phase 2 (Endgame CI/CD):** Once the cluster is stable, we will implement a GitHub Actions workflow. Pushes will go exclusively to GitHub, which will trigger a webhook/action to automatically mirror the repository state to GitLab and the internal Forgejo instance.

## Consequences
* **Positive:** Phase 1 guarantees redundancy from day one without brittle automation blocking the bootstrap process.
* **Positive:** Phase 2 automates the flow, ensuring ArgoCD can fall back to Forgejo instantly without manual intervention if GitHub experiences an outage.
* **Negative:** Phase 1 requires the administrator to push from a specifically configured workstation. Phase 2 introduces a dependency on GitHub Actions for internal cluster updates.
