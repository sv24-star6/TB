# Tuberculosis Detection from Chest X-Rays: Machine Learning Pilot Study

## Overview

This repository documents a pilot study of automated tuberculosis (TB) detection using chest X-ray images. Handcrafted radiographic features and a convolutional neural network (CNN) were evaluated for binary TB versus non-TB classification. Grad-CAM visualizations were generated to explore the regions influencing CNN predictions.

The study represents the **imaging phase** of a broader research project. Transcriptomic analysis and drug-target prioritization have not yet been performed.

## Dataset

The pilot used 155 labelled chest X-rays from an Indian Jaypee collection:

- **TB:** 78 images
- **Non-TB:** 77 images

Images were resized and converted to grayscale for modelling. The source images are not redistributed in this repository. See the original dataset provider for access and usage conditions.

## Methods

### Handcrafted image features and logistic regression

Images were resized to 128 × 128 pixels. Histogram of oriented gradients (HOG), intensity histograms, gray-level co-occurrence matrix (GLCM) texture features and image intensity statistics were extracted. Features were standardized, and a logistic regression classifier was trained.

### Convolutional neural network

Images were resized to 96 × 96 pixels. A compact CNN containing three convolutional layers was trained for TB versus non-TB classification. Grad-CAM maps were generated for selected held-out examples to visualize regions contributing to the TB prediction score.

### Evaluation

Both approaches were evaluated using five-fold stratified, image-level cross-validation. Out-of-fold predictions were used to calculate accuracy, area under the receiver operating characteristic curve (AUROC), TB sensitivity and non-TB specificity. The models were also compared using paired predictions.

## Pilot results

| Metric | Handcrafted features + logistic regression | CNN |
|---|---:|---:|
| Accuracy | 74.2% | 63.9% |
| AUROC | 0.848 | 0.704 |
| TB sensitivity | 78.2% | 85.9% |
| Non-TB specificity | 70.1% | 41.6% |
| False negatives | 17 | 11 |
| False positives | 23 | 45 |

The handcrafted-feature model achieved higher accuracy and AUROC, whereas the CNN showed higher sensitivity but lower specificity. These results were exploratory and **do not establish clinical diagnostic performance**.

See [model comparison](results/model_comparison.json) for the paired analysis.

## Reproducibility

1. Obtain the images and associated metadata from the original provider.
2. Place the dataset archive in the repository root as `dataset.zip`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the handcrafted-feature experiment: `python run_pilot.py`
5. Run the CNN experiment: `python run_cnn.py`
6. Once both prediction files have been generated, run the paired comparison: `python compare_models.py`

Scripts write generated outputs to the `results/` directory.

## Repository structure

- `run_pilot.py`: handcrafted feature extraction, logistic regression and cross-validation
- `run_cnn.py`: CNN training, evaluation and Grad-CAM generation
- `compare_models.py`: paired comparison of model predictions
- `results/`: summary metrics and selected analysis outputs
- `transcriptomics/`: proposed molecular analysis design, **not completed results**
- `requirements.txt`: Python dependencies

## Limitations

This pilot used a small dataset. Patient-level identifiers were unavailable, so patient independence could not be established. Image acquisition differences, near-duplicate scans, selection bias and limited external generalizability may have affected the results. Grad-CAM maps are exploratory explanations and have not been validated as lesion localization by a radiologist.

The X-ray dataset is not paired with transcriptomic measurements. No radiogenomic associations or drug discovery findings are claimed.
