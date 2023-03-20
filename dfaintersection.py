"""
CMSC 141 X Exercise 1
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
    states = set(itertools.product(self.states,M.states))
    alphabet = self.alphabet & M.alphabet
    transition = dict()

    


    dfa_intersection  = DFA(
        states = states,
        alphabet  = alphabet,
        transition = transition,
        start_state = (self.start_state, M.start_state),
        accept_states = set(itertools.product(self.accept_states, M.accept_states))
    )
    return dfa_intersection