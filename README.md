# **Active Learning Approaches For Ligand Binding Affinity Prediction**
## Final Project for the course Automation of Scientific Research
## **Contributors:** Shweta Jones, Alex Kullman, Anushka Sinha, Aman Virmani

### **Project Overview**
Active learning plays a crucial role in computational drug discovery by optimizing the identification of top binders for a given target protein.

The project intends to use active learning to balance exploration, which seeks novel chemical spaces, and exploitation, which maximizes the identification of potent compounds, to accurately predict ligand binding activity with increased efficiency. The two primary learning models used for this project are a Gaussian process model and the Chemprop deep learning model. Benchmarking active learning approaches can help to identify the best labeling methods for ligand binding affinity. Query selection strategies for the Gaussian process include Upper Confidence Bound (UCB), biased-UCB, Mean, and Variance, whereas the Chemprop model employs uncertainty sampling using Monte Carlo dropout. Both the models used random sampling as a baseline for comparison. The aims of this project are to understand the impact of batch size and uncertainty sampling on the accuracy of the models. Understanding the impact of batch size and sampling methods on the chosen models can help with future computational drug discovery studies. 

This project is loosely based on the paper titled, "Benchmarking Active Learning Protocols for Ligand-Binding Affinity Prediction" by Gorantla et al.

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

