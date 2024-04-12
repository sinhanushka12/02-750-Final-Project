# **Final Project for the course Automation of Scientific Research**

## **Performance Evaluation**

First Plot:
Schematic of GP Models and Chemprop

**GP model:**

Run across various batch sizes (1, 25, 50), across 3 seeds

    1. Random Sampling:
        mean: 0.8320423537582441
        standard deviation: 0.01794566021989391
    2. Max Variance (exploration)
    3. Max Mean (exploitation)
    4. UCB (combination)

Plots
    1. MAE vs. Instances 
    2. R2 vs. Instances
    3. Barplots of Accuracy at the end of simulations

**Chemprop model:**

Run across various batch sizes (1, 25, 50), across 3 seeds

    1. Random sampling
    2. Uncertainty sampling (Monte Carlo Dropout)
    3. QBC/Ensemble (if feasible)

Plots
    1. Accuracy vs. Instances
    2. R2 vs. Instances
    3. Barplots of Accuracy at the end of simulations


**Possible additions:**

    1. Other types of models for comparison
    2. density/diversity sampling
    3. maybe DOE?
    4. Tune UCB for exploration vs. exploitation

**Considerations:**

    1. sparse vs. regular GP

