# Host blood transcriptomics and computational drug repurposing in tuberculosis

## Study aim
Exploratory identification of reproducible host blood-expression changes associated with active versus latent tuberculosis (TB), followed by functional analysis, STRING network analysis, LINCS transcriptional-reversal screening and preliminary compound assessment. This is **not** a clinical treatment recommendation or a validated drug-discovery pipeline.

The chest X-ray classification pilot in the repository is **separate** and uses unpaired data.

## Cohorts and differential expression
- Discovery: [GSE19439](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19439), 42 samples (13 active, 17 latent, 12 healthy).
- Within-study replication: [GSE19442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19442), 51 samples (20 active, 31 latent).
- Both: Illumina HumanHT-12 v3 (GPL6947), part of the same broader original research programme.
- 18,625 representative gene symbols tested using limma. Method A used `asinh(signal/10)`; Method B additionally used within-cohort quantile normalisation. Both used BH FDR control.
- 1,689 genes replicated under A, 2,044 under B, and **1,453** under both (684 upregulated; 769 downregulated). These coefficients are **asinh-scale differences, not log2 fold changes**.
- GO-BP ORA: 576 significant upregulated and 77 downregulated term entries; ontology redundancy and identifier mapping still need review.

## STRING protein association network
- 50 selected GO-supported proteins; 50 mapped to STRING v12.0.
- High-confidence combined score ≥700; 108 edges; 13 connected components; 12 isolated nodes.
- STAT1 was the highest-degree node (degree 14). Other high-degree nodes included CD2, CD3E, IFI35, CD3D and CD28.
- STRING edges include functional associations and do not establish direct physical binding or therapeutic tractability. The network was preselected and hubness is not a validated drug-target score.

## Transcriptomic drug-repurposing screen
1. Rank 1,453 stable genes using a conservative minimum absolute effect across cohort/preprocessing comparisons.
2. Create separate 150-gene active-TB-up and active-TB-down signatures; additional sizes (50, 100, 200) are available for sensitivity checks.
3. Submit signatures to [L2S2](https://l2s2.maayanlab.cloud/) for opposing LINCS perturbation signatures.
4. Filter the exported perturbation table for concentration-labelled chemical treatments and rank by adjusted reverser p-value.
5. Summarise recurrence across experimental signatures and cell lines.
6. Integrate PubChem-resolved RDKit physicochemical descriptors with targeted published pharmacology and safety evidence.

### Important screening limitation
The 10,000-row L2S2 export appeared to be selected by **mimicker** significance even though the interface was sorted by reverser significance. Re-sorting this truncated export by reverser FDR does **not** recover missing reversal hits. Reported hits and recurrence counts are **conditional on the exported subset**, not exhaustive LINCS rankings. Concentration-labelled rows are a proxy for chemical treatments and require perturbation-type verification.

### Screening and ADMET summary
| Metric | Result |
|---|---:|
| Exported L2S2 records | 10,000 |
| Concentration-labelled treatment records | 7,076 |
| Reversal-significant concentration-labelled records (adjusted p < 0.05) | 715 |
| Distinct perturbations in this subset | 599 |
| Compounds/signatures represented across ≥3 cell lines in recurrence review | 16 |
| Compounds in physicochemical audit | 30 |
| Structures resolved through PubChem | 28 |
| Unresolved LINCS identifiers | 2 |
| Resolved compounds with zero Lipinski violations | 20 |
| Compounds in focused literature/safety review | 6 |

The two unresolved identifiers are `BRD-K11614492` and `BRD-K22969690`. All resolved chemical identities require manual confirmation. Lipinski compliance does **not** establish ADMET, efficacy or safety.

### Focused candidate interpretation
| Compound | Exploratory interpretation |
|---|---|
| Zileuton | TB-relevant preclinical rationale; hepatotoxicity is a significant concern alongside TB therapy |
| Vorinostat | TB macrophage mechanistic evidence; haematological and thromboembolic safety concerns |
| Etodolac | NSAID class-level TB rationale, but compound-specific efficacy not established |
| Olaparib | No established TB efficacy; rifampicin markedly reduces exposure |
| Selumetinib | No established TB efficacy; rifampicin interaction and organ toxicity concerns |
| Bortezomib | Proteasome-inhibition reversal signal; substantial neuropathy and cytopenia risks |

These are **research hypotheses**, not a ranking of clinically usable TB drugs.

## Files and provenance
- [Audit summary](audit_summary.csv): counts for 30-compound descriptor/literature review.
- [Screen summary](screen_summary.csv): exported LINCS screen counts.
- [Focused compound evidence](focused_six_compound_evidence.csv): selected TB-relevant mechanistic and label concerns with sources.
- [Methods and limitations](METHODS_AND_LIMITATIONS.md): reproducibility notes and outstanding validation.
- The full compound-level screening CSVs, detailed descriptor matrices, R scripts and raw GEO data are **not yet committed**. Do not interpret this documentation as a fully reproducible data archive.

## Required validation before manuscript submission
- Review probe annotation, detection filtering, transformation-scale sensitivity, cell-composition confounding and gene-mapping losses.
- Validate the disease signature in a genuinely independent cohort (GSE37250 is a candidate; metadata and groups need verification).
- Repeat the reversal search with an unbiased reverser-oriented export and assess 50/100/150/200-gene sensitivity.
- Confirm chemical identity, drug concentration, cell-line relevance, dose dependence and direction of modulation.
- Evaluate hepatotoxicity, myelosuppression, immunomodulation, drug-drug interactions with TB regimens and available experimental TB evidence.
- Do not interpret whole-blood expression reversal as proof of therapeutic benefit.

## Key sources
- Berry et al., *Nature* (2010): https://doi.org/10.1038/nature09247
- L2S2: https://l2s2.maayanlab.cloud/
- LINCS GSE92742: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742
- Zileuton and NSAID TB mechanisms: https://pmc.ncbi.nlm.nih.gov/articles/PMC11987284/
- Vorinostat macrophage study: https://pmc.ncbi.nlm.nih.gov/articles/PMC7390906/
- NSAIDs review: https://pmc.ncbi.nlm.nih.gov/articles/PMC5492311/
- Zileuton prescribing information: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f7573809-7741-04c9-e053-6294a90ab193
- Olaparib prescribing information: https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=741ff3e3-dc1a-45a6-84e5-2481b27131aa
