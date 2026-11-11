# Molecular analysis: TB host transcriptomics

## Data selection

[GSE19491](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19491) is a **SuperSeries**, not a homogeneous discovery cohort. It contains UK training/test sets, South African samples, longitudinal samples, and other inflammatory diseases. Do **not** combine all 498 samples into a single active-TB versus healthy-control comparison.

Start with the UK training subseries [GSE19439](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19439), inspect metadata, and manually verify case/control labels. Reserve a separate cohort such as GSE19442 for external validation only after checking platform, preprocessing, sample independence and clinical labels.

## Analysis plan

1. Audit accession, sample IDs, clinical groups, time points and platform.
2. Use normalized expression values; inspect their scale and missingness before transformation.
3. Perform active-TB versus healthy-control differential expression using a properly specified design (limma is recommended for microarrays, including relevant covariates where available).
4. Adjust for multiple comparisons (Benjamini-Hochberg); map probes to genes using the exact platform annotation.
5. Validate gene direction and effect size in an independent cohort; test specificity against other inflammatory diseases.
6. Enrich replicated gene sets for GO/Reactome pathways with an appropriate tested-gene background.
7. Only then assess host target evidence, druggability and known compound interactions. Drug signature reversal is hypothesis generation, not evidence of clinical efficacy.

**Status:** Study selection and analysis design only. No molecular expression data have been downloaded or analysed, and no molecular results are claimed.

## Reproducible starting point

Use [GEO2R](https://www.ncbi.nlm.nih.gov/geo/geo2r/) on GSE19439 for a first QC inspection, or download the processed series matrix from GEO. Record exact sample inclusion/exclusion decisions. The main analysis should use limma rather than a generic t-test for publication.

## Interpretation limits

The 155 Indian chest X-rays are not paired with GEO blood samples. We cannot claim radiogenomic correlations, infer drug response from X-ray attention maps, or link specific image features to expression of specific genes.

Reference: Berry et al., *Nature* (2010), doi:10.1038/nature09247.
