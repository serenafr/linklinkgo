import boards
  
def GetInput(prompt):
  while True:
    try:
      n = int(raw_input(prompt))
      break
    except ValueError as e:
      print "Wrong input: %s" % e
  return n

board = boards.Board(kinds=5, interval=3, pairsPerKind=2)

while board.Size() > 0:
  while board.NeedShuffle():
    board.Shuffle()
    print 'Shuffle!'
  board.Print()
  n1 = GetInput('Please enter the first number: ')
  n2 = GetInput('Please enter the second number: ')    
  try:
    board.ManualErase(n1, n2)
  except RuntimeError as e:
    print e
