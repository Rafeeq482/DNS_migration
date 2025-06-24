provider "aws" {
  region = "us-east-1"
}

data "aws_route53_zone" "existing_zone" {
  name         = "${var.domain_name}."
  private_zone = false
}

