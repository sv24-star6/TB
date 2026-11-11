# Tuberculosis Research: Chest X-ray Classification and Host Blood Transcriptomics

## Overview
This repository contains two **independent exploratory research components**:
1. A chest X-ray machine-learning pilot comparing handcrafted features with a convolutional neural network (CNN).
2. A whole-blood microarray analysis comparing active versus latent tuberculosis (TB), with cross-cohort replication and preprocessing sensitivity testing.

**The imaging and transcriptomic samples are not patient-matched.** No radiogenomic associations, clinical diagnostic claims, or validated therapeutic targets are inferred.

## Chest X-ray pilot
The imaging dataset comprises 155 labelled chest X-rays from an Indian Jaypee collection (78 TB, 77 non-TB). Original images are not redistributed.

Images were analysed using handcrafted HOG, intensity histogram, GLCM and summary intensity features with logistic regression, and a three-convolutional-layer CNN. Both models used five-fold stratified, image-level cross-validation; CNN Grad-CAM images were exploratory.

| Metric | Handcrafted + logistic regression | CNN |
|---|---:|---:|
| Accuracy | 74.2% | 63.9% |
| AUROC | 0.848 | 0.704 |
| TB sensitivity | 78.2% | 85.9% |
| Non-TB specificity | 70.1% | 41.6% |
| False negatives | 17 | 11 |
| False positives | 23 | 45 |

See [model comparison](results/model_comparison.json). Patient-level independence could not be confirmed, and results do not establish clinical performance.

### Reproduce imaging pilot
1. Obtain the original image dataset and metadata from its provider; place the archive at the repository root as `dataset.zip`.
2. Run `pip install -r requirements.txt`.
3. Run `python run_pilot.py` and `python run_cnn.py`.
4. Run `python compare_models.py` after both prediction files exist.

## Host blood transcriptomics
- **Discovery:** [GSE19439](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19439), 42 samples (13 active TB, 17 latent TB, 12 healthy controls).
- **Validation:** [GSE19442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19442), 51 samples (20 active TB, 31 latent TB).
- **Platform:** Illumina HumanHT-12 v3, GPL6947.
- Local expression matrices were checked against original GEO series matrices and matched exactly.
- **18,625** representative gene-symbol probes were analysed with limma.
- Two sensitivity approaches: `asinh(signal/10)` on GEO-submitted intensities (A), and the same transform plus within-cohort quantile normalisation (B).
- Replication required Benjamini-Hochberg FDR < 0.05 in both cohorts and consistent direction. Stable genes also had to meet this criterion under both preprocessing methods.

| Result | Genes |
|---|---:|
| Replicated under Method A | 1,689 |
| Replicated under Method B | 2,044 |
| Stable under both | **1,453** |
| Stable upregulated | 684 |
| Stable downregulated | 769 |

Read [transcriptomics methods and status](transcriptomics/README.md), [sensitivity analysis](transcriptomics/sensitivity_2026/README.md), and [completed GO-BP enrichment findings](transcriptomics/GO_BP/README.md) (576 upregulated and 77 downregulated significant GO terms). The [sensitivity summary](transcriptomics/sensitivity_2026/sensitivity_summary.csv) is committed; detailed gene-level CSVs and QC images are not yet included in the repository.

**Interpretation:** These are exploratory host-response associations, not diagnostic markers or validated drug targets. The asinh-scale limma coefficients are not log2 fold changes. Detection filtering, probe annotation, cell-composition effects, clinical covariates and the asinh scale parameter need further assessment before publication.

## Repository layout
- `run_pilot.py`, `run_cnn.py`, `compare_models.py`: imaging analyses
- `results/`: imaging results and selected figures
- `transcriptomics/README.md`: transcriptomic data, workflow and outstanding validation
- `transcriptomics/sensitivity_2026/`: sensitivity documentation and summary table
- `requirements.txt`: imaging Python dependencies

## Study limitations
Imaging data are limited in size and may contain patient-level overlap, acquisition bias or near-duplicates. Blood transcriptomic cohorts are independent of the X-ray collection. Transcriptomic replication across cohorts and preprocessing choices does not replace biological or prospective validation.

## Reference
Berry et al. *Nature* (2010). [DOI: 10.1038/nature09247](https://doi.org/10.1038/nature09247).
