terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "1.8.0"
    }
  }
}



provider "render" {
  api_key  = "rnd_jydqwMIJ2X1nqJJvGYxgI1qBMOSG"
  owner_id = "tea-d48rptogjchc73f28go0"
}

# Define Render Registry Credential for GitHub Container Registry (GHCR)

resource "render_registry_credential" "ghcr_credential" {
  name = "ghcr-credential"
  registry = "GITHUB"
  username = "ratanhalder888"
  # github personal access access auth_token
  auth_token = ""
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


}

resource "render_postgres" "Database1" {

    name = "ProductionDatabase1"
    plan = "free"       
    region = "oregon"      
    version = "16"

    database_name = ""
    database_user = ""

    high_availability_enabled = false  # Disabled high availability for simplicity

  }

