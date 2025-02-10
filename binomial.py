from typing import List, Optional
from dataclasses import dataclass
import numpy as np
from math import factorial

@dataclass
class Binomial:
    n: int
    p: float
    trials: int

    def calc_ev(self): 
        return self.n * self.p
    
    def calc_var(self):
        return self.calc_ev()*(1-self.p)


    def gen_rand(self):
        rand = np.random.random()
        # Check that our random number generated is below the limit, probability p. 
        if rand <= self.p:
            return 1 # Return 1 to indicate success
        else:
            return 0
        

    def simulate_dist(self):
        # Initialize the dictionary with keys and 0 values. 
        self.results = {i: 0 for i in range(self.trials)}
        
        # Simulate the results for every trial
        for i in range(0, self.trials):
            # Keep count of the running total for the trial
            n_count = 0
            for j in range(0, self.n):
                # Use the random generator function here
                if self.gen_rand() == 1: 
                    n_count += 1
            
            # Set dictionary values
            self.results[i] += n_count
        
        return self.results

    def plot_pmf(self):
        pass

if __name__ == "__main__":
    bin = Binomial(100, 0.5, 100)
    print(bin.simulate_dist())


    
