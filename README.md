Final Project for the course Automation of Scientific Research 

Performance Evaluation
GP model:
**Run across various batch sizes (1, 25, 50), across 3 seeds**

    1. Random Sampling:
    
        mean: 0.8320423537582441
        
        standard deviation: 0.01794566021989391
        
    2. Max Variance (exploration)
    3. Max Mean (exploitation)
    4. UCB (combination)

Chemprop model:
**Run across various batch sizes (1, 25, 50), across 3 seeds**
    1. Random sampling
    2. Uncertainty sampling (Monte Carlo Dropout)
    3. QBC/Ensemble (if feasible)


Possible additions:
    1. Other types of models for comparison
    2. density/diversity sampling
    3. maybe DOE?
    4. Tune UCB for exploration vs. exploitation

Considerations:
    1. sparse vs. regular GP

