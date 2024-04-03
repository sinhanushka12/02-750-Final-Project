#Loading in packages
import numpy as np
import pandas as pd
import GPy
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.utils import shuffle
import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from scipy.stats import spearmanr

#Converting to fingerprints
def smiles_to_fingerprint(smiles, nBits=4096):
    mol = Chem.MolFromSmiles(smiles)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=4, nBits=nBits, useChirality=True)
    return list(fp)


#This function runs sequential model-based optimization. This function works by training a sparse GP model on the start data, 
#and using a selection/activation function that performs UCB to select the data point to query.
#Input: starting data and unlabeled remaining data
#Output: Instance with the maximum GP mean upon prediction, as well as the actual value (if it is 9.0)

def smbo(start_X, start_y, remaining_X):
    
    k = GPy.kern.RBF(start_X.shape[1])

    m = GPy.models.SparseGPRegression(start_X, start_y, k)

    m.optimize('bfgs', max_iters=10)

    mean, var = m.predict(remaining_X, full_cov=False)

    return mean, var

def uncertainty_sampling(flag, batch_size, data):
    seeds = [1,2,3]

    rmse_vals = []
    r2_vals = []
    spear_vals = []

    for seed in seeds:

        rmse_instance =[]
        r2_instance = []
        spear_instance = []
        
        #Getting X and y values to start with
        X = np.array([val for val in data['fingerprint'].values])
        y = data['target'].values.reshape(-1,1)
        X, y = shuffle(X,y, random_state=seed)

        size = int(len(X) * 0.1)
        start_X = X[:size]
        start_y = y[:size]

        remaining_X = X[size:]
        remaining_y = y[size:]

        #set initial variables for calculating UCB
        Dsize = len(X)
        bo_lambda = 0.1 #ADJUST LATER
        bo_iters = 1 #ADJUST LATER

        #calculate beta constant from 
        beta = 2 * math.log(Dsize * math.pow(bo_iters,2) * math.pow(np.pi,2) / (6 * bo_lambda) )

        counter = 0

        #Until we sample another 70%...
        while len(start_X) < int(len(X) * 0.8):

            #run smbo and get the sparse GP parameters to select the next instance
            mean, var = smbo(start_X, start_y, remaining_X)

            #depending on the selection function, we calculate a specific alpha_full value
            if flag == "ucb":
                #get the UCB value at each x
                alpha_full = mean + math.sqrt(beta) * var
            elif flag == "mean":
                alpha_full = mean
            else:
                alpha_full = var

            #get the index for the row with the largest UCB
            sorted = np.argsort(alpha_full)
            inds = sorted[-batch_size:]
            inds = np.sort(inds)[::-1]

            for ind in inds:
                #adding the row of the selected index to the starting data
                start_X = np.vstack((start_X, remaining_X[ind,:]))
                start_y = np.vstack((start_y, remaining_y[ind]))

                #removing the row of the selected index from the remaining data
                remaining_X = np.delete(remaining_X, ind, axis=0)
                remaining_y = np.delete(remaining_y, ind)


            if counter % 500 == 0:
                #creating kernel
                k = GPy.kern.RBF(start_X.shape[1])

                #training and optimizing GP regression model
                m = GPy.models.GPRegression(start_X, start_y, k)
                print("model trained")
                m.optimize('bfgs', max_iters=10)
                print("model optimized")

                #Predicting on final 20%
                pred_means, pred_vars = m.predict(remaining_X)

                #Getting rmse score
                rmse_instance.append(np.sqrt(mean_squared_error(remaining_y, pred_means)))
                r2_instance.append(r2_score(remaining_y, pred_means))
                spear_instance.append(spearmanr(remaining_y, pred_means).statistic)
            
            counter += batch_size

        rmse_vals.append(rmse_instance)
        r2_vals.append(r2_instance)
        spear_vals.append(spear_instance)
            
    #return r2 vals
    return r2_vals

    


def main():
    # Loading in data and subsetting columns
    data = pd.read_csv("TYK2_final.csv")
    data = data.drop(['target', 'top_2p', 'top_5p'], axis=1)
    column_names = ['smiles', 'target']
    data.columns = column_names
    
    data['fingerprint'] = data['smiles'].apply(smiles_to_fingerprint)

    batch_sizes = [1,25,50]
    flag = "mean"
    mean_rmse_dict = {}
    mean_r2_dict = {}
    mean_spear_dict = {}

    final_mean_data = pd.DataFrame()

    for batch in batch_sizes:

        mean_rmse, mean_r2, mean_spear = uncertainty_sampling(flag, batch, data)

        mean_rmse_mean = np.mean(mean_rmse, axis=0)
        mean_rmse_stdev = np.std(mean_rmse, axis=0)
        print("mean:", mean_rmse_mean)
        print("standard deviation:", mean_rmse_stdev)
        mean_rmse_dict[batch] = (mean_rmse, mean_rmse_mean, mean_rmse_stdev)
        final_mean_data[f"{batch}_rmse_mean"] = mean_rmse_mean
        final_mean_data[f"{batch}_rmse_stdev"] = mean_rmse_stdev


        mean_r2_mean = np.mean(mean_r2, axis=0)
        mean_r2_stdev = np.std(mean_r2, axis=0)
        print("mean:", mean_r2_mean)
        print("standard deviation:", mean_r2_stdev)
        mean_r2_dict[batch] = (mean_r2, mean_r2_mean, mean_r2_stdev)
        final_mean_data[f"{batch}_r2_mean"] = mean_r2_mean
        final_mean_data[f"{batch}_r2_stdev"] = mean_r2_stdev

        mean_spear_mean = np.mean(mean_spear, axis=0)
        mean_spear_stdev = np.std(mean_spear, axis=0)
        print("mean:", mean_spear_mean)
        print("standard deviation:", mean_spear_stdev)
        mean_spear_dict[batch] = (mean_spear, mean_spear_mean, mean_spear_stdev)
        final_mean_data[f"{batch}_spear_mean"] = mean_spear_mean
        final_mean_data[f"{batch}_spear_stdev"] = mean_spear_stdev


    final_mean_data.to_csv("final_data_mean.csv")

if __name__ == "__main__":
    main()

