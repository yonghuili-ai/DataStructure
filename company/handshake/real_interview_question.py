from abc import ABC, abstractmethod
from collections import defaultdict
 
class Mapper(ABC):
  def _map(self, data_part):
    pass
 
class Reducer(ABC):
  def _reduce(self, kvs):
    pass
 
class MapReduce(Mapper, Reducer):
  def __init__(self, mapper, reducer):
    self.mapper= mapper()
    self.reducer= reducer()
 
  def runMR(self, data_parts):
    storage = defaultdict(list)
    for data_part in data_parts:
      for key, value in self.mapper._map(data_part).items():
        storage[key].append(value)
    return self.reducer._reduce(storage)
 
#####################################################################
 
data = [ "Handshake lets universities and employers connect with a single click",
         "leading to more diverse, high-quality networking opportunities for students",
         "and employers. Because Handshake now connects over 300,000 unique employers",
         "from every industry and region, most schools see a 2-3x increase in relevant",
         "job opportunities within the first 6 months of switching to Handshake"
       ]
from collections import defaultdict
class WCMapper(Mapper):
  def _map(self, data_part):
    # TODO: mapper code here
    d = defaultdict(int)
    # list_data = data.split(',')
    word_data = data_part.split(" ")
    # word_data = []
    # for sen in list_data:
    #     word_data.extend(sen.split(' '))
    #     print(word_data)
    for word in word_data:
        d[word] += 1
    # print(d)
    return d
 
 
class WCReducer(Reducer):
  def _reduce(self, kvs):
    # TODO: reducer code here
    h = defaultdict(int)
    for k, v in kvs.items():
        total_cnt = 0
        for cnt in v:
            total_cnt += cnt
        h[k] = total_cnt
    return h

 
for x in MapReduce(WCMapper, WCReducer).runMR(data):
  print("'{}': {}".format(x[0], x[1]))