#!/usr/bin/env Rscript
suppressPackageStartupMessages(library(GEOquery))
args <- commandArgs(trailingOnly=TRUE)
accession <- if(length(args)>=1) args[1] else 'GSE19439'
sets <- getGEO(accession,GSEMatrix=TRUE,AnnotGPL=FALSE)
if(length(sets)!=1) stop('Multiple platforms detected: inspect each separately.')
eset <- sets[[1]]
dir.create(file.path('transcriptomics','metadata'),recursive=TRUE,showWarnings=FALSE)
p <- pData(eset)
write.csv(p,file.path('transcriptomics','metadata',paste0(accession,'_full_metadata.csv')),row.names=FALSE)
template <- data.frame(geo_accession=sampleNames(eset),group='Exclude',stringsAsFactors=FALSE)
write.csv(template,file.path('transcriptomics','metadata',paste0(accession,'_sample_groups_TEMPLATE.csv')),row.names=FALSE)
cat('Metadata saved. Verify each clinical label before analysis.\n')
