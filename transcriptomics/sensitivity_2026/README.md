# TB Blood Transcriptomics: Preprocessing Sensitivity Analysis

## Datasets and design
- GSE19439: discovery, 13 active TB, 17 latent TB and 12 healthy controls.
- GSE19442: validation, 20 active TB and 31 latent TB.
- Platform: Illumina HumanHT-12 v3 (GPL6947).
- Original local GEO expression CSVs matched the source series matrices exactly.
- 18,625 representative gene-symbol probes tested, selected by highest discovery mean intensity among probes found in both cohorts.

## Preprocessing and statistics
- **Method A:** `asinh(signal / 10)` on GEO-submitted average-chip-normalised intensities.
- **Method B:** Method A plus quantile normalisation within each cohort.
- limma `lmFit`, `eBayes(trend=TRUE)`, Benjamini-Hochberg FDR.
- Replicated: adjusted p-value < 0.05 in discovery and validation, with matching direction.
- Stable: replicated in both methods with consistent direction across methods and cohorts.

The limma coefficient is measured on the **asinh scale**, not as a log2 fold change.

## Results
| Metric | Genes |
|---|---:|
| Tested | 18,625 |
| Method A replicated | 1,689 |
| Method B replicated | 2,044 |
| Stable | **1,453** |
| Stable upregulated | 684 |
| Stable downregulated | 769 |
| Method A only | 236 |
| Method B only | 591 |

[Download the committed summary CSV](sensitivity_summary.csv).

## Files and reproducibility status
Currently committed here:
- `README.md`: method, results, caveats.
- `sensitivity_summary.csv`: aggregated counts.

Produced locally but **not yet committed**:
- `stable_replicated_genes.csv`
- `Method_A_replicated.csv`, `Method_B_replicated.csv`
- `Method_A_all_genes.csv`, `Method_B_all_genes.csv`
- `final_probe_mapping.csv`
- QC boxplots, PCA and cross-cohort plots
- `TB_sensitivity_analysis.R` and session information



## Limitations
The overlap supports robustness to two related preprocessing choices, not independent biological validation. The fixed asinh scale of 10 is a modelling choice. Additional work is needed on probe specificity, detection filtering, cell-composition confounding, clinical covariates and empirical Bayes variance assumptions. Do not interpret these genes as validated TB diagnostics or therapeutic targets.


