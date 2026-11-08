# Infrastructure Backlog & Action Items

## Backup & Disaster Recovery
- [ ] Define VZDump Retention Policy: Document how many daily/weekly VM backups to retain per node before pruning.
- [ ] Map Cross-Node Backup Targets: Explicitly document which Proxmox host backs up to which (e.g., `pve-dell01` writes to `pve-acer`).
- [ ] Establish Restore Testing Cadence: Schedule a recurring calendar event to perform a dry-run worker VM restore.

## Automation & CI/CD
- [ ] Configure `git remote set-url --add --push origin` for simultaneous manual pushes to GitHub and GitLab.
- [ ] Research and implement GitHub Actions workflow for automated mirroring to GitLab and internal Forgejo.
