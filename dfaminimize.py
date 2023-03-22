"""
CMSC 141 X Exercise 1
Name:   John Mickey Cabauatan
        Cedric Ramos
        Jianne Rimar Sison
Date: 27 March 2023
"""

from dfa import DFA

def dfa_strip(self):
    
    reachableStates = {self.start_state}
    newStates = {self.start_state}

    while newStates != {}:
        tempStates = {}
        for r in newStates:
            for symbol in self.alphabet:
                tempStates = tempStates | (str(self.transition[r][symbol]))
        newStates = tempStates.difference(reachableStates)
        reachableStates = reachableStates | newStates

    statePrime = reachableStates
    accept_statesPrime = self.accept_states & reachableStates
    transitionPrime = self.transition

    for (q, a) in set(itertools.product((self.states.difference(statePrime)), self.alphabet)):
        
    


