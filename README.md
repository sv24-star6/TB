# Tuberculosis Research: Chest X-ray Classification and Host Blood Transcriptomics

This repository contains two **separate, exploratory research components**: (1) a chest X-ray classification pilot and (2) whole-blood transcriptomics with host-directed drug-repurposing hypotheses. Imaging and transcriptomics samples are **not patient-matched**.

## Chest X-ray pilot
155 labelled chest X-rays (78 TB; 77 non-TB), with five-fold stratified image-level cross-validation. The handcrafted-features logistic regression model achieved 74.2% accuracy and AUROC 0.848; a three-layer CNN achieved 63.9% accuracy and AUROC 0.704. Patient-level independence was not confirmed. See [imaging model comparison](results/model_comparison.json). Original images are not redistributed.

To reproduce the imaging pilot, obtain the provider's dataset as `dataset.zip`, run `pip install -r requirements.txt`, then `python run_pilot.py`, `python run_cnn.py`, and `python compare_models.py`.

## Blood transcriptomics
- [GSE19439](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19439): 42 samples, including 13 active TB, 17 latent TB, 12 healthy controls.
- [GSE19442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19442): 51 samples, including 20 active and 31 latent TB.
- Both use GPL6947 and originate from the same broader research programme; replication is not fully independent study-level validation.
- Limma tested 18,625 representative genes under two asinh-based preprocessing methods; 1,453 genes replicated under both methods (684 up, 769 down).
- GO-BP enrichment found 576 significant upregulated and 77 downregulated term entries.
- STRING network of 50 selected GO-supported proteins (score ≥700): 108 edges, 13 components and 12 isolates.

See [transcriptomics methods](transcriptomics/README.md) and [GO-BP analysis](transcriptomics/GO_BP/README.md).

## Drug-repurposing and ADMET extension
A 150-up/150-down active-TB signature was screened using [L2S2](https://l2s2.maayanlab.cloud/) LINCS transcriptional reversal. The 10,000-row exported subset contained 7,076 concentration-labelled treatment rows, 715 with adjusted reversal p <0.05. The export was apparently truncated by **mimicker** rather than reverser significance, so these are **not exhaustive LINCS rankings**.

A 30-compound chemical-property audit resolved 28 PubChem structures, of which 20 had zero Lipinski violations. Six compounds were reviewed for TB-relevant evidence and selected safety concerns. **No candidate is clinically validated for TB.**

**[Drug-repurposing methods, results, evidence tables and limitations](transcriptomics/drug_repurposing/README.md)**

## Final conclusion and project status

**Status: Analysis concluded at the exploratory computational stage (November 2026). No further analyses are planned for this repository version.**

Across the two related GEO cohorts and two preprocessing approaches, 1,453 active-versus-latent TB-associated genes showed consistent direction and statistical support. Functional enrichment and a selected STRING network highlighted immune-response patterns, while a LINCS/L2S2 screen identified transcriptional reversal signals in an exported subset. Physicochemical profiling resolved 28 of 30 shortlisted structures; targeted literature review identified mechanistic interest in zileuton and vorinostat, alongside important safety and drug-interaction concerns across candidates.

**Overall conclusion:** This work provides a descriptive, hypothesis-generating computational assessment of TB host-response signatures and possible host-directed repurposing leads. It does **not** establish independent study-level validation, comprehensive LINCS rankings, actual ADMET performance, anti-TB activity, or clinical suitability. The study is intentionally closed at this stage; any future external validation or experiments would be a separate project.

## Important limitations
Whole-blood transcriptional signals may reflect cell-composition changes. Asinh-scale coefficients are not log2 fold changes. GEO probe mapping, independent validation, unbiased reversal export, chemical identity checks, TB-drug interactions and experimental confirmation remain necessary. Physicochemical descriptors are not measured ADMET properties. No docking or machine-learning classification was performed for the drug-repurposing extension.

## Reference
Berry et al., *Nature* (2010): https://doi.org/10.1038/nature09247
