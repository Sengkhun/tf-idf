import math

def find_tf_idf(line):
  value = line.rstrip("\n\r").split(',')
  keyword = value[0]

  idf = find_idf(value[1:])

  print('{:10} '.format(keyword), end='')
  for x in value[1:]:
    tf = find_tf(x)
    tf_idf = tf * idf
    if tf_idf > 0:
      print('{:.2f}  '.format(tf_idf), end='')
    else:
      print('{:6}'.format(''), end='')
  print()

def find_tf(d):
  int_d = int(d)  # casting
  return 1 + math.log2(int_d) if int_d > 0 else 0

def find_idf(d):
  N = len(d)
  ni = 0
  for x in d:
    if int(x) > 0:
      ni += 1
  return math.log2(N/ni)

f = open("data.txt", "r")
data = f.readlines()

print('\n===Document Matrix===')
for line in data:
  find_tf_idf(line)
print()
