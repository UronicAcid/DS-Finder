#!/usr/bin/env python
# coding: utf-8

import argparse
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_model(model_path):
    """Load the model from the specified file"""
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_dataset(dataset_path):
    """Load the dataset from the specified file"""
    return pd.read_csv(dataset_path)

def check_column_names(df, required_columns):
    """Check if the dataframe contains the required columns"""
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(missing_columns)}")
    return True

def preprocess_data(df, columns_to_scale):
    """Preprocess the data by filling NaN values and scaling numerical columns"""
    df[columns_to_scale] = df[columns_to_scale].fillna(0)
    std_scaler = StandardScaler()
    X = df[columns_to_scale]
    numeric_columns = X.select_dtypes(include=['float64', 'int64']).columns
    X[numeric_columns] = std_scaler.fit_transform(X[numeric_columns])
    return X

def main(model_path, dataset_path, output_path):
    # Load the model
    model = load_model(model_path)

    # Load the dataset
    df = load_dataset(dataset_path)

    # Check if the required columns are present in the dataset
    required_columns = ['expression_log', 'gene_effect', 'original_codon_freq', 'mutated_codon_freq',
                        'mutated_codon_norm_freq', 'codon_freq_norm_change', 'splicing_score',
                        'silva_X.GERP..', 'silva_dRSCU', 'absplice_tissue', 'CADD_RawScore',
                        'position', 'gene_aa_num', 'wildtype_energy', 'energy_change',
                        'energy_change_abs_ratio', 'silva_CpG_exon', 'silva_X.CpG.', 'DS_DL',
                        'DS_DG', 'mutated_codon_index3', 'original_codon_index3']
    check_column_names(df, required_columns)

    # Preprocess the data
    X = preprocess_data(df, required_columns)
    X.columns = ['expression', 'gene effect', 'old codon frequency', 'new codon frequency',
                 'new codon normalized frequency', 'delta codon normalized frequency', 'SpliceAI score',
                 'conservation score', 'dRSCU', 'AbSplice score', 'CADD score',
                 'position', 'gene length', 'WT RNA folding energy', 'RNA folding energy change',
                 '|energy change ratio|', 'exon CpG', 'nucleitide CpG', 'SpliceAI DS DL',
                 'SpliceAI DS DG', 'new codon position3', 'old codon position3']

    # Make predictions with the model
    y_pred = model.predict(X)
    y_score = model.predict_proba(X)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(X)

    # Save the prediction results
    df['predicted_y'] = y_pred
    df['predicted_y_score'] = y_score
    df.to_csv(output_path, index=False)

    # Print the model score
    print(f"Model Score: {model.score(X, y_pred)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prediction script using a pre-trained model")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the model file")
    parser.add_argument("--dataset_path", type=str, required=True, help="Path to the dataset file")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the prediction results")
    args = parser.parse_args()
    
    main(args.model_path, args.dataset_path, args.output_path)
