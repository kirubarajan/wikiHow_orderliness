# wikiHow Orderliness Prediction
This repository contains data and code for the wikiHow Orderliness Prediction project, annotated and implemented by Aditya Kashyap, Arun Kirubarajan and Li Zhang {kashyap, kiruba, zharry}@seas.upenn.edu. This is a part of a project for the University of Pennsylvania CIS 700 course in Spring 2020.

## Data
Access the annotations and predicted labels [here](https://drive.google.com/file/d/1miFUCvLKF7jeeqwR0_bWp-rNaJIGgy9_/view). 

## Usage
To replicate our results:
1. In `split_cv.py`, replace the file path with the path to the 1,000 annotations, and the path to output the splits. Running the script produces two files: `train.csv` and `val.csv` in the output directory.
2. Run the [HuggingFace interface](https://huggingface.co/transformers/examples.html#fine-tuning-on-swag) to fine-tune a Roberta model on the directory containing the splits. The code to run the HuggingFace interface is NOT contained in this repository. 
3. In `perf_cv.py`, replace the file path with the path to the output directory of the HuggingFace model. Running the script produces precision, recall and F1-score. 
4. Run `abalation.sh` to perform abalation analysis.
