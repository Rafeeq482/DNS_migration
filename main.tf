provider "aws" {
  region = "ap-south-1"
}

resource "aws_route53_zone" "new_zone" {
  name = "devopsengg.xyz"
}

# Include converted records here or in `records.tf`
