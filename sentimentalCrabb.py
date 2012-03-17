#!/usr/bin/env python

import json

reviews = 'review.json'
userfile = 'user.json'
busifile = 'business.json'

data = open(reviews)

users = {}
def getUsers(userdata):
    for line in userdata:
        user = json.loads(line)
        iden = user['user_id']
        avg = user['average_stars']
        if iden not in users:
            users[iden] = avg
        else:
            print "DUPLICATE"
    print users

busis = {}
def getUsers(busidata):
    for line in busidata:
        busi = json.loads(line)
        iden = busi['business_id']
        avg = busi['stars']
        if iden not in users:
            busis[iden] = avg
        else:
            print "DUPLICATE"
    print busis

words = {}
def zachStuff():
    for review in data:
      obj = json.loads(review)

      contents = obj['text']
      stars = float(obj['stars'])

      userid = obj['user_id']
      useravg = float(users[userid])
      
      diff = stars - useravg #higher than average = +
      diff /= 5

      wc = 0
      for word in contents.split():
        wc += 1
      weight = 1/wc
      for word in contents.split():
        sanitized = ''.join(e for e in word if e.isalnum()).lower()
        if len(sanitized) > 3 and len(sanitized) < 15:  
          if sanitized not in words:
            words[sanitized] = (1, stars)
          else:
            count,s = words[sanitized]

            nbs = s*count + diff/wc
            nw = s + count
            ns = nbw
            words[sanatized] = (nw, ns)

            #times = s*count + stars

            count += 1
            words[sanitized] = (count, times / count)



      for word in words:
          w = 1 / wc
          c,s = words[word]
          newScore = s * c + diff/wc
          newweight = s + c
          words[word] = (c,s)

    commonWords = {}
    for word in words:
      if words[word][0] > 10:
        commonWords[word] = words[word]

    trained = open('trained.json', 'w')
    trained.write(json.dumps(commonWords))


if __name__ == "__main__":
    getUsers(open(userfile))
    getBusis(open(busifile))
    zachStuff()
