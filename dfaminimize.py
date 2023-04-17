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
    
    reachableStates = set(self.start_state)
    newStates = set(self.start_state)

    while newStates != ():
        tempStates = set()
        for state in newStates:
            for symbol in self.alphabet:
                    tempStates.add(self.transition[state][symbol])
        newStates = tempStates.difference(reachableStates)
        reachableStates = reachableStates.union(newStates)

    statePrime = reachableStates
    accept_statesPrime = self.accept_states & reachableStates
    transitionPrime = self.transition

    for (q, a) in set(itertools.product((self.states.difference(statePrime)), self.alphabet)):
        del transitionPrime[q][a]

    dfa_strip = DFA(
        states = reachableStates,
        alphabet = self.alphabet,
        transition = transitionPrime,
        start_state = self.start_state,
        accept_states = accept_statesPrime
    )
    return dfa_strip

def dfa_minimize(self):
    
    M = dfa_strip(self)
    G = {dict(itertools.product(self.states, self.states)) : {0}}
    #G = { (q, r): {0} for q in selfl.states for r in self.states}