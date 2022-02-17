insurance<-read.csv("insurance.csv")
insurance_train<-insurance[1:1000,]
insurance_test<-insurance[1001:1338,]
insurance<-lm(expenses ~ age+sex+bmi+children+smoker+region,data=insurance_train)
insurance_model<-lm(expenses ~ age+sex+bmi+children+smoker+region,data=insurance_train)
insurance_model
summary(insurance_model)
insurance_pred<-predict(insurance_model,insurance_test)
insurance_pred