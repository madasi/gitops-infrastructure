# ADR 0002: GitOps Secret Management

**Date:** 2026-11-07
**Status:** Accepted

## Context
A strict GitOps methodology dictates that the Git repository is the single source of truth for cluster state. However, committing plaintext secrets (Gandi API tokens, Authentik database passwords) to version control is a critical security vulnerability. 

## Decision
We will use **SOPS (Secrets OPerationS)** combined with **age** for in-repo encryption, rejecting external dependencies like HashiCorp Vault or External Secrets Operator (ESO).

1. All secrets will be encrypted using a dedicated `age` public key before being committed.
2. The SOPS configuration (`.sops.yaml`) will ensure only YAML values (`data` / `stringData`) are encrypted, leaving metadata readable for Git diffs.
3. The private `age` key will be manually injected as a Kubernetes Secret into the ArgoCD namespace exactly once during cluster bootstrap.
4. ArgoCD will use the SOPS plugin to decrypt the manifests in-memory during the sync loop.

## Consequences
* **Positive:** The entire infrastructure state, including secrets, is portable and self-contained within the Git repository without relying on third-party SaaS secret managers or heavy in-cluster databases.
* **Negative:** The private `age` key becomes the master key to the kingdom. If it is lost, all encrypted secrets in the repository become unrecoverable.
