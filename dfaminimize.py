"""
CMSC 141 X Exercise 1
Name:   John Mickey Cabauatan
        Cedric Ramos
        Jianne Rimar Sison
Date: 27 March 2023
"""

from dfa import DFA
import itertools

def dfa_strip(self):
    
    reachableStates = {self.start_state}
    newStates = {self.start_state}

    while newStates != {}:
        tempStates = {}
        for state in newStates:
            for symbol in self.alphabet:
                tempStates = tempStates | str(self.transition[state][symbol])
        newStates = tempStates.difference(reachableStates)
        reachableStates = reachableStates | newStates

    statePrime = reachableStates
    accept_statesPrime = self.accept_states & reachableStates
    transitionPrime = self.transition

    for (q, a) in set(itertools.product((self.states.difference(statePrime)), self.alphabet)):
        pop(str(transitionPrime[q][a]))

    dfa_strip = DFA(
        states = reachableStates,
        alphabet = self.alphabet,
        transition = transitionPrime,
        start_state = self.start_state,
        accept_states = accept_statesPrime
    )
    return dfa_strip
    



