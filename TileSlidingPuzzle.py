
from ctypes import sizeof
import queue

# StateDimension=3
StateDimension=4
# InitialState = '123456708'
#InitialState = '218764053'
GoalState = '123456780'

# GoalState = "123456789ABCDEF0"
Actions = lambda s: ['u', 'd', 'l', 'r']


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


def BreadthFirstSearch(GoalState):
  InitialState = '16235A749C08DEBF'
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