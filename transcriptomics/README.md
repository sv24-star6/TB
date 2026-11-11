# Planned Analysis: Host Transcriptomics and Drug-Target Prioritization in Tuberculosis

## Status

**Planned, not executed.** This folder records the proposed molecular research workflow. No gene-expression analysis, pathway enrichment, drug repurposing or molecular docking results have been generated for this project.

## Scientific objective

The proposed study will investigate reproducible host transcriptional signatures associated with active tuberculosis and assess whether the resulting evidence supports prioritization of host-directed therapeutic targets.

The molecular component will use **independent public cohorts**. The chest X-rays used in the imaging pilot are not linked to these samples, so patient-level radiogenomic correlation will not be possible.

## Candidate data sources

- [GSE19491](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19491): a SuperSeries comprising distinct study cohorts, rather than one homogeneous case-control dataset.
- [GSE19439](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19439): proposed discovery cohort, subject to verification of sample-level metadata and clinical labels.
- [GSE19442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19442): potential validation cohort, subject to verification of independence, platform and clinical labels.

Cohorts will not be pooled indiscriminately. Their eligibility will be assessed before analysis.

## Proposed methodology

1. **Data audit:** Review sample identifiers, TB status, controls, study design, time points, platform and possible cohort overlap.
2. **Quality control:** Inspect expression distributions, normalization, missing values and sample-level outliers.
3. **Differential expression:** Compare active TB with appropriate controls using a platform-appropriate statistical design, such as limma for microarray data.
4. **Multiple-testing correction:** Apply Benjamini–Hochberg false discovery rate adjustment and map probes using the relevant platform annotation.
5. **External validation:** Assess effect-direction concordance and reproducibility in an independent cohort.
6. **Functional interpretation:** Evaluate replicated genes using GO and Reactome enrichment with a suitable gene background.
7. **Target prioritization:** Examine disease relevance, druggability, known interactions and supporting experimental evidence.
8. **Exploratory drug repurposing:** Consider drug-signature reversal only if data quality and target evidence justify it. Predicted compounds will not be presented as validated TB therapies.

## Reproducibility requirements

The completed analysis will document accession versions, sample inclusion/exclusion criteria, preprocessing, statistical models, software versions, gene identifiers and validation strategy. Expression matrices, metadata, code and actual outputs will be added only when the corresponding work has been performed and their redistribution is permitted.

## Interpretation

Findings from independent imaging and blood transcriptomic cohorts may provide complementary information about TB, but cannot establish patient-level associations between chest X-ray features, molecular pathways or drug response.

## Reference

Berry et al. *Nature* (2010). DOI: [10.1038/nature09247](https://doi.org/10.1038/nature09247).
