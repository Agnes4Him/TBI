terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "my-terraform-state-bucket"     
    key            = "envs/production/terraform.tfstate"   
    region         = "us-east-1"                     
    dynamodb_table = "terraform-locks"              
    encrypt        = true
  }
}


provider "aws" {
  region = var.region
}