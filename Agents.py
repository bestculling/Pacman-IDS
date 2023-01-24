import random
from game import Agent
from game import Directions

class DumbAgent(Agent):
    def getAction(self, state):
        
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP

class RandomAgent(Agent):
    def getAction(self, state):
        print(('Location: '), state.getPacmanPosition())
        listofactions = state.getLegalPacmanActions()[:]
        listofactions.remove(Directions.STOP)
        print(('Actions available:'), listofactions)
        action = random.choice(listofactions)
        print("Going" + action)
        return action

class ReflexAgent(Agent):
    def getAction(self, state):
        print(('Location:'), state.getPacmanPosition())
        listofactions = state.getLegalPacmanActions()[:]
        listofactions.remove(Directions.STOP)
        print(('Actions available:'), listofactions)
        num_food = state.getNumFood()
        for act in listofactions:
            if num_food > state.generatePacmanSuccessor(act).getNumFood():
                return act
        return random.choice(listofactions)