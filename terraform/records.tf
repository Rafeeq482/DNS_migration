
resource "aws_route53_record" "a_@_devopsengg_xyz_0" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "@.devopsengg.xyz."
  type    = "A"
  ttl     = 300
  records = ["192.0.2.123"]
}

resource "aws_route53_record" "mx_@_devopsengg_xyz_1" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "@.devopsengg.xyz."
  type    = "MX"
  ttl     = 300
  records = ["10 mail.externalprovider.com."]
}

resource "aws_route53_record" "a_api_devopsengg_xyz_2" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "api.devopsengg.xyz."
  type    = "A"
  ttl     = 300
  records = ["192.0.2.124"]
}

resource "aws_route53_record" "cname_mail_devopsengg_xyz_3" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "mail.devopsengg.xyz."
  type    = "CNAME"
  ttl     = 300
  records = ["mail.externalprovider.com."]
}

resource "aws_route53_record" "cname_www_devopsengg_xyz_4" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "www.devopsengg.xyz."
  type    = "CNAME"
  ttl     = 300
  records = ["devopsengg.xyz."]
}