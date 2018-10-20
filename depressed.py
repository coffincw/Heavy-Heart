"""
before running, set the map of the grouped reviews to their respective dictionaries.
"""
from math import log


def is_depressed(review):
  if(is_depressed.counter==0):#define probabilities
      is_depressed.lenP = 0
      is_depressed.lenN = 0
      is_depressed.countMapD = {}#depressed revieww 
      is_depressed.countMapC = {}#Control review
      print("defining probabilities, this will take a while")
      for depressedReview in train_depressed:
          for word in depressedReview:
              is_depressed.lenP+=1
              if(is_depressed.countMapD.__contains__(word)):
                  tempDic = {word: is_depressed.countMapD.get(word) + 1}
                  is_depressed.countMapD.update(tempDic)
              else:
                  is_depressed.countMapD.update({word: 1})
      for controlReview in train_control:
          for word in controlReview:
              is_depressed.lenN+=1
              if (is_depressed.countMapC.__contains__(word)):
                  tempDic = {word: is_depressed.countMapC.get(word) + 1}
                  is_depressed.countMapC.update(tempDic)
              else:
                  is_depressed.countMapC.update({word: 1})
  is_depressed.counter+=1
  logProductP = 0
  logProductN = 0
  probPos = float(is_depressed.lenP)/float(is_depressed.lenP+is_depressed.lenN)
  probNeg = float(is_depressed.lenN)/float(is_depressed.lenP+is_depressed.lenN)
  for word in review:
      logProductN += math.log(float(is_depressed.countMapC.get(word,1)))
      logProductP += math.log(float(is_depressed.countMapD.get(word,1)))
  return logProductP-math.log(float(is_depressed.lenP))>logProductN-math.log(float(is_depressed.lenN))

is_depressed.counter = 0
is_depressed.lenP = 0
is_depressed.lenN = 0
is_depressed.countMapD = {}
is_depressed.countMapC = {}