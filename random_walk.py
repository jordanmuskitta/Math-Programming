from dataclasses import dataclass
import numpy as np
from typing import Optional
import matplotlib.pyplot as plt

@dataclass
class RandomWalk:
    n: int
    start: float

    def walk_around(self, steps):
        self.walk = [self.start]

        for i in range(steps): 
            rand = np.random.normal()
            next_val = self.walk[-1] + rand
            self.walk.append(next_val)

    def plot_walk(self):
        plt.plot(np.arange(len(self.walk)), self.walk)
        plt.tight_layout()
        plt.show() 
    

if __name__ == "__main__":
    walker = RandomWalk(n=10, start=2.4)
    print(walker.walk_around(100))
    print(walker.walk)
    walker.plot_walk()