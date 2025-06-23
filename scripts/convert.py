import sys

def convert_to_tf(input_file, output_file):
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    tf_lines = []
    index = 0

    for line in lines:
        if line.startswith("$") or "SOA" in line:
            continue  # Skip $ORIGIN and SOA
        if "NS" in line and line.startswith("devopsengg.xyz."):
            continue  # Skip root NS records

        parts = line.strip().split()
        if len(parts) < 5:
            continue

        name, ttl, _, record_type, *values = parts
        value = " ".join(values).strip('"')
        value = value.replace('\\100', '@')  # decode any escaped @ symbol

        resource_name = f"{record_type.lower()}_{name.replace('.', '_').strip('_')}_{index}"

        tf_lines.append(f'''
resource "aws_route53_record" "{resource_name}" {{
  zone_id = aws_route53_zone.new_zone.zone_id
  name    = "{name}"
  type    = "{record_type}"
  ttl     = {ttl}
  records = ["{value}"]
}}''')
        index += 1

    with open(output_file, "w") as f:
        f.write("\n".join(tf_lines))

if __name__ == "__main__":
    convert_to_tf(sys.argv[1], sys.argv[2])
