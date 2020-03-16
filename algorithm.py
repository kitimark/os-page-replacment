from operator import itemgetter

def FIFO(dataList: list, frame: int) -> int:
  """First in, First out"""
  pageFaults = 0
  frameList = [None] * frame
  pointFrameList = 0

  for data in dataList:
    if not frameList.count(data):
      frameList[pointFrameList] = data
      pageFaults += 1
      pointFrameList = (pointFrameList + 1) % frame

  return pageFaults


def _index(dataList: list, value, start:int=None) -> int:
  """return index of value otherwise return None"""
  try:
    if start:
      return dataList.index(value, start)
    else:
      return dataList.index(value)
  except ValueError:
    return None


def Optimal(dataList: list, frame: int) -> int:
  """Optimal (MIN)"""
     
  pageFaults = 0
  frameList = [None] * frame
  nextIndexEachFrame = [None] * frame

  for idx, data in enumerate(dataList):
    if not frameList.count(data):
      frameIdx = _index(frameList, None)
      if frameIdx is None:
        frameIdx = _index(nextIndexEachFrame, None)
      if frameIdx is None:
        # frame_idx, _ = max(enumerate(nextIndexEachFrame), key=itemgetter(1))
        candidate = list(map(lambda x, i: (i, x) if x < idx else (i, None), 
                         nextIndexEachFrame, 
                         range(len(nextIndexEachFrame))))
        candidate = list(filter(lambda x: x[1] is not None, candidate))
        if candidate:
          frameIdx, _ = max(enumerate(candidate), key=itemgetter(1))
        else:
          frameIdx, _ = max(enumerate(nextIndexEachFrame), key=itemgetter(1))
        pass

      frameList[frameIdx] = data
      nextIndexEachFrame[frameIdx] = _index(dataList, data, idx + 1)

      pageFaults += 1

  return pageFaults


def LRU(dataList:list, frame:int) -> int:
  """Least Recently Used"""
  pageFaults = 0
  frameList = [None] * frame
  callFrameList = [None] * frame

  for idx, data in enumerate(dataList):
    if not frameList.count(data):
      frameIdx = _index(frameList, None)
      if frameIdx is None:
        frameIdx, _ = min(enumerate(callFrameList), key=itemgetter(1))

      frameList[frameIdx] = data
      callFrameList[frameIdx] = idx

      pageFaults += 1
    else:
      # update callFrameList
      frameIdx = frameList.index(data)
      callFrameList[frameIdx] = idx
  
  return pageFaults
