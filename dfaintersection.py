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
            
    for state in states:
        for alphabet in alphabet:
            transition = {
                """
                notes:

                state = (q1, q2)

                M1_transition = {
                    "q1": {"0": "q1", "1": "q2"},
                    "q2": {"0": "q3", "1": "q2"},
                    "q3": {"0": "q2", "1": "q2"}
                }
                
                M2_transition = {
                    "r1": {"0": "r1", "1": "r2"},
                    "r2": {"0": "r2", "1": "r2"},
                }
                

                M1&M2_transition = {
                    ("q1", "r2") : {"0": ("q1", "r2"), "1": ("q2", "r2") }
                    ...
                }     


                """

            }


    dfa_intersection  = DFA(
        states = states,
        alphabet  = alphabet,
        transition = transition,
        start_state = (self.start_state, M.start_state),
        accept_states = set(itertools.product(self.accept_states, M.accept_states))
    )
    return dfa_intersection