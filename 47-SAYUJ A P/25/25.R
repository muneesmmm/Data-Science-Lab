print(getwd())
setwd("/Users/mes27/Desktop/say47/25")
library(e1071)
cars=read.csv("cars.csv")
cars_train=cars[,1:4]
cars_test=data.frame(Colour="red",Type="SUV",Origin="domestic",Stolen="yes")
classifier_cl <- naiveBayes(cars_train,cars$Stolen)
classifier_cl
carss_test_pred <- predict(classifier_cl, cars_test)
cat("Prediction of Stolen or not:\n")
carss_test_pred
