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



    dfa_intersection  = DFA(
        
    )
    return dfa_intersection