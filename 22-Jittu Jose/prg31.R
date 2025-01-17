library(C50)
library(gmodels)
heart<-read.csv("heart.csv")
heart_train<-heart[1:420,]
heart_test<-heart[421:498,]
heart_model<-lm(heart.disease~biking+smoking,data=heart_train)
heart_model
summary(heart_model)
heart_pred<-predict(heart_model,heart_test)
heart_pred
