
R version 4.1.2 (2021-11-01) -- "Bird Hippie"
Copyright (C) 2021 The R Foundation for Statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> setwd("D:\Documents\Ajnas\Semester - 3\Lab\DATA SCIENCE LAB\28")
> library(C50)
> library(gmodels)
> cricket<-read.csv("cricket.csv")
> cricket_train<-cricket[1:12,-5]
> cricket_test<-cricket[13:15,-5]
> cricket_train_labels<-cricket[1:12,5]
> cricket_test_labels<-cricket[13:15,5]
> cricket_model<-C5.0(cricket_train,as.factor(cricket_train_labels))
> cricket_model

Call:
C5.0.default(x = cricket_train, y
 = as.factor(cricket_train_labels))

Classification Tree
Number of samples: 12 
Number of predictors: 4 

Tree size: 3 

Non-standard options: attempt to group attributes

> summary(cricket_model)

Call:
C5.0.default(x = cricket_train, y
 = as.factor(cricket_train_labels))


C5.0 [Release 2.07 GPL Edition]         Fri Feb 04 11:16:40 2022
-------------------------------

Class specified by attribute `outcome'

Read 12 cases (5 attributes) from undefined.data

Decision tree:

Outlook in {Overcast,Sunny}: Yes (7/1)
Outlook = Rainy:
:...Humidity = High: No (3)
    Humidity = Normal: Yes (2)


Evaluation on training data (12 cases):

            Decision Tree   
          ----------------  
          Size      Errors  

             3    1( 8.3%)   <<


           (a)   (b)    <-classified as
          ----  ----
             3     1    (a): class No
                   8    (b): class Yes


        Attribute usage:

        100.00% Outlook
         41.67% Humidity


Time: 0.0 secs

> cricket_pred<-predict(cricket_model,cricket_test)
> cricket_pred
[1] Yes Yes Yes
Levels: No Yes
> CrossTable(cricket_test_labels,cricket_pred,prop.chisq=FALSE)

 
   Cell Contents
|-------------------------|
|                       N |
|         N / Table Total |
|-------------------------|

 
Total Observations in Table:  2 

 
                    | cricket_pred 
cricket_test_labels |       Yes | Row Total | 
--------------------|-----------|-----------|
                 No |         1 |         1 | 
                    |     0.500 |           | 
--------------------|-----------|-----------|
                Yes |         1 |         1 | 
                    |     0.500 |           | 
--------------------|-----------|-----------|
       Column Total |         2 |         2 | 
--------------------|-----------|-----------|

 
> 
