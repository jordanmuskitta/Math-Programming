from typing import List, Optional
from dataclasses import dataclass
import numpy as np
from math import factorial
import matplotlib.pyplot as plt

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
        res_list = self.results.values()
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        # PMF plot
        ax1.hist(res_list, bins=range(self.n + 2), density=True, 
                alpha=0.7, color='blue', edgecolor='black', rwidth=0.8)
        ax1.set_title('PMF')
        ax1.set_xlabel('Number of Successes')
        ax1.set_ylabel('Probability')

        # CDF plot
        ax2.hist(res_list, bins=range(self.n + 2), density=True, 
                cumulative=True, alpha=0.7, color='green', 
                edgecolor='black', rwidth=0.8)
        ax2.set_title('CDF')
        ax2.set_xlabel('Number of Successes')
        ax2.set_ylabel('Cumulative Probability')


        plt.tight_layout()
        plt.show()        

if __name__ == "__main__":
    
    # Initialise object
    bin = Binomial(100, 0.5, 1000)

    # Print the theorectical expected value and variance
    print(f"The expected value: {bin.calc_ev()}")
    print(f"The variance: {bin.calc_var()}")
    
    bin.simulate_dist()
    bin.plot_pmf()


    
