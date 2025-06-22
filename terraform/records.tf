
resource "aws_route53_record" "ns_devopsengg_xyz_0" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "devopsengg.xyz."
  type    = "NS"
  ttl     = 172800
  records = ["ns-1454.awsdns-53.org."]
}

resource "aws_route53_record" "ns_devopsengg_xyz_1" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "devopsengg.xyz."
  type    = "NS"
  ttl     = 172800
  records = ["ns-1657.awsdns-15.co.uk."]
}

resource "aws_route53_record" "ns_devopsengg_xyz_2" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "devopsengg.xyz."
  type    = "NS"
  ttl     = 172800
  records = ["ns-65.awsdns-08.com."]
}

resource "aws_route53_record" "ns_devopsengg_xyz_3" {
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "devopsengg.xyz."
  type    = "NS"
  ttl     = 172800
  records = ["ns-693.awsdns-22.net."]
}
