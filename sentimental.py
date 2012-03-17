import json

data = 'yelp_academic_dataset.json'

dataset = open(data)

lines = 0

types = {}
for line in dataset:
  reviewData = json.loads(line)
  t = reviewData['type']
  if t not in types:
    types[t] = []
  types[t].append(reviewData)

for t in types:
  fname = t + '.json'
  handle = open(fname, 'w')
  for line in types[t]:
    handle.write(json.dumps(line) + '\n')
  handle.close()
