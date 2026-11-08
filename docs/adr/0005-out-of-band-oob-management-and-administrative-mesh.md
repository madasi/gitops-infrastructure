# ADR 0005: Out-of-Band (OOB) Management and Administrative Mesh

**Date:** 2026-11-08
**Status:** Accepted

## Context
The primary ingress path for public services relies on a GCP-hosted Pangolin reverse tunnel routed into the Kubernetes `ingress-nginx` controller. If the Kubernetes cluster fails, the tunnel drops, or the ingress controller crashes, administrative access to the underlying hypervisors is lost from outside the physical local area network. We also need a mechanism to route mobile device traffic through the homelab's ad-blocking DNS without exposing ports.

## Decision
We will deploy **Tailscale** as an out-of-band administrative mesh overlay.
1. The Tailscale daemon will be installed directly on the bare-metal Proxmox hosts (`pve-dell01`, `pve-dell02`, `pve-acer`) and core LXC containers, completely bypassing the Kubernetes networking stack.
2. The Technitium DNS LXC container (`192.168.1.45`) will be registered as the global nameserver in the Tailscale admin console with "Override Local DNS" enabled.
3. Mobile devices will run the Tailscale client continuously, routing cellular DNS requests to the homelab for ad-blocking and resolving internal `*.lab.internal` infrastructure.

## Consequences
* **Positive:** Administrative SSH and web UI access to the Proxmox hypervisors survives a total Kubernetes cluster collapse.
* **Positive:** Mobile devices receive network-wide ad-blocking and secure access to internal services without configuring split-tunnel VPNs manually.
* **Negative:** Introduces a third-party SaaS dependency (Tailscale coordination servers) for the control plane of the administrative mesh.
