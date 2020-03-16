import algorithm as alg
import visualize as vis

if __name__ == "__main__":
  dataList = [0, 1, 7, 2, 3, 2, 7, 1, 0, 3]
  print(alg.FIFO(dataList, 4))
  print(alg.Optimal(dataList, 4))
  print(alg.LRU(dataList, 4))
  vis.visualize_alg(100, 10, 5, 4)
