# DS Finder

This project includes a script for loading a pre-trained model and making predictions on a dataset. The script can read model file paths and dataset file paths from the command line, preprocess the data, and output the prediction results.



## Dependencies

Before running the script, ensure you have the following Python libraries installed:

- pandas
- numpy
- scikit-learn
- catboost

### Using Conda to Install Dependencies

You can create a new Conda environment and install the dependencies with the following commands:

```sh
conda create -n model-prediction python=3.8
conda activate model-prediction
conda install pandas numpy scikit-learn
pip install catboost
```

### Using pip to Install Dependencies
Alternatively, you can install the dependencies using pip:
```sh
pip install pandas numpy scikit-learn catboost
```

## Usage
Command Line Arguments
--model_path: Path to the model file (required).
--dataset_path: Path to the dataset file (required).
--output_path: Path to save the prediction results (required).

**required_columns in dataset**
```python
required_columns = ['expression_log', 'gene_effect', 'original_codon_freq', 'mutated_codon_freq',
                        'mutated_codon_norm_freq', 'codon_freq_norm_change', 'splicing_score',
                        'silva_X.GERP..', 'silva_dRSCU', 'absplice_tissue', 'CADD_RawScore',
                        'position', 'gene_aa_num', 'wildtype_energy', 'energy_change',
                        'energy_change_abs_ratio', 'silva_CpG_exon', 'silva_X.CpG.', 'DS_DL',
                        'DS_DG', 'mutated_codon_index3', 'original_codon_index3']
```
                        
**Running the Script**
Run the following command in your terminal:
```shell
python prediction.py --model_path model/240304_catboost_model_trained_on_HCT116_D35.sav --dataset_path test_dataset.csv --output_path output.csv
```

