# User-Authentication-using-Keylogger-and-Mouse-Dynamics


Data:
Download the dataset from https://drive.google.com/drive/u/0/my-drive and unzip in the code directory. 

Libraries:
Please use pip install before running any code
1) json (to save, load, get pre preprocessed data)
2) numpy (for vector operation)
3) sklearn (for k-fold split, evaluation metrics)
4) susi (for Self Organizing Map)
5) matplotlib (For Plots)



Instructions for creating data:
1) The data collected from group 4 and 5 in placed in the Processed folder.(downloaded from drive link and unzipped)
2) To convert this data into 702 dimensional feature vector, run python3 feature_vector_extraction.py
3) This will create a json file with the training and testing data


Instructions for running code to train and test model:
1) Run python3 model_train_test.py to train the SOM classsifier and get the results. 
