# TB Host Blood Transcriptomics

## Datasets
- GSE19439: 42 samples (13 active TB, 17 latent, 12 healthy)
- GSE19442: 51 samples (20 active TB, 31 latent)
- Both GPL6947, within the same original study programme.

## Completed analyses
- GEO series-matrix verification and sample-label checks
- limma differential expression with 18,625 representative gene symbols
- Method A: `asinh(signal/10)`; Method B: same transform followed by within-cohort quantile normalisation
- BH FDR <0.05 and consistent active-versus-latent effect direction in both cohorts
- 1,689 replicated genes under A, 2,044 under B; **1,453 stable across both** (684 up, 769 down)
- GO-BP ORA: 576 significant upregulated and 77 downregulated term entries
- STRING v12.0 score ≥700 network of 50 selected genes: 108 edges, 13 components, 12 isolates
- L2S2 reversal screening, 30-compound RDKit descriptor audit and focused six-compound literature review

## Documentation
- [Sensitivity analysis](sensitivity_2026/README.md)
- [GO-BP analysis](GO_BP/README.md)
- [Drug repurposing and ADMET evidence](drug_repurposing/README.md)

## Caveats
The asinh-scale limma coefficients are **not log2 fold changes**. Preprocessing approaches use the same samples and do not provide independent biological validation. GSE19439 and GSE19442 originate from the same broader programme. Whole-blood gene expression is vulnerable to cell-composition and clinical confounding. Gene annotations and filtering need review.

The L2S2 10,000-row export was apparently truncated by mimicker significance; re-ranking by reverser significance is **conditional on this subset**. Drug identity and pharmacology require independent verification. Lipinski compliance does not establish ADMET or TB efficacy.

## Next steps
1. Audit probe mappings, detection filtering, clinical covariates and cell composition.
2. Validate in an independent cohort, with GSE37250 as a potential candidate pending metadata verification.
3. Repeat unbiased reverser-oriented LINCS screening and signature-size sensitivity analysis.
4. Confirm chemical identities, compound types, exposure, TB-specific pharmacology and TB-regimen interactions.

The chest X-ray pilot is separate and not patient-matched.

Reference: Berry et al., *Nature* (2010), https://doi.org/10.1038/nature09247
