provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "fastapi_app" {
  metadata {
    name = "fastapi-app"
    labels = {
      app = "fastapi"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "fastapi"
      }
    }

    template {
      metadata {
        labels = {
          app = "fastapi"
        }
      }

      spec {
        container {
          image = "myusername/my-fastapi-app:latest"
          name  = "fastapi-container"

          port {
            container_port = 80
          }

          env {
            name  = "DATABASE_URL"
            value = var.database_url
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "fastapi_service" {
  metadata {
    name = "fastapi-service"
  }

  spec {
    selector = {
      app = "fastapi"
    }

    port {
      port = 80
      target_port = 80
    }

    type = "LoadBalancer"
  }
}
