provider "aws" {
  region = "us-east-1"
}

resource "aws_route53_zone" "new_zone" {
  name    = var.domain_name
  comment = "Migrated via Terraform"
}