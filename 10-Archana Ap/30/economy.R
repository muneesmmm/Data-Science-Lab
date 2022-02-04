economy<-read.csv("economy.csv")
economy_train<-economy[1:20,]
economy_test<-economy[21:24,]
economy_model<-lm(Stock_Index_Price~Interest_Rate+Unemployment_Rate,data=economy_train)
economy_model
economy_pred<-predict(economy-model,economy_test)
economy_pred<-predict(economy_model,economy_test)
economy_pred