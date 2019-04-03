#packages from the main R repository (CRAN) can be installed like this:
install.packages("ggplot2")

#another important package repository is called Bioconductor (which itself needs to be installed):
## try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
biocLite()

#For installing individal packages:
source("https://bioconductor.org/biocLite.R")
biocLite("DESeq2")


#below is a more fancy way that checks if the package is already installed on your computer before installing it if needed
if (!require(tidyverse)) {
  install.packages("tidyverse")
  require(tidyverse)
}

#### install gplots (heatmap)
if (!require(gplots)) {
  install.packages("gplots")
  require(gplots)
}

if (!require(pheatmap)) {
  install.packages("pheatmap")
  require(pheatmap)
}

if (!require(pvclust)) {
  install.packages("pvclust")
  require(pvclust)
}

if (!require(gridExtra)) {
  install.packages("gridExtra")
  require(gridExtra)
}

### install bioconductor as well as the DESeq2 and BiocParallel packages
if (!require(DESeq2)) {
  source("https://bioconductor.org/biocLite.R")
  biocLite()  ### <- this will either install bioconductor or update your current packages.  
  biocLite("DESeq2")
  require("DESeq2")
}

if (!require(BiocParallel)) {
  source("https://bioconductor.org/biocLite.R")
  biocLite("BiocParallel")
  require("BiocParallel")
}
