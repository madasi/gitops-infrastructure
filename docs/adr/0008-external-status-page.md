# ADR 0008: External Status Page and Incident Communication

**Date:** 2026-11-08
**Status:** Accepted

## Context
Users (family members) require a centralized, reliable method to check service status and view planned maintenance windows. A status page hosted inside the local Kubernetes cluster is a single point of failure; if the cluster or ISP drops, the status page drops with it. We must host this externally, but the external GCP `e2-micro` instance is constrained to 1 GB of RAM.

## Decision
We will deploy **Uptime Kuma** on the external GCP Free Tier `e2-micro` instance.
1. **Out-of-Band Hosting:** Uptime Kuma will run alongside the Pangolin reverse tunnel, bound to a public subdomain (e.g., `status.madasi.com`).
2. **Resource Efficiency:** Uptime Kuma's Node.js/SQLite architecture ensures memory usage remains well below the GCP instance limits, avoiding the overhead of heavier tools like Cachet.
3. **Automated Updates:** Internal Prometheus Alertmanager will be configured to send webhooks to Uptime Kuma's API to update service statuses automatically during degradation.

## Consequences
* **Positive:** Incident communication survives a total homelab power or ISP failure.
* **Positive:** Users have a professional, single pane of glass for maintenance notifications.
* **Negative:** Requires managing a persistent workload and SQLite database on the external cloud node.
