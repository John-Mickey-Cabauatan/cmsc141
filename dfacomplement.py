"""
CMSC 141 S Exercise 1
Name:   John Mickey Cabauatan
        Cedric Ramos
        Jianne Rimar Sison
Date: 27 March 2023
"""

from dfa import DFA

def dfa_complement(self):
    """
    Class for Deterministic Finite Automata (DFA)
    Attributes
    ------
        states (q): set
        alphabet (sigma): set
        transition (delta): dict
            transition function of the form transition [state][symbol] -> state
        start_state (q0): str
        accept_state (f): set
    """
    dfa_complement = DFA(states = self.states, 
                        alphabet = self.alphabet, 
                        transition = self.transition, 
                        start_state = self.start_state, 
                        accept_states = self.states.difference(self.accept_states))  #accept states (f) = (Q - f)
    
    return dfa_complement
