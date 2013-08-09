import random

class Board(object):
  def __init__(self, kinds, pairsPerKind, interval):
    self.interval = interval
    self.kinds = kinds
    self.pairsPerKind = pairsPerKind
    self.tiles = None
    self.GenTiles()

  def GenTiles(self):
    'generate a new game'
    self.tiles = []
    for i in xrange(self.kinds):
      self.tiles.extend([i] * self.pairsPerKind * 2)
    self.Shuffle()
    
  def Shuffle(self):
    random.shuffle(self.tiles)
    
  def Size(self):
    return len(self.tiles)

  def Find(self):
    '''find two tiles that are the same with each other
    if not found, return two -1'''
    for i in xrange(self.Size() - 1):
      for j in xrange(i + 1, min(self.Size(), i + self.interval)):
        if self.tiles[i] == self.tiles[j]:
          return i, j
    return -1, -1
    
  def NeedShuffle(self):
    'return True if the board needs shuffle'
    return self.Find() == (-1, -1)
    
  def GetTile(self, pos):
    return self.tiles[pos]

  def CanErase(self, pos1, pos2):
    'return True if can erase, otherwise return False'
    if pos1 >= self.Size() or pos2 >= self.Size() or pos1 < 0 or pos2 < 0:
      return False
    return 0 < abs(pos1 - pos2) < self.interval and \
        self.GetTile(pos1) == self.GetTile(pos2)

  def ManualErase(self, num1, num2):
    '''Erase 2 tiles mannually
       Raise a RuntinmeError if pic[num1] and pic[num2] cannot be erased
    '''
    if self.CanErase(num1, num2):
      self.tiles.pop(min(num1, num2))
      self.tiles.pop(max(num2, num1) - 1)
    else:
      raise RuntimeError('Not match!')

  def Print(self):
    'Print board'
    print PrettyPrint(self.tiles)
    print PrettyPrint(range(self.Size()))


def PrettyPrint(pic):
  'Arrange the list as if each element takes two space, return a string list'
  pic1 = []
  for i in pic:
    pic1.append(str(i).rjust(2))
  return ' '.join(pic1)  
