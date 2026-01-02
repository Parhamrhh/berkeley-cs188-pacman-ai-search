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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    fringe = util.Stack()  # initialize the fringe as a stack
    initialState = (problem.getStartState(), 0, [])  # (node, cost, path)
    fringe.push(initialState)  # push the start state onto the stack
    explored = set()  # tracking visited nodes

    while not fringe.isEmpty():
        current, cost, path = fringe.pop()  # pop the most recent state

        if problem.isGoalState(current):  # if it's the goal state, return the path
            return path

        if current not in explored:# only expand unvisited states
            explored.add(current)  # mark current as visited

            for child, action, step_cost in problem.expand(current):  # expand children
                new_cost = cost + step_cost  # calculate new cost
                new_path = path + [action]  # extend path
                new_node = (child, new_cost, new_path)  # create new node tuple
                fringe.push(new_node)  # push the new node onto the stack

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()  # initialize fringe as a FIFO queue
    initialState = (problem.getStartState(), 0, [])  # (node, cost, path)
    fringe.push(initialState)  # push the start state onto the queue
    explored = set()  # tracking visited nodes

    while not fringe.isEmpty():
        current, cost, path = fringe.pop()  # pop the oldest state from queue

        if problem.isGoalState(current):  # if it's the goal state, return the path
            return path

        if current not in explored:  # only expand unvisited states
            explored.add(current)  # mark current as visited

            for child, action, step_cost in problem.expand(current):  # expand children
                new_cost = cost + step_cost  # calculate new cost
                new_path = path + [action]  # extend path
                new_node = (child, new_cost, new_path)  # create new node tuple
                fringe.push(new_node)  # add to queue

    return []

def uniformCostSearch(problem):
    """Search the node of the least total cost first."""
    fringe = util.PriorityQueue()  # initialize fringe as a priorityy queue
    initialState = (problem.getStartState(), 0, [])  # (node, cost, path)
    fringe.push(initialState, 0)  # add to fringe with priority 0
    explored = set()  # tracking visited nodes

    while not fringe.isEmpty():
        current, cost, path = fringe.pop()  # pop node with the lowest total cost

        if problem.isGoalState(current):  # if it's the goal state, return the path
            return path

        if current not in explored:
            explored.add(current)  # mark current as visited

            for child, action, step_cost in problem.expand(current):  # expand children
                new_cost = cost + step_cost  # calculate new cost
                new_path = path + [action]  # extend path
                new_node = (child, new_cost, new_path)  # create new node tuple
                fringe.update(new_node, new_cost)  # update or add to fringe with cost as priority

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def greedySearch(problem, heuristic=nullHeuristic):
    """
    Search the node that appears to be closest to the goal
    according to the heuristic function.
    """
    fringe = util.PriorityQueue()  # initialize fringe as a priorityy queue
    startState = problem.getStartState()
    initialState = (startState, 0, [])  # (state, cost, path)
    priority = heuristic(startState, problem)  # f(n) = h(n)
    fringe.push(initialState, priority)  # push the start state onto the queue with priority
    explored = set()  # tracking visited states

    while not fringe.isEmpty():
        current, cost, path = fringe.pop()  # pop node with the smallest f(n)

        if problem.isGoalState(current):  # if it's the goal state, return the path
            return path

        if current not in explored:
            explored.add(current)  # mark current as visited

            for child, action, step_cost in problem.expand(current):  # expand children
                new_cost = cost + step_cost  # calculate new cost
                new_path = path + [action]  # extend path
                new_node = (child, new_cost, new_path) # create new node tuple
                priority = heuristic(child, problem)  # use heuristic for priority
                fringe.update(new_node, priority) # update or add to fringe with heuristic as priority

    return []

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue() # initialize fringe as a priorityy queue
    startState = problem.getStartState()
    initialState = (startState, 0, [])  # (state, cost, path)
    priority = 0 + heuristic(startState, problem)  # f(n) = g(n) + h(n)
    fringe.push(initialState, priority)  # push the start state onto the queue with priority
    explored = set()  # tracking visited states

    while not fringe.isEmpty():
        current, cost, path = fringe.pop()  # pop node with the smallest f(n)

        if problem.isGoalState(current):  # if it's the goal state, return the path
            return path

        if current not in explored:
            explored.add(current)  # mark current as visited

            for child, action, step_cost in problem.expand(current):  # expand children
                new_cost = cost + step_cost  # calculate g(n)
                new_path = path + [action]  # extend path
                new_node = (child, new_cost, new_path) # create new node tuple
                priority = new_cost + heuristic(child, problem)  # f(n) = g(n) + h(n)
                fringe.update(new_node, priority) # update or add to fringe with f(n) as priority

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
gs = greedySearch
astar = aStarSearch
