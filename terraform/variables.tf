variable "resource_group_name" {
    type    = string
    default = "rg-bpp-devops"
    description = "name of resource group"
}

variable "location" {
    type    =string
    default = "uksouth"
    description = "location set"
}

variable "cluster_name"{
    type = string
    default = "aks-bpp-devops"
    description = "name of cluster"

}

variable "node_count"{
    
    default = 1
    description = "number of nodes"
}

variable "vm_size"{
    default = "Standard_D2pls_v6"
    description = "aks vm size"
}

variable "environment" {
  type        = string
  default     = "prod"
  description = "deployment environment"
}