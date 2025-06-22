import sys

def convert_to_tf(input_file, output_file):
    with open(input_file, "r", encoding="utf-16") as f:
        lines = f.readlines()

    tf_lines = []
    index = 0

    for line in lines:
        line = line.strip().replace("\x00", "")
        if not line or line.startswith("$") or "SOA" in line:
            continue  # skip empty, $ORIGIN and SOA lines
        if "NS" in line:
            parts = line.split()
            if len(parts) >= 5:
                name, ttl, _, record_type, value = parts[:5]
                resource_name = f"ns_{name.replace('.', '_').strip('_')}_{index}"
                tf_lines.append(f'''
resource "aws_route53_record" "{resource_name}" {{
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "{name}"
  type    = "{record_type}"
  ttl     = {ttl}
  records = ["{value}"]
}}
''')
                index += 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(tf_lines)

if __name__ == "__main__":
    convert_to_tf(sys.argv[1], sys.argv[2])
