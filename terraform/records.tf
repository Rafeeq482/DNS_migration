resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "www.${var.domain_name}"
  type    = "A"
  ttl     = 300
  records = ["1.2.3.4"]
}

resource "aws_route53_record" "mail" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "mail.${var.domain_name}"
  type    = "CNAME"
  ttl     = 300
  records = ["mail.externalprovider.com"]
}
