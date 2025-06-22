import sys

def convert_to_tf(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    tf_lines = []
    domain = "devopsengg.xyz."
    index = 0

    for line in lines:
        if line.startswith("$") or "SOA" in line:
            continue

        parts = line.split()
        if len(parts) < 5:
            continue

        name, ttl, _, record_type = parts[:4]
        values = parts[4:]

        if record_type == "NS" and name.strip() == domain:
            continue

        resource_name = f"{record_type.lower()}_{name.replace('.', '_').strip('_')}_{index}"

        if record_type == "TXT":
            value_str = ', '.join([f'"{v.strip()}"' for v in values])
        elif record_type == "MX":
            value_str = ', '.join([f'"{values[0]} {values[1]}"'])
        else:
            value_str = ', '.join([f'"{v.strip()}"' for v in values])

        tf_lines.append(f'''
resource "aws_route53_record" "{resource_name}" {{
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "{name}"
  type    = "{record_type}"
  ttl     = {ttl}
  records = [{value_str}]
}}
''')
        index += 1

    with open(output_file, "w") as f:
        f.writelines(tf_lines)

if __name__ == "__main__":
    convert_to_tf(sys.argv[1], sys.argv[2])