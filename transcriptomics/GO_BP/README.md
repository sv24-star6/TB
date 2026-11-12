# Gene Ontology Biological Process Enrichment: Active vs Latent TB

## Analysis status
GO Biological Process over-representation analysis has been **executed** for the stable, cross-cohort differential-expression gene lists. Results were supplied as `GO_BP_Upregulated.csv` and `GO_BP_Downregulated.csv` and checked against their reported counts and adjusted p-values. These full CSV files and figures are **not yet committed to this repository**.

## Inputs and methods
- Source: stable active-versus-latent TB genes from GSE19439 (discovery) and GSE19442 (validation).
- Original stable gene set: 1,453 genes (684 upregulated; 769 downregulated).
- GO Biological Process enrichment performed separately for each direction using `clusterProfiler::enrichGO` with human `org.Hs.eg.db` annotation.
- Benjamini-Hochberg adjusted p-value threshold < 0.05.
- Successfully mapped background: **13,925 genes**. Enrichment input sizes: **563 upregulated** and **596 downregulated**.
- This represents a mapping reduction from the 18,625 tested gene symbols; unmapped symbols require audit.

## Results
| Direction | Significant GO BP terms | Mapped input genes |
|---|---:|---:|
| Upregulated | **576** | 563 |
| Downregulated | **77** | 596 |
| Total term entries | **653** | — |

The total counts term entries across both lists; many GO terms overlap in genes and biological meaning.

### Selected upregulated GO terms
| GO BP term | Count | BH-adjusted p |
|---|---:|---:|
| Regulation of response to biotic stimulus | 90 | 5.52e-31 |
| Response to virus | 75 | 1.20e-30 |
| Activation of immune response | 87 | 3.85e-29 |
| Positive regulation of defense response | 83 | 1.55e-28 |
| Regulation of innate immune response | 78 | 3.01e-28 |
| Defense response to virus | 63 | 3.44e-28 |
| Response to bacterium | 78 | 2.58e-23 |
| Pattern recognition receptor signaling | 54 | 1.66e-22 |

### Selected downregulated GO terms
| GO BP term | Count | BH-adjusted p |
|---|---:|---:|
| Cytoplasmic translation | 42 | 3.08e-16 |
| Antigen receptor-mediated signaling pathway | 39 | 1.31e-15 |
| Negative regulation of myoblast fusion | 20 | 1.25e-12 |
| Ribonucleoprotein complex biogenesis | 51 | 2.50e-11 |
| T cell receptor signaling pathway | 27 | 8.12e-10 |
| Ribosome biogenesis | 37 | 2.95e-09 |
| T cell activation | 53 | 8.62e-09 |
| Lymphocyte differentiation | 41 | 1.22e-07 |

## Interpretation
Upregulated transcripts are enriched for innate immune, interferon-associated, pathogen recognition and host-defense annotations. Downregulated transcripts are enriched for antigen-receptor/T-cell signalling and translation/ribosome-related processes. This is **gene-set over-representation**, not a direct measurement of pathway activation or inhibition.

A notable annotation caveat: the 20 genes driving the `negative regulation of myoblast fusion` term are ribosomal proteins, so this does not independently demonstrate altered muscle-cell fusion. GO term redundancy and blood-cell composition must be considered. Some T-cell-related GO terms contain genes from both expression directions, so uniform T-cell suppression cannot be inferred.

See [the parent transcriptomics overview](../README.md) and [sensitivity analysis](../sensitivity_2026/README.md).
