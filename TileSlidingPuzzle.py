
from ctypes import sizeof
import queue
import time
import random
start = time.time()

StateDimension=4
# StateDimension=3
# GoalState = '123456780'
GoalState = "123456789ABCDEF0"
Actions = lambda s: ['u', 'd', 'l', 'r']
Opposite=dict([('u','d'),('d','u'),('l','r'),('r','l'), (None, None)])

class Node:
  def __init__(self,InitialState,action,parent=None):
    self.state = InitialState
    self.action = action
    self.parent = parent



def Result(state, action):
  i = state.index('0')
  newState = list(state)
  row,col=i//StateDimension, i % StateDimension
  if ( (action=='u' and row==0) or
       (action=='d' and row==StateDimension-1) or
       (action=='l' and col==0) or
       (action=='r' and col==StateDimension-1)):
      return ''.join(newState)
  if action=='u':
    l,r = row*StateDimension+col, (row-1)*StateDimension+col
  elif action=='d':
    l,r = row*StateDimension+col, (row+1)*StateDimension+col
  elif action=='l':
    l,r = row*StateDimension+col, row*StateDimension+col-1
  elif action=='r' :
    l,r = row*StateDimension+col, row*StateDimension+col+1
  newState[l], newState[r] = newState[r], newState[l] 
  return ''.join(newState)


initialStates = ['213807456','735102648','843251670']
def BreadthFirstSearch(GoalState):
  InitialState = '237416B8590CDAEF'

  print(InitialState)
  node = Node(InitialState,'',None)
  global expandedNodes
  expandedNodes = 0
  if GoalState == node.state: 
    return node
#FIFO
  frontier = queue.Queue()
  frontier.put(node)
  reached = {node.state}
  while not frontier.empty():
    expandedNodes += 1
    # print(expandedNodes)
    newNode = frontier.get()
    for child in Expand(newNode):
        if GoalState == child.state:
            print('Success')
            return child
        if child.state not in reached:
            reached.add(child.state)
            frontier.put(child)
  return False
    
    
def Expand(newNode):
    newStates = []
    for action in ['u','d','l','r']:
        s1 = Result(newNode.state,action)
        newStates.append(Node(s1,action,newNode))
    return newStates
        
successNode = BreadthFirstSearch(GoalState)
moveString = successNode.action

while successNode.parent is not None:
  successNode = successNode.parent
  moveString = successNode.action + moveString

print(moveString)
print(expandedNodes)
def LegalMove(state, action):
  i = state.index('0')
  row,col=i//StateDimension, i % StateDimension
  if ( (action=='u' and row==0) or
       (action=='d' and row==StateDimension-1) or
       (action=='l' and col==0) or
       (action=='r' and col==StateDimension-1)):
      return False
  return True
def RandomWalk(state, steps):
  actionSequence = []
  actionLast = None
  for i in range(steps):
    action = None
    while action==None:
      action = random.choice(Actions(state))
      action = action if (LegalMove(state, action) 
          and action!= Opposite[actionLast]) else None
    actionLast = action
    state = Result(state, action)
    actionSequence.append(action)
  return state, actionSequence


result4x4, solution = RandomWalk(GoalState,35)
print(result4x4,solution)

end = time.time()
print(f"Runtime of the program is {end - start}")