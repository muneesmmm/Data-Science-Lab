library(e1071)
cars = read.csv("cars.csv")
cars_train = cars[,1:4]
cars_test=data.frame(Colour=
+ + "red",Type="SUV",Origin="domestic",Stolen="yes")
cars_test=data.frame(Colour=
+  "red",Type="SUV",Origin="domestic",Stolen="yes")
classifier_cl <- naiveBayes(cars_train,cars$Stolen)
classifier_cl

Naive Bayes Classifier for Discrete Predictors

Call:
naiveBayes.default(x = cars_train, y = cars$Stolen)

A-priori probabilities:
cars$Stolen
 no yes 
0.5 0.5 

Conditional probabilities:
           Example
cars$Stolen [,1]     [,2]
        no   5.8 2.863564
        yes  5.2 3.492850

           Colour
cars$Stolen red yellow
        no  0.4    0.6
        yes 0.6    0.4

           Type
cars$Stolen sports SUV
        no     0.4 0.6
        yes    0.8 0.2

           Origin
cars$Stolen domestic imported
        no       0.6      0.4
        yes      0.4      0.6

