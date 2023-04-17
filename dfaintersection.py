"""
CMSC 141 S Exercise 1
Name:   John Mickey Cabauatan
        Cedric Ramos
        Jianne Rimar Sison
Date: 27 March 2023
"""
import itertools
from dfa import DFA


def dfa_intersection(self, M = DFA()):
    """
    Input two DFAs
    """
    states = set(itertools.product(list(self.states), list(M.states)))
    alphabet = self.alphabet & M.alphabet
    transition = {}
            
    for state in states:
        q1 = state[0]
        r1 = state[1]
        transition[state]={}
        for symbol in alphabet:
            transition[state][symbol] = (self.transition[q1][symbol], M.transition[r1][symbol])
  
    """
    Intersecting two DFAs
    """
    dfa_intersection  = DFA(
        states = states,
        alphabet  = alphabet,
        transition = transition,
        start_state = (self.start_state, M.start_state),
        accept_states = set(itertools.product(self.accept_states, M.accept_states)) 
    )
    return dfa_intersection
