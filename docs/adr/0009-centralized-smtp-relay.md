# ADR 0009: Centralized SMTP Relay

**Date:** 2026-11-08
**Status:** Accepted

## Context
Numerous internal homelab services (Proxmox VZDump, Alertmanager, ArgoCD, TrueNAS, etc.) require the ability to send outbound email notifications. Configuring individual SMTP authentication, TLS parameters, and Google Workspace App Passwords inside every application creates a massive configuration sprawl and a security risk during credential rotation.

## Decision
We will deploy a **Centralized Postfix SMTP Relay** inside the local network.
1. **Internal Ingress:** The Postfix container will accept unauthenticated SMTP traffic on Port 25 exclusively from trusted internal IP subnets.
2. **External Egress:** Postfix will act as the sole outbound gateway, handling TLS encryption and authenticating against Google Workspace (`smtp.gmail.com` or Workspace SMTP Relay) using a single, centrally managed App Password encrypted via SOPS.

## Consequences
* **Positive:** Drastically simplifies email configuration for all internal apps down to a single internal IP and port.
* **Positive:** Credential rotation is centralized to a single SOPS secret.
* **Negative:** If the Postfix container fails, all outbound homelab email alerting is temporarily blackholed.
