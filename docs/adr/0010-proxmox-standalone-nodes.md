# ADR 0010: Proxmox Standalone Nodes vs. Clustering

**Date:** 2026-11-08
**Status:** Accepted

## Context
The homelab infrastructure is being built on a foundation of recycled consumer laptop hardware (Dell Inspiron, Acer, etc.). The target state is a three-node hypervisor pool hosting a highly available Kubernetes (K3s) cluster. We must decide whether to link these underlying hypervisors using Proxmox VE's native clustering engine.

## Decision
We will explicitly **NOT** join the Proxmox nodes into a native cluster. The nodes will operate as completely independent, standalone hypervisors. 

1. High Availability (HA) and clustering will be delegated entirely to the Kubernetes (K3s) layer.
2. Cross-node communication will be handled by the Tailscale out-of-band mesh and K3s networking, not Proxmox's Corosync engine.

## Consequences
* **Positive (Stability):** Proxmox's Corosync/Pacemaker stack requires strict, ultra-low latency (< 2ms). Consumer laptops frequently trigger Corosync timeouts. Avoiding the cluster prevents split-brain scenarios and catastrophic fencing where hypervisors unexpectedly hard-reboot themselves.
* **Positive (Decoupling):** The Kubernetes workloads become truly hardware-agnostic, relying only on standard Linux OS access rather than deep hypervisor-level orchestration.
* **Negative (Management Overhead):** Proxmox Cluster File System (`pmxcfs`) is not shared. Proxmox users (`opentofu@pve`), API tokens, LXC templates, and ISOs do not automatically sync across nodes and must be provisioned individually.
