suppressPackageStartupMessages(library(knitr))
suppressPackageStartupMessages(library(caret))
suppressPackageStartupMessages(library(gmodels))
suppressPackageStartupMessages(library(lattice))
suppressPackageStartupMessages(library(ggplot2))
suppressPackageStartupMessages(library(gridExtra))
suppressPackageStartupMessages(library(Kmisc))
suppressPackageStartupMessages(library(ROCR))
suppressPackageStartupMessages(library(corrplot))

set.seed(1023)
weather_data <- read.csv(url("trainset.csv"), header = TRUE, sep = ",", stringsAsFactors = TRUE)
kable(head(weather_data))
