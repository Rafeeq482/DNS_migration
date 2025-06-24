provider "aws" {
  region = "us-east-1"
}

variable "domain_name" {
  description = "The domain name for the hosted zone"
  type        = string
}

variable "zone_id" {
  description = "Route53 Hosted Zone ID"
  type        = string
}

# No need for data lookup anymore
