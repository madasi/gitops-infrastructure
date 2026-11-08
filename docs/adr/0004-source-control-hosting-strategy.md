# ADR 0004: Source Control Hosting Strategy

**Date:** 2026-11-07
**Status:** Accepted

## Context
The Git repository is the absolute source of truth for the cluster. If the cluster goes offline, the Git repository must remain accessible to rebuild it. However, relying entirely on an external SaaS provider limits the self-sufficiency of the homelab environment.

## Decision
We will adopt a **Hybrid Multi-Remote Hosting Strategy**:
1. **Primary SaaS:** GitHub will serve as the primary origin and the public-facing portfolio link for prospective employers.
2. **Secondary SaaS:** GitLab SaaS will act as a redundant mirror.
3. **Internal Hosting:** We will self-host **Forgejo** within the homelab Kubernetes cluster. Once deployed, it will act as an internal mirror/read-replica.
4. **Secret Key Storage:** The master `age` private key required to decrypt the SOPS repository secrets will be stored securely offline in a 1Password vault, completely decoupled from the Git repositories.

## Consequences
* **Positive:** Ensures the GitOps pipeline and repository access survive a total local power or hardware failure (solving the chicken-and-egg bootstrap problem).
* **Positive:** Incorporating Forgejo satisfies the desire for self-hosted infrastructure while mitigating the risk of total lockout.
* **Negative:** Requires configuring Git to push to multiple remotes simultaneously or setting up automated CI/CD mirroring between GitHub, GitLab, and Forgejo.
