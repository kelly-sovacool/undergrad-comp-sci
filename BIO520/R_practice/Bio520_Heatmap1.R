setwd("~/Dropbox/BIO520/project/R_practice/")
library(tidyverse)
library(pheatmap) 
library(RColorBrewer)

data <- as.matrix(read.table("postFC.filtered.txt", row.names = 1, header = T))
#pheatmap(data, cluster_cols=F)

# a way of generting scaled values and writing them to a new matrix
datascaled <- as.matrix(t(scale(t(data), center = T, scale = T)))

#View(datascaled)

#filter out undefined values and write it to a new matrix
datascalefilt <- datascaled[complete.cases(datascaled),]

View(datascalefilt)


# make a heatmap
#pheatmap(datascalefilt, clustering_distance_cols = "euclidean", clustering_distance_rows = "euclidean", border = NA )

# remove messy row names and do a different clustering method 
pheatmap(datascalefilt, color = colorRampPalette(rainbow(3))(1000), show_rownames = T, clustering_method = "ward.D2", cluster_cols = F, clustering_distance_rows = "euclidean", border = NA )

# maybe a useful website for this -- http://www.opiniomics.org/you-probably-dont-understand-heatmaps/

