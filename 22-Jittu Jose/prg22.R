std=read.csv("survey.csv")
std
ramu=data.frame(X=5,Y=7)
ramu
std1=std[,1:2]
library(class)
pred=knn(std1,ramu,std$Z,k=3]
pred
