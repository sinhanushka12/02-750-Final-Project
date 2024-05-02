# **Active Learning Approaches For Ligand Binding Affinity Prediction**
### Final Project for the course Automation of Scientific Research
### **Contributors:** Shweta Jones, Alex Kullman, Anushka Sinha, Aman Virmani

## **Project Overview**
Active learning plays a crucial role in computational drug discovery by optimizing the identification of top binders for a given target protein.

The project intends to use active learning to balance exploration, which seeks novel chemical spaces, and exploitation, which maximizes the identification of potent compounds, to accurately predict ligand binding activity with increased efficiency. The two primary learning models used for this project are a Gaussian process model and the Chemprop deep learning model. Benchmarking active learning approaches can help to identify the best labeling methods for ligand binding affinity. Query selection strategies for the Gaussian process include Upper Confidence Bound (UCB), biased-UCB, Mean, and Variance, whereas the Chemprop model employs uncertainty sampling using Monte Carlo dropout. Both the models used random sampling as a baseline for comparison. The aims of this project are to understand the impact of batch size and uncertainty sampling on the accuracy of the models. Understanding the impact of batch size and sampling methods on the chosen models can help with future computational drug discovery studies. 

This project is loosely based on the paper titled, "Benchmarking Active Learning Protocols for Ligand-Binding Affinity Prediction" by Gorantla et al.

## **Data**
Two publicly available binding affinity datasets are used in this project. The dataset used for training and testing the Gaussian Process and Chemprop models is a binding affinity dataset for the target Tyrosine Kinase 2 (TYK2). It comprises the SMILES representation of 9,997 ligands and their associated binding affinity in terms of their relative binding free energy (RBFE) values which have been converted to pKi values to quantify binding affinity. 

The dataset used for pre-training the Chemprop model is a binding affinity dataset for a different target, Dopamine Receptor D2 (D2R). It contains SMILES of 2,502 different ligands and their associated binding affinity expressed in pKi.

They can be found here: https://github.com/meyresearch/ActiveLearning_BindingAffinity 
![tyk2_distr](https://github.com/sinhanushka12/02-750-Final-Project/assets/55162745/1184a367-1ffd-4d48-8164-bd4795781a3f)

## **Results**
Complete details regarding the methods, implementation, results, and conclusions can be found in the full pdf file in this repository...

The table below provides the runtime, R-squared (R²) values, and Root-Mean Square Error (RMSE) values of all the different models with their respective query selection strategies and batch sizes. The direct comparison between these methods highlights the trade-off between runtime and higher accuracies to make better conclusions about which method is best for ligand binding prediction.


<div align="center">
  <img width="490" alt="Screenshot 2024-05-02 at 12 58 04 PM" src="https://github.com/sinhanushka12/02-750-Final-Project/assets/66140791/9f77654e-b7e2-4c2b-a703-1af5b7a8513a">
</div>

The project performed a comprehensive analysis of different methods and strategies for predicting ligand binding affinity. It explored the relationship between query selection strategies and batch sizes and their impact on runtimes and accuracies. The study shows the need for strategically designed model training for identifying top binders, which potentially could save a significant amount of time and money in drug discovery pipelines.
