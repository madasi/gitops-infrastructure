terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "~> 0.69.0"
    }
    sops = {
      source  = "carlpett/sops"
      version = "~> 1.1.1"
    }
  }
}

# Initialize the SOPS provider
provider "sops" {}

# Read the encrypted variables file from the Ansible directory
data "sops_file" "secrets" {
  source_file = "../../ansible/group_vars/all/secrets.sops.yaml"
}

# Configure the Proxmox provider using the decrypted SOPS data
provider "proxmox" {
  endpoint  = "https://192.168.1.40:8006/"
  api_token = "${data.sops_file.secrets.data["pve_dell01_api_token_id"]}=${data.sops_file.secrets.data["pve_dell01_api_token_secret"]}"
  insecure  = true # Required because the Proxmox default cert is self-signed

  ssh {
    agent    = true
    username = "ansible"
  }
}
