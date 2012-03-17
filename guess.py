import json

train = json.loads(open('trained.json').read())

test = open('test_reviews.json')

bus = open('business.json')

businesses = {}

for b in bus:
  obj = json.loads(b)
  bid = obj['business_id']
  ave = float(obj['stars'])
  votes = float(obj['review_count'])
  businesses[bid] = (ave, votes)

for t in test:
  obj = json.loads(t)
  output = {'review_id' : obj['review_id']}

  contents = obj['text']

  guessStars = 0
  dataPoints = 0
  if obj['business_id'] in businesses:
    guessStars = businesses[obj['business_id']][0]
    dataPoints = businesses[obj['business_id']][1]*100
  else:
    guessStars = 3.0
    dataPoints = 100

  for word in contents.split():
    sanitized = ''.join(e for e in word if e.isalnum()).lower()

    if sanitized in train:
      bigStars = guessStars*dataPoints

      weight,stars = train[sanitized]

      dataPoints += weight
      bigStars += stars*weight

      guessStars = bigStars / dataPoints
  output['stars'] = guessStars

  print json.dumps(output)
