import sys

def convert_to_tf(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    tf_lines = []

    domain = "devopsengg.xyz."  # root domain to exclude from NS records
    index = 0

    for line in lines:
        if line.startswith("$") or "SOA" in line:
            continue  # skip $ORIGIN and SOA lines

        if "NS" in line:
            parts = line.split()
            if len(parts) != 5:
                continue  # skip malformed lines

            name, ttl, _, record_type, value = parts

            if name.strip() == domain:
                continue  # skip root NS record

            resource_name = f"ns_{name.replace('.', '_').strip('_')}_{index}"
            tf_lines.append(f'''
resource "aws_route53_record" "{resource_name}" {{
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "{name.strip()}"
  type    = "{record_type.strip()}"
  ttl     = {ttl.strip()}
  records = ["{value.strip()}"]
}}
''')
            index += 1

    with open(output_file, "w") as f:
        f.writelines(tf_lines)

if __name__ == "__main__":
    convert_to_tf(sys.argv[1], sys.argv[2])
