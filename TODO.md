# Tactical Backlog & Action Items

## Immediate Next Steps (Hypervisor Bootstrap)
- [ ] **Flash Installation Media:** Write Proxmox VE ISO to USB drive.
- [ ] **Install Proxmox OS:** Provision base OS on `pve-dell01` and `pve-acer` laptops.
- [ ] **Configure Tailscale OOB:** Install Tailscale directly on the new Proxmox hosts for emergency administrative mesh access.

## Documentation & Architecture
- [ ] **Document IPAM:** Create `docs/architecture/network.md` and document Technitium/AT&T DHCP scopes and static infrastructure IP reservations.
- [ ] **Define VZDump Retention Policy:** Document daily/weekly VM backup retention counts per node to prevent local disk exhaustion.
- [ ] **Map Cross-Node Backup Targets:** Explicitly document which Proxmox host backs up to which local path.
- [ ] **Establish Restore Testing Cadence:** Add a recurring task for dry-run worker VM restores from VZDump archives.

## Core Services Deployment
- [ ] **Deploy Centralized SMTP Relay:** Stand up a Postfix container/VM to route unauthenticated internal alerts out via Google Workspace.
- [ ] **Configure External Status Page:** Deploy Uptime Kuma on the GCP `e2-micro` instance.
- [ ] **Wire Prometheus to Status Page:** Configure Alertmanager webhooks to update Uptime Kuma automatically.

## Automation & CI/CD
- [ ] **GitHub Actions Mirroring:** Research and implement a workflow to automatically mirror the GitHub repository state to GitLab and the internal Forgejo instance.
