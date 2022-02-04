# Loads e1071 package containing naiveBayes
library(e1071)
# Read the csv file into a data frame
cars = read.csv("cars.csv")
#Training Data and Test Data
cars_train = cars[,1:4]
cars_test = data.frame(Color="red",Type="SUV",Origin="domestic",Stolen="yes")
#Naive Bayes Classification
classifier_cl <- naiveBayes(cars_train,cars$Stolen)
# This will print classical and conditional probabilities
classifier_cl
# Predicting on test data
cars_test_pred <- predict(classifier_cl, cars_test)
cat("Prediction of Flu:\n")
cars_test_pred