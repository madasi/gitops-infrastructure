resource "proxmox_virtual_environment_container" "technitium_dns" {
  description   = "Technitium DNS Server - Managed by OpenTofu"
  node_name     = "pve-dell01"
  vm_id         = 153
  unprivileged  = true
  start_on_boot = true

  features {
    nesting = true
  }

  initialization {
    hostname = "dns-primary"

    ip_config {
      ipv4 {
        address = "192.168.1.53/24"
        gateway = "192.168.1.254"
      }
    }

    user_account {
      keys = [
        trimspace(file(pathexpand("~/.ssh/id_homelab.pub")))
      ]
    }
  }

  cpu {
    cores = 1
  }

  memory {
    dedicated = 512
  }

  disk {
    datastore_id = "local-lvm"
    size         = 8
  }

  network_interface {
    name   = "eth0"
    bridge = "vmbr0"
  }

  operating_system {
    # We will update this exact filename dynamically below
    template_file_id = "local:vztmpl/debian-12-standard_12.12-1_amd64.tar.zst"
    type             = "debian"
  }
}
