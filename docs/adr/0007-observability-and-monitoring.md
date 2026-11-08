# ADR 0007: Observability and Monitoring Stack

**Date:** 2026-11-08
**Status:** Accepted

## Context
As the homelab transitions to a production-like Kubernetes environment, we require deep visibility into hardware utilization, container health, and service availability. We need a solution that aligns with industry standards, integrates seamlessly into a GitOps workflow (configurable via code), and supports complex alerting logic.

## Decision
We will deploy the **`kube-prometheus-stack`** via Helm/ArgoCD as our primary observability platform.
1. **Metrics & Visualization:** Prometheus will scrape time-series metrics from `node_exporter` (hardware) and `cAdvisor` (containers), visualized through Grafana dashboards.
2. **Alerting Philosophy:** Prometheus Alertmanager will handle alert routing. Alerts will be configured to trigger on symptom-based, user-facing degradation (e.g., HTTP 5xx rates) rather than strictly underlying causes (e.g., high CPU utilization), minimizing alert fatigue.

## Consequences
* **Positive:** Provides a CKA-aligned, enterprise-grade metrics ecosystem fully manageable via YAML/GitOps.
* **Positive:** Alertmanager's webhook support enables automation for external status pages (see ADR 0008).
* **Negative:** Introduces a heavier resource footprint (~1-2 GB RAM) compared to basic ping monitors.
