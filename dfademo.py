from dfa import DFA
from dfacomplement import dfa_complement
from dfaintersection import dfa_intersection
from dfaminimize import dfa_minimize

if __name__ == "__main__":
        M = DFA(states={"q1", "q2", "q3"}, alphabet={"0","1"}, 
                transition = {
                    "q1": {"0": "q2", "1": "q3"},
                    "q2": {"0": "q2", "1": "q2"},
                    "q3": {"0": "q3", "1": "q3"}
                }, start_state="q1", accept_states = {"q2"})
        print(M)

        N = dfa_complement(M)
        print(N)

        M2 = DFA(states={"r1", "r2", "r3", "r4", "r5"}, alphabet={"0","1"}, 
                transition = {
                    "r1": {"0": "r2", "1": "r1"},
                    "r2": {"0": "r2", "1": "r3"},
                    "r3": {"0": "r3", "1": "r4"},
                    "r4": {"0": "r4", "1": "r5"},
                    "r5": {"0": "r5", "1": "r5"},
                }, start_state="r1", accept_states = {"r1", "r2", "r3", "r4"})

        O = dfa_intersection(M,M2)
        print("\n\nFor intersection: \n")
        print(O)

        for input_string in ["100", "101", "11101010101010101", "110"]:
            print(M.__repr__() + " accepts " + input_string + "? " + str(M.accepts(input_string)))

        # Minimize M
        P = dfa_minimize(M)
        print("\nMinimized DFA: \n")
        print(P)