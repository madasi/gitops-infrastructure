# Network Architecture & IP Address Management (IPAM)

## DHCP Scopes & Gateway Topology
The homelab utilizes a split-horizon DHCP configuration to prevent IP conflicts while maintaining an emergency fallback if the cluster goes down.

| Service | Role | Range | Gateway |
| :--- | :--- | :--- | :--- |
| **Technitium (Primary)** | Primary DNS/DHCP (LXC) | `192.168.1.100` - `192.168.1.200` | `192.168.1.254` |
| **AT&T BGW620 (Fallback)** | Emergency DHCP | `192.168.1.240` - `192.168.1.250` | `192.168.1.254` |

*Note: The AT&T gateway is restricted to a 10-IP pool. Technitium handles all primary local routing and DNS ad-blocking.*

## Static Infrastructure Reservations
Core infrastructure components are assigned static IP addresses outside the primary DHCP pool to ensure deterministic routing during cold boots and disaster recovery.

| Hostname | Role | IP Address | MAC Address |
| :--- | :--- | :--- | :--- |
| `pve-dell01` | Proxmox Host (Control Plane) | `192.168.1.40` | `TBD` |
| `pve-acer` | Proxmox Host (Heavy Worker) | `192.168.1.41` | `TBD` |
| `pve-dell02` | Proxmox Host (Secondary Worker) | `192.168.1.42` | `TBD` |
| `technitium-dns` | LXC Primary DNS/DHCP | `192.168.1.45` | `TBD` |
| `pangolin-client`| LXC Reverse Tunnel (Ingress) | `192.168.1.46` | `TBD` |
| `k8s-cp01` | Kubernetes Control Plane | `192.168.1.50` | `TBD` |
| `k8s-node01` | Kubernetes Worker 01 | `192.168.1.51` | `TBD` |
| `k8s-node02` | Kubernetes Worker 02 | `192.168.1.52` | `TBD` |

## Out-of-Band & Ingress Routing
*   **Public Ingress:** External traffic routes through a GCP Free Tier (`e2-micro`) instance running Pangolin, tunneling down via WireGuard into the Kubernetes `ingress-nginx` controller.
*   **Administrative Mesh:** Tailscale is installed directly on the bare-metal Proxmox hypervisors, bypassing the Kubernetes networking stack entirely.
*   **Mobile DNS:** The Tailscale administrative console is configured to use the Technitium LXC (`192.168.1.45`) as the global nameserver with "Override Local DNS" enabled, providing homelab ad-blocking to mobile devices on cellular networks.
