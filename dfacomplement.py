"""
CMSC 141 X Exercise 1
Name:   John Mickey Cabauatan
        Cedric Ramos
        Jianne Rimar Sison
Date: 27 March 2023
"""

from dfa import DFA

def dfa_complement(self):
    dfa_complement = DFA(states = self.states, 
                        alphabet = self.alphabet, 
                        transition = self.transition, 
                        start_state = self.start_state, 
                        accept_states = self.states.difference(self.accept_states))
    
    return dfa_complement
    #return "\n...For DFA Complement...\n" + f"{str_complement}\n" 
    # I changed the code, need to return DFA class - ji