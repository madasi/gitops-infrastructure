# Infrastructure Roadmap

This document outlines the strategic phases of the homelab infrastructure. The goal is to evolve from a manually bootstrapped environment into a fully automated, API-driven private cloud, heavily aligned with CKA principles and enterprise GitOps standards.

## Phase 1: Foundation and GitOps Bootstrap (Current)
Establish the core virtualization platform, secure the network perimeter, and implement declarative continuous delivery.

- [x] High-Availability Git routing and repository scaffolding.
- [x] Architectural documentation (ADRs 0001 through 0009).
- [ ] Bare-metal Proxmox hypervisor provisioning.
- [ ] Out-of-band management mesh via Tailscale.
- [ ] Split-horizon DNS and DHCP fail-safes (Technitium/AT&T IP Passthrough).
- [ ] OpenTofu VM orchestration and Ansible cluster bootstrap (`kubeadm`).
- [ ] ArgoCD GitOps pipeline with SOPS in-repo secret encryption.

## Phase 2: Observability and Incident Communication
Implement comprehensive telemetry, alerting, and out-of-band user communication.

- [ ] Deploy `kube-prometheus-stack` for cluster and hardware metrics.
- [ ] Deploy external Uptime Kuma status page to the GCP ingress node.
- [ ] Configure centralized Postfix SMTP relay for internal alerting.
- [ ] Implement Grafana Loki and Promtail/Vector for centralized, label-based log aggregation.

## Phase 3: Dynamic Automation and IPAM
Replace static configurations with API-driven inventory and centralized address management.

- [ ] **Deploy NetBox:** Spin up NetBox within the Kubernetes cluster to serve as the single source of truth for IPAM and DCIM.
- [ ] **Dynamic Ansible Inventory:** Deprecate the static `inventory.ini` file. Configure Ansible to query the NetBox API dynamically for host execution.
- [ ] **Automated DNS Records:** Integrate Technitium with NetBox or Kubernetes ExternalDNS to automate record creation during workload deployment.

## Phase 4: Storage and High Availability
Prepare the cluster for highly available (HA) stateful workloads and hardware failures.

- [ ] Migrate local-path persistent storage to a clustered storage solution (e.g., Longhorn or Ceph) for stateful pod failover.
- [ ] Implement automated VZDump backup verification testing.
