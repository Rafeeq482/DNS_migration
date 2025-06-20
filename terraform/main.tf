provider "aws" {
  region = "us-east-1" # any region; Route 53 is global
}

resource "aws_route53_zone" "new_zone" {
  name = var.domain_name
}

# Include all DNS records in records.tf
