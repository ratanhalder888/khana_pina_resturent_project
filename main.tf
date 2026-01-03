terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "1.8.0"
    }
  }
}


variable "RENDER_API_KEY" {}
variable "RENDER_OWNER_ID" {}
variable "GHCR_USERNAME" {}
variable "GHCR_PAT" {}

variable "DATABASE_NAME" {}
variable "DATABASE_USER" {}

variable "SECRET_KEY" {}




provider "render" {
  api_key  = var.RENDER_API_KEY
  owner_id = var.RENDER_OWNER_ID
}

# Define Render Registry Credential for GitHub Container Registry (GHCR)

resource "render_registry_credential" "ghcr_credential" {
  name = "ghcr-credential"
  registry = "GITHUB"
  username = var.GHCR_USERNAME
  # github personal access access auth_token
  auth_token = var.GHCR_PAT
}

# Define the Render Web Service

resource "render_web_service" "WebApp1" {
  
  name   = "my-django-app"
  plan   = "starter"
  region = "oregon"

   runtime_source = {
    image = {
      image_url = "ghcr.io/ratanhalder888/app-image"
      tag = "latest"  
      registry_credential_id = render_registry_credential.ghcr_credential.id
    }
  }
  
  env_vars = {

    SECRET_KEY = {value = var.SECRET_KEY}

  }


}

resource "render_postgres" "Database1" {

    name = "ProductionDatabase1"
    plan = "free"       
    region = "oregon"      
    version = "18"

    database_name = var.DATABASE_NAME
    database_user = var.DATABASE_USER

    high_availability_enabled = false  # Disabled high availability for simplicity

  }

