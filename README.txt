User Authentication based on Key-stroke Logging using Self Organizing maps
Group-4                         
Pranit Chawla                  (17EC35017)
Pravartya Dewangan      (17EC35041)
Subhadeep Paul              (17EC10064)
Sumegh Roychowdhury  (17EC35033)
Vandit Sharma                 (17EC10060)

This folder has the following:
1) Report_Group_4.pdf
2) Presentation_group_4.pptx
3) feature_vector_extraction.py (code to generate feature vectors)
4) model_train_test.py (code to train and test model)
5) mean_feature_vector.json (preprocessed data)


Data:
Download the dataset from https://drive.google.com/file/d/1qnRSyw47qJ0amQfFWRPIW0SK01c8-fAT/view and unzip in the code directory. 

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

