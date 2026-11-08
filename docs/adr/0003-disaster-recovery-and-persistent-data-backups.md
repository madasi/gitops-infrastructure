# ADR 0003: Disaster Recovery and Persistent Data Backups

**Date:** 2026-11-07
**Status:** Accepted

## Context
The homelab utilizes local-path storage on individual Kubernetes VMs (`k8s-node01`, `k8s-node02`) rather than a centralized NAS/SAN. Dedicated cloud backup storage is currently cost-prohibitive. We need a zero-cost method to ensure stateful workloads (Authentik, Home Assistant) and node configurations survive a localized hardware failure.

## Decision
We will rely on **Cross-Node Proxmox VM Backups (VZDump)**. 
1. Each unclustered bare-metal Proxmox host (`pve-dell01`, `pve-dell02`, `pve-acer`) will be configured with a backup storage target pointing to the local disks of a *different* host in the environment (e.g., `pve-acer` backs up its VMs to a shared directory on `pve-dell01`).
2. Backups will capture the entire VM state, inherently backing up the Kubernetes persistent volumes mounted within them.

## Consequences
* **Positive:** Achieves complete data redundancy and disaster recovery capabilities without incurring any monthly cloud storage costs.
* **Positive:** VM-level backups allow for rapid, single-click restoration of an entire worker node if a laptop's physical drive fails.
* **Negative:** Storing backup archives locally reduces the usable storage capacity on each bare-metal node for active workloads.
