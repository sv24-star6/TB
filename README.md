# Tuberculosis chest X-ray classification: pilot study

Reproducible **research pilot** using 155 chest X-rays (78 TB-labelled, 77 non-TB-labelled) from the Jaypee Indian chest X-ray collection. Compares handcrafted HOG, histogram and GLCM features with logistic regression against a small CNN. Includes held-out Grad-CAM visualisations.

## Results (5-fold image-level cross-validation)

| Metric | Handcrafted + logistic regression | CNN |
|---|---:|---:|
| Accuracy | 74.2% | 63.9% |
| AUROC | 0.848 | 0.704 |
| Sensitivity (TB) | 78.2% | 85.9% |
| Specificity (non-TB) | 70.1% | 41.6% |
| False negatives | 17 | 11 |
| False positives | 23 | 45 |

Results are **preliminary, not clinically validated**. Patient identifiers are unavailable, so patient-level independence and external generalisation are unverified. Exact file duplicates were not found, but visually near-duplicate scans and acquisition confounding have not been ruled out.

## Reproduce

1. Obtain the dataset from its original provider and place the archive at `dataset.zip` in the repository root. The dataset is **not included**.
2. Install requirements: `pip install -r requirements.txt`
3. Run `python run_pilot.py`
4. Run `python run_cnn.py`

Both scripts save output to `results/`. The feature model uses 128×128 grayscale images, HOG, 16-bin histogram, GLCM features and standardized logistic regression (C=0.01). The CNN uses 96×96 grayscale images, three convolutional layers, 12 epochs per fold, random initialization and no hyperparameter tuning. Both use stratified five-fold image-level out-of-fold predictions.

## Repository contents

- `run_pilot.py`: handcrafted features, logistic regression, predictions and metrics
- `run_cnn.py`: CNN, predictions, metrics and held-out Grad-CAM examples
- `results/`: previously generated pilot outputs
- `requirements.txt`: dependencies

The Grad-CAM overlays show model attention, **not confirmed lesion localization**. The radiologist review template contains model outputs and is not blinded; remove those fields before blinded review.

No transcriptomic analysis, radiogenomic association, docking or drug repurposing was performed. This repository documents the imaging phase only. Avoid claiming molecular validation from these results.
