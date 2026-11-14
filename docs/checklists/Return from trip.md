Homelab Return & Refactor Fixes Checklist
1. Fix the Broken Refactor Branch (Safety Walkaround)
[ ] Move the tasks from archive/harden-proxmox.yaml directly into roles/proxmox_harden/tasks/main.yml (so the laptops don't accidentally fall asleep when the lids close).

[ ] Add become: true to the Technitium install playbook (otherwise apt and systemd will fail immediately upon execution).

[ ] Put the upstream DNS forwarders for Cloudflare and Google back into the Technitium configuration.

[ ] Add no_log: true to all the Technitium API uri tasks (to keep that API token out of the terminal scrollback).

[ ] Update the dns_records role to query the existing IP address and compare it to the inventory (instead of blindly accepting "already exists" when the IP might be wrong).

[ ] Swap the flaky tilde expansion for the SSH key lookup for an explicit variable path.

2. Test & Merge
[ ] Run a syntax check on the playbooks using ansible-playbook --syntax-check.

[ ] Run the DNS provisioning deployment to verify the roles execute cleanly and the DNS records update correctly.

[ ] Merge the refactor/ansible-roles branch into main (git checkout main, git pull, git merge).

3. Tailscale Subnet Router Setup
[x] Enable IPv4 forwarding on pve-dell01 by setting net.ipv4.ip_forward = 1 in sysctl.

[x] Advertise the home subnet by running tailscale up with the advertise-routes=192.168.1.0/24 flag.

[x] Log into the Tailscale admin console, find pve-dell01, and approve the subnet route.

[x] Verify remote access by pinging dns-primary at 192.168.1.53 over the Tailscale connection.