"""
CS 141 Python Module for Deterministic Finite Automata (DFA)
(q, sigma, delta, q0, f)
q = set of states
sigma = set/collection of symbols
delta = transition function
q0 = element of q, start state
f = subset of q, accept state
"""

class DFA():
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
    
    def __init__(self, states=set(), alphabet=set(), transition=dict(), start_state=None, accept_states=set()):
        """
        Class initialization
        """
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition = transition
        self.start_state = start_state
        self.accept_states = set(accept_states)
        
    def __repr__(self):
        return "Deterministic Finite Automation (DFA) at" + f"{hex(id(self))}"
    
    def __str__(self):
        str_self = (
            self.__repr__() + "\n"
            + "States: " + f"{self.states}\n"
            + "Symbols: " + f"{self.alphabet}\n"
            + "Start State: " + f"{self.start_state}\n"
            + "Accept States: " + f"{self.accept_states}\n"
            + self.str_transition()
        )
        return str_self
    
    def str_transition(self):
        
        string = "Transitions: state, symbol -> state"
        for state in self.transition:
            state_transitions = self.transition[state]
            for symbol in self.alphabet:
                string += "\n\t" + state + " , " + symbol + " -> " + state_transitions[symbol]
        return string
            
    def accepts(self, input_string = ""):
        """
        Returns True if DFA accepts the input string (default is the empty string), otherwise, False.
        """
        
        current_state = self.start_state
        for idx in range(len(input_string)):
            symbol = input_string[idx]
            current_state = self.transition[current_state][symbol]
        if current_state in self.accept_states:
            return True
        else:
            return False