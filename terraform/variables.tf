variable "resource_group_name" {
    type    = string
    default = "rg-bpp-devops"
}

variable "location" {
    type    =string
    default = "uksouth"
}

variable "cluster_name"{
    type = string
    default = "aks-bpp-devops"

}

variable "node_count"{
    default = 1
}

variable "vm_size"{
    default = "Standard_D2pls_v6"
}