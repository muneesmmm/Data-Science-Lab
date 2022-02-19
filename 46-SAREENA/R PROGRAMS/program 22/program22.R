survey=read.csv("survey.csv")
survey
hakeem=data.frame(X=7,Y=9,Z="Outstanding")
hakeem
survey1=survey[,1:2]
hakeem1=hakeem[,1:2]
library (class)
identify=knn(survey1,hakeem1,survey$Z,k=1)
identify
