import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
j = 0
with open(input_file, 'r') as f:
  for line in f.readlines():
    gene_name = re.search(r'gene_name\s(\S+)',line)
    gene_id = gene_name.group(1)
    match = re.search(r'(\w+);(\w+)', gene_id)
    if match:
      newid = ''.join(['"', match.group(1), match.group(2), '"', ';'])
      newline = line.replace(gene_id, newid)
    else:
      newline = line

    with open(output_file, 'a') as newf:
      newf.write(newline)
      j += 1

print 'totaly', j, 'number of lines modified!'
