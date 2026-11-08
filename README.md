# Homelab Infrastructure & GitOps Pipeline

This repository contains the declarative Infrastructure as Code (IaC), GitOps manifests, and automation runbooks for a bare-metal homelab environment. It serves as a testing ground for cloud-native architectures, Kubernetes administration (CKA alignment), and observability.

## Architecture Overview

The environment is built on repurposed hardware running independent, unclustered Proxmox VE hosts to maximize resource allocation and prevent Corosync quorum locks during maintenance.

* **Hypervisor:** Proxmox VE 8.x (Standalone Hosts)
* **Infrastructure Provisioning:** OpenTofu (VMs & LXC Containers)
* **Configuration Management:** Ansible (OS Hardening, Containerd, Kubeadm Bootstrap)
* **Kubernetes:** v1.31 (kubeadm, Flannel CNI, Local Path Provisioning)
* **GitOps Engine:** ArgoCD
* **Secret Management:** Mozilla SOPS with `age` encryption
* **Ingress & Networking:** ingress-nginx, cert-manager (Let's Encrypt DNS-01), Technitium DNS, and Pangolin (Reverse Tunnel)

## Repository Structure

* `/docs/adr/` - Architecture Decision Records (ADRs) explaining technical trade-offs.
* `/automation/ansible/` - Playbooks for host preparation and Kubernetes cluster assembly.
* `/infrastructure/tofu/` - OpenTofu HCL definitions for virtual machines and LXC nodes.
* `/kubernetes/base/` - Raw application manifests.
* `/kubernetes/overlays/` - Kustomize patches for specific deployments (Authentik, Outline, Prom-Stack).
* `/scripts/` - Utility scripts for maintenance and etcd backups.

## Deployment Pipeline

1. Physical hosts are provisioned with Proxmox VE 8.x and Debian 12 cloud-init templates.
2. OpenTofu (`/infrastructure/tofu`) stamps out the control plane and worker VMs.
3. Ansible (`/automation/ansible`) configures the OS and initializes the Kubernetes cluster via `kubeadm`.
4. ArgoCD is deployed to the cluster and pointed at this repository.
5. All subsequent application deployments (Authentik, Home Assistant, Observability) are managed entirely via declarative Git commits. Secrets are encrypted in-repo using SOPS and decrypted in-memory by ArgoCD.
