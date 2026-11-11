# TB Host Blood Transcriptomics: Completed Exploratory Analysis

## Status
**Differential-expression, GEO matrix verification, cross-cohort replication and preprocessing sensitivity analysis completed.** GO/KEGG/Reactome enrichment, updated probe annotation, detection p-value filtering, clinical-confounder assessment and host-directed drug-target prioritisation remain future work.

The chest X-ray pilot uses a separate, unpaired dataset. No patient-level radiogenomic association can be inferred.

## Public datasets
| Dataset | Role | Samples | Groups |
|---|---|---:|---|
| [GSE19439](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19439) | Discovery | 42 | 13 active TB, 17 latent TB, 12 healthy |
| [GSE19442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19442) | Validation | 51 | 20 active TB, 31 latent TB |

Both use Illumina HumanHT-12 v3 (GPL6947) and belong to the broader [GSE19491](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19491) study collection. GEO-submitted signal intensities were produced using Illumina BeadStudio and average chip normalisation. The locally prepared expression matrices matched the GEO series matrices exactly.

## Completed methods
1. Audited local GEO matrices and sample group labels.
2. Inspected signal distributions, including negative intensities, and transformation/normalisation diagnostics.
3. Restricted to probes present in both cohorts, then selected one representative probe per gene symbol using highest mean intensity in the discovery cohort (18,625 genes).
4. Applied two preprocessing methods independently within each cohort:
   - **A:** `asinh(signal / 10)`, retaining GEO-submitted normalisation.
   - **B:** A followed by between-array quantile normalisation.
5. Applied limma linear modelling with empirical Bayes moderation (`eBayes(trend=TRUE)`) to active versus latent TB in each cohort; active versus healthy was also evaluated in GSE19439.
6. Called genes replicated when FDR < 0.05 in both cohorts and effect direction matched; intersected replicating genes across A and B with consistent direction.

**The asinh-transformed effect coefficients are not log2 fold changes.**

## Sensitivity results
| Outcome | Count |
|---|---:|
| Tested genes | 18,625 |
| Method A replicated | 1,689 |
| Method B replicated | 2,044 |
| Stable in both methods | **1,453** |
| Stable upregulated | 684 |
| Stable downregulated | 769 |
| A only | 236 |
| B only | 591 |

See [sensitivity_2026/README.md](sensitivity_2026/README.md) and [sensitivity_2026/sensitivity_summary.csv](sensitivity_2026/sensitivity_summary.csv). Detailed output CSVs, scripts and figures still need to be committed for complete reproducibility.

## Next steps
- Review current probe-to-gene mappings and Illumina detection p-values.
- Examine sample-level confounders and potential changes in blood-cell composition.
- Assess robustness to the chosen asinh scale and limma variance assumptions.
- Perform GO, KEGG and Reactome enrichment using the tested-gene background and separate up/down sets.
- Prioritise possible host-directed targets only after pathway and external evidence review.

## Interpretation and limitations
The 1,453-gene intersection is a conservative **exploratory** gene set. Methods A and B are related transformations of the same GEO measurements; agreement does not establish independent experimental validation. Cohorts may differ in population, sampling and other clinical variables. No drug repurposing or docking conclusions are claimed.

## Reference
Berry et al. *Nature* (2010). [DOI: 10.1038/nature09247](https://doi.org/10.1038/nature09247).
