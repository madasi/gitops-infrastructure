# ADR 0001: Network Topology, Ingress, and External Exposure

**Date:** 2026-11-07
**Status:** Accepted

## Context
The homelab requires both internal resolution for administrative tools and secure public exposure for specific family services (Outline, Authentik). The physical network sits behind an AT&T residential gateway that prevents custom DNS injection. Furthermore, opening inbound firewall ports (80/443) on the residential IP exposes the network to direct internet scanning and potential ISP restrictions.

## Decision
1. **Local DNS & DHCP:** We will deploy Technitium DNS in an isolated LXC container on the Proxmox host. Technitium will handle local DHCP leases, bypassing the AT&T gateway limitations, and resolve `*.lab.internal` and `*.madasi.com` (split-horizon) to the internal Kubernetes Ingress IP.
2. **Cluster Ingress:** We will standardize on `ingress-nginx` as the sole Kubernetes ingress controller. It aligns with CKA objectives and natively supports Authentik ForwardAuth annotations without manual proxy file configuration.
3. **Public Exposure (Zero Open Ports):** We will utilize a GCP Free Tier (`e2-micro`) instance running the Pangolin Server. A local Pangolin client (running in an LXC container) will establish an outbound WireGuard tunnel to GCP. Public traffic hitting `*.madasi.com` will route through GCP, down the tunnel, and into the local `ingress-nginx` controller.

## Consequences
* **Positive:** The residential IP remains entirely hidden from public DNS and Shodan scanners. Internal services continue resolving instantly even if the internet drops.
* **Positive:** `ingress-nginx` allows dynamic service routing and SSO integration without hand-editing static SWAG/NGINX `.conf` files.
* **Negative:** If the isolated Technitium LXC container goes offline, local DNS fails until the AT&T gateway's emergency fallback DHCP pool kicks in.
