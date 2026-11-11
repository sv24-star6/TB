# TB blood transcriptomics: preprocessing sensitivity analysis

## Data and comparison
- **GSE19439**: discovery cohort, active TB versus latent TB; also active TB versus healthy controls.
- **GSE19442**: validation cohort, active TB versus latent TB.
- Platform: Illumina HumanHT-12 v3 (GPL6947).
- Original GEO signal intensities were compared against local expression matrices; both matched exactly.
- Representative probes were selected using the highest discovery-cohort mean intensity for each gene symbol, with probes required in both cohorts. **18,625 genes** were tested.

## Methods
- **Method A**: `asinh(signal / 10)` on GEO-submitted, average-chip-normalised intensities.
- **Method B**: Method A followed by within-cohort quantile normalisation.
- Differential expression: limma linear model and empirical Bayes moderation (`eBayes(trend=TRUE)`), Benjamini-Hochberg adjusted p-values.
- Replication: adjusted p < 0.05 in both cohorts, with matching effect direction.
- Stable genes: replicated under both preprocessing methods, with consistent direction.

**Important:** asinh-scale limma coefficients are *not* log2 fold changes. This is a preprocessing sensitivity analysis, not independent clinical validation.

## Results
| Metric | Count |
|---|---:|
| Tested genes | 18,625 |
| Method A replicated | 1,689 |
| Method B replicated | 2,044 |
| Stable across both | **1,453** |
| Stable upregulated | 684 |
| Stable downregulated | 769 |
| A only | 236 |
| B only | 591 |

See [sensitivity_summary.csv](sensitivity_summary.csv).

## Interpretation and limitations
The 1,453-gene intersection provides a conservative working set for exploratory pathway enrichment and TB host-response analyses. The two methods are related and do not provide independent replication beyond the two GEO cohorts. Probe annotation, detection p-value filtering, clinical covariates, and the arbitrary asinh scale parameter remain to be evaluated before publication. Blood-cell composition may influence differential expression. These results do not establish diagnostic or therapeutic validity.

## Local analysis outputs
The analysis generated `stable_replicated_genes.csv`, `Method_A_replicated.csv`, `Method_B_replicated.csv`, `final_probe_mapping.csv`, and GEO QC PDFs. They should be uploaded to this folder with the original analysis script to make the results fully reproducible.
