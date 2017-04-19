# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    "*** YOUR CODE HERE ***"

    frontier = util.Stack()
    closedList = []
    ## defined a stack to stored (node,path)
    ## defined a list to store the explored node

    if problem.isGoalState(problem.getStartState()):
        return "It is goal state now"
    ## check if the start node is the goal state
    else :
        frontier.push((problem.getStartState(),[]))
    ## if it's not, then wen can push the start node in the stack

        while frontier.isEmpty() == False:
            processingNode = frontier.pop()
    ## pop the last one node from the stack
    ## in the next code,'Anything[0]' means coordinate of the node we are processing
    ## 'Anything[1]' means the path we store in that state.

            if problem.isGoalState(processingNode[0]):
                return processingNode[1]

        ## so, if the node we pop is the goal, we return the path to this node
            if processingNode[0] not in closedList:
                closedList.append(processingNode[0])
                for succ in problem.getSuccessors(processingNode[0]):
                    if succ[0] not in closedList:
        ##for each successors of the node we pop, we use a subPath to store the path we get to that successors
                        subPath = list(processingNode[1])
                        subPath.append(succ[1])
                        frontier.push((succ[0], subPath))
        ## finally, we push the node and the path we get this node


        ##util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ## BFS is quite like DFS, just in BFS, we will use queue to store the coordinate and path
    frontier = util.Queue()
    closedList = []

    if problem.isGoalState(problem.getStartState()):
        return "It is goal state now"
    else:
        frontier.push((problem.getStartState(), []))

        while frontier.isEmpty() == False :
            processingNode = frontier.pop()

            if problem.isGoalState(processingNode[0]):
                print processingNode[1]
                return processingNode[1]

            if processingNode[0] not in closedList:
                closedList.append(processingNode[0])
                for succ in  problem.getSuccessors(processingNode[0]):
                    if succ[0] not in closedList:
                        subPath = list(processingNode[1])
                        subPath.append(succ[1])
                        frontier.push((succ[0],subPath))

    ##util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ## to the Uniform Cost Search, we use priority queue
    frontier = util.PriorityQueue()
    closedList = []

    if problem.isGoalState(problem.getStartState()):
        return "It is goal state now"
    else:
        frontier.push((problem.getStartState(),[]),0)
        ## in the uniform cost search, we need use cost to measure the priority

        while frontier.isEmpty() == False:
            processingNode = frontier.pop()

            if problem.isGoalState(processingNode[0]):
                return processingNode[1]

            if processingNode[0] not in closedList:
                closedList.append(processingNode[0])
                for succ in problem.getSuccessors(processingNode[0]):
                    if succ[0] not in closedList:
                        subPath = list(processingNode[1])
                        subPath.append(succ[1])
                        cost = problem.getCostOfActions(subPath)
                ## 'cost' is the cost of action we get to the succ[0]
                ## it also equal to the previous total cost(processingNode[2]) + the cost of this successor(succ[2]).
                        frontier.push((succ[0], subPath),cost)

    ##util.raiseNotDefined()
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    closedList = []

    if problem.isGoalState(problem.getStartState()):
        return "It is goal state now"
    else:
        frontier.push((problem.getStartState(), []), 0)

        while frontier.isEmpty() == False:
            processingNode = frontier.pop()

            if problem.isGoalState(processingNode[0]):
                return processingNode[1]

            if processingNode[0] not in closedList:
                closedList.append(processingNode[0])
                for succ in problem.getSuccessors(processingNode[0]):
                    if succ[0] not in closedList:
                        subPath = list(processingNode[1])
                        subPath.append(succ[1])
                        cost = problem.getCostOfActions(subPath) + heuristic(succ[0],problem)
        ## different from the uniform cost search, the cost in AStar search is f(s)= g(s) + h(s)
                        frontier.push((succ[0], subPath), cost)
    ##util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


