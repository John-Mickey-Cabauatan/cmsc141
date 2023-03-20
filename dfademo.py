from dfa import DFA
from dfacomplement import dfa_complement

if __name__ == "__main__":
        M = DFA(states={"q1", "q2", "q3"}, alphabet={"0","1"}, 
                transition = {
                    "q1": {"0": "q1", "1": "q2"},
                    "q2": {"0": "q3", "1": "q2"},
                    "q3": {"0": "q2", "1": "q2"}
                }, start_state="q1", accept_states = {"q2"})
        print(M)

        N = dfa_complement(M) #need help, how to to it like this -> N = M.dfa_complement()
        print(N)

        for input_string in ["100", "101", "11101010101010101", "110"]:
            print(M.__repr__() + " accepts " + input_string + "? " + str(M.accepts(input_string)))