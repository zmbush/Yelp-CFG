import json

data = "tmplIDXQt"

dataset = open(data)

for obj in dataset:
    j = json.loads(obj)
#    print j
    text = j["text"]

    print text

def numStars(text):
    text = text.split()
    for word in text:
        print word

if __name__ == "__main__":
    pass
