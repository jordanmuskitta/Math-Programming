from typing import List, Optional
from dataclasses import dataclass
import numpy as np
from math import factorial
import matplotlib.pyplot as plt

@dataclass
class Geometric:
    # Recall: Geometric distribution is defined as P(X=k) = (1-p)**(k-1)*p 
    # where: p is the probability of success and k is the number of independent trials
    n: int
    k: int
    p: float

    def calc_ev(self): 
        return 1/self.p
    
    def calc_var(self):
        return (1-self.p)/(self.p)**2
    

    def rand_gen(self): 
        rand = np.random.random()
        
        if rand < self.p:
            return 1
        
        else: 
            return 0
        
    def simulate_dist(self):
        self.results = {i: 0 for i in range(0, self.n)}

        for i in range(0, self.n):
            k_count = 1
            while k_count <= self.k:
                if self.rand_gen() == 1: 
                    break
                k_count += 1
            self.results[i] = k_count
        return self.results


    def plot_pmf_cdf(self):
        res_list = list(self.results.values())
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        # PMF plot
        ax1.hist(res_list, bins=range(1, self.k + 2), density=True, 
                alpha=0.7, color='blue', edgecolor='black')
        ax1.set_title('PMF')
        ax1.set_xlabel('Number of Trials Until Success')
        ax1.set_ylabel('Probability')
        
        # CDF plot
        ax2.hist(res_list, bins=range(1, self.k + 2), density=True, 
                cumulative=True, alpha=0.7, color='green', edgecolor='black')
        ax2.set_title('CDF')
        ax2.set_xlabel('Number of Trials Until Success')
        ax2.set_ylabel('Cumulative Probability')
        
        plt.tight_layout()
        plt.show()



if __name__ == "__main__": 
    geom = Geometric(1000, 100, 0.10)
    geom.simulate_dist()
    geom.plot_pmf_cdf()