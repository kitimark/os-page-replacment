import algorithm as alg
import matplotlib.pyplot as plt
from random import randrange

def visualize_alg(number, randRange, step, frame):
  dataList = [randrange(randRange) for _ in range(number)]
  steps = list(range(0, number, step))
  
  fifoResult = []
  optimalResult = []
  lruResult = []

  for step in steps:
    fifoResult.append(alg.FIFO(dataList[:step], frame))
    optimalResult.append(alg.Optimal(dataList[:step], frame))
    lruResult.append(alg.LRU(dataList[:step], frame))

  plt.plot(steps, fifoResult)
  plt.plot(steps, optimalResult)
  plt.plot(steps, lruResult)
  plt.legend(['FIFO', 'Optimal', 'LRU'])
  plt.ylabel('page faults')
  plt.xlabel('number of steps')
  plt.show()
