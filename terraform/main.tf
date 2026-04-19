resource "azurerm_resource_group" "rg"{
    name = var.resource_group_name
    location = var.location
}

resource "azurerm_kubernetes_cluster" "aks"{
    name = var.cluster_name
    location = var.location
    resource_group_name = var.resource_group_name
    dns_prefix = "${var.cluster_name}-dns"

    default_node_pool {
        name = "default"
        node_count = var.node_count
        vm_size = var.vm_size
    }
    identity {
        type = "SystemAssigned"
    }
    tags = {
        environment = "dev"
        project = "bpp-devops"
    }
}