# Methods and limitations

## Study scope
The transcriptomics and drug-repurposing analysis is separate from the unpaired chest X-ray pilot.

## Differential-expression evidence
GSE19439 and GSE19442 use GPL6947 and belong to the same original research programme. The two asinh-based preprocessing strategies are sensitivity checks on the same measurements, not independent biological experiments. Probe mapping and GO universe audit remain open. Limma effect estimates are on the asinh scale.

## Signature generation
Active versus latent TB: 1,453 stable genes (684 up, 769 down), with top-150 genes in each direction used as L2S2 query inputs. The top-N selection is heuristic and should be tested at N=50,100,150,200. Whole-blood signals can reflect changes in leukocyte composition.

## PPI
STRING v12.0, organism 9606, score ≥700, 50 selected genes, 108 edges, 13 components and 12 isolates. Associations are not necessarily physical interactions. Degree centrality is not evidence of therapeutic efficacy.

## L2S2
An exported 10,000-row table was sorted in Python by adjusted reverser p-value. The original export appeared limited by mimicker significance; thus rankings are conditional on the available subset. 7,076 rows were concentration-labelled and 715 of those had reverser adjusted p <0.05. Concentration alone is not definitive perturbation-type annotation. Recurrence across signatures or cell lines is descriptive, not independent validation.

## Chemical structures and descriptors
30 compounds were assessed, 28 resolved through PubChem, and 2 LINCS BRD IDs unresolved. RDKit computed MW, cLogP, TPSA, HBD, HBA, rotatable bonds and Lipinski violations. 20/28 resolved structures had zero Lipinski violations. These descriptors are not measured absorption, distribution, metabolism, excretion or toxicity. Manually confirm compound identity and stereochemistry before interpretation.

## Evidence review
Focused source-backed review of bortezomib, selumetinib, olaparib, vorinostat, zileuton and etodolac. The remaining 24 were not fully reviewed and must not be considered safe by default. Relevant clinical labels and TB-specific studies should be rechecked at manuscript submission.

## Outstanding work
1. Independent external cohort validation.
2. Unbiased reversal-oriented export and sensitivity analyses.
3. Verify LINCS perturbation types, chemical identities, cell lines, dose and duration.
4. Review interactions with rifampicin and other TB drugs, immunosuppression and liver toxicity.
5. Preserve exact raw inputs, code, software versions and provenance for manuscript reproducibility.

No docking, machine-learning classification, wet-lab TB experiment or quantitative ADMET model was performed.
