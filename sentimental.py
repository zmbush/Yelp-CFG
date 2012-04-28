#!/usr/bin/env python

import json

reviews = 'review.json'

data = open(reviews)

words = {}

for review in data:
  obj = json.loads(review)

  contents = obj['text']
  stars = float(obj['stars'])
  for word in contents.split():
    sanitized = ''.join(e for e in word if e.isalnum()).lower()
    if len(sanitized) > 3 and len(sanitized) < 15:  
      if sanitized not in words:
        words[sanitized] = (1, stars)
      else:
        count,s = words[sanitized]

        times = s*count + stars

        count += 1
        words[sanitized] = (count, times / count)

commonWords = {}
delta = .85
for word in words:
  if words[word][0] > 10:
    if words[word][1] < 3 - delta or words[word][1] > 3 + delta:
      commonWords[word] = words[word]

trained = open('trained.json', 'w')
trained.write(json.dumps(commonWords))
