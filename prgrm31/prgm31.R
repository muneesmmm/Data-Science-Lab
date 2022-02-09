heart<-read.csv("heart.csv")
heart_train<-heart[1:495,]
heart_test<-heart[496:498,]
heart_model<-lm(heart.disease~biking+smoking,data=heart_train)
heart-model
heart_model
heart_pred<-predict(heart_model,heart_test)
heart_pred