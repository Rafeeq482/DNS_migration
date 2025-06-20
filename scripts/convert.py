import sys

def convert_to_tf(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    tf_lines = []

    for line in lines:
        if line.startswith("$") or "SOA" in line:
            continue  # skip ORIGIN and SOA
        if "NS" in line:
            name, ttl, _, record_type, value = line.split()
            tf_lines.append(f'''
resource "aws_route53_record" "ns_{name.replace(".", "_")}" {{
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "{name}"
  type    = "{record_type}"
  ttl     = {ttl}
  records = ["{value}"]
}}
''')

    with open(output_file, "w") as f:
        f.writelines(tf_lines)

if __name__ == "__main__":
    convert_to_tf(sys.argv[1], sys.argv[2])
