import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional



@dataclass
class MarkovChain:
    states: Dict[int, np.ndarray]
    
    def __post_init__(self):
        # Initialise dependent attributes after states is set
        unique_states = set(tuple(state) for state in self.states.values())
        self.state_list = np.array(list(unique_states))
        self.n = len(self.state_list)
        self.trans_matrix = np.zeros((self.n, self.n))

    def calc_trans_p(self):
        # Create a zero matrix
        counts = np.zeros((self.n, self.n))

        # Iterrate n - 1 times, need to reduce by one to account for the +1 for next state
        for i in range(len(self.states) - 1): 
            curr = tuple(self.states[i])
            next_state = tuple(self.states[i+1])

            # Create a bool mask -> return indices where TRUE, [0][0] drill down to the bottom layer
            from_idx = np.where([np.array_equal(curr, tuple(s)) for s in self.state_list])[0][0]
            to_idx = np.where([np.array_equal(next_state, tuple(s)) for s in self.state_list])[0][0]
            
            # Increase the counts by 1
            counts[from_idx][to_idx] += 1
        
        print(counts)
        
        for i in range(self.n): 
            row_sum = np.sum(counts[i])
            if row_sum > 0: 
                self.trans_matrix[i] = counts[i]/row_sum
        print(self.trans_matrix)
        return self.trans_matrix
    
    def print_transitions(self):
        # Print in a readable format
        print("\nTransition Matrix:")
        print("From State -> To State: Probability")
        for i in range(self.n):
            for j in range(self.n):
                if self.trans_matrix[i][j] > 0:
                    print(f"{tuple(self.state_list[i])} -> {tuple(self.state_list[j])}: {self.trans_matrix[i][j]:.2f}")


@dataclass
class DataGenerator:
    n: int # Number of required samples
    space: np.ndarray # This will take all the combinations of our states
    results: Optional[Dict] = None
    
    def gen_rand(self):
        self.results = {}
        for i in range(self.n):
            # Randomly select a state from space
            self.results[i] = self.space[np.random.randint(0, len(self.space))]
        return self.results



if __name__ == "__main__":
    # t_state = np.array([1,2,3,4])
    positions = ['long', 'short', 'hold']
    volumes = ['low', 'mid', 'high']
    
    t_state = np.array([(pos, vol) for pos in positions for vol in volumes])
    data_gen = DataGenerator(n=100, space=t_state)
    sample_df = data_gen.gen_rand()

    m_chain = MarkovChain(sample_df)
    trans_prob = m_chain.calc_trans_p()
    m_chain.print_transitions()

    # print(m_chain)
