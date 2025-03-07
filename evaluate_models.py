'''
Script to evaluate the three models; MLP, LSTM, and Transformer on test data. 
Please use the CLI to configure settings for what you would like to evaluate.

python evaluate_models.py --all : Evaluates all three models with the standard test set.
python evaluate_models.py --MLP : Evaluates the MLP static baseline with the standard test set.
python evaluate_models.py --LSTM : Evaluates the LSTM dynamic baseline with the standard test set.
python evaluate_models.py --STTR : Evaluates the ST-TR with the standard test set.

All generate confusion matrices and multi-class f1 in a folder called "results".

To implement:
- selecting specific classes to evaluate over
- selecting specific subsets of the dataset to evaluate over
- iterator: selecting a combination of data subsets and classes to evaluate over.
'''
