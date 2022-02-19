> library(C50)
> library(gmodels)
> heart<-read.csv("heart.csv")
> heart_train<-heart[1:420]
Error in `[.data.frame`(heart, 1:420) : undefined columns selected
> heart_train<-heart[1:420,]
> heart_test<-heart[421:498,]
> heart_model<-lm(heart.disease~biking+smoking,data=heart_train)
> heart_model

Call:
lm(formula = heart.disease ~ biking + smoking, data = heart_train)

Coefficients:
(Intercept)       biking      smoking  
    15.0552      -0.2016       0.1774  

> summary(heart_model)

Call:
lm(formula = heart.disease ~ biking + smoking, data = heart_train)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.1221 -0.4569  0.0334  0.4456  1.9811 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 15.055175   0.088661  169.81   <2e-16 ***
biking      -0.201647   0.001516 -133.03   <2e-16 ***
smoking      0.177442   0.003902   45.47   <2e-16 ***
---
Signif. codes:  
0 �***� 0.001 �**� 0.01 �*� 0.05 �.� 0.1 � � 1

Residual standard error: 0.6644 on 417 degrees of freedom
Multiple R-squared:  0.9793,    Adjusted R-squared:  0.9792 
F-statistic:  9840 on 2 and 417 DF,  p-value: < 2.2e-16

> heart_pred<-predict(heart_model,heart_test)
> heart_pred
       421        422        423        424        425 
13.3774446 12.6985699  3.9958593  7.0121683 13.4051861 
       426        427        428        429        430 
16.1087822  4.0466358  3.0950353  9.5162276 14.7039457 
       431        432        433        434        435 
 7.3880164  4.1509370 16.0341025  9.1933013  9.4575109 
       436        437        438        439        440 
 6.2651892 13.3090206 12.5701883  3.9573294 12.1201868 
       441        442        443        444        445 
 1.7418361  8.5177092 13.4097176 14.9606310 15.9272397 
       446        447        448        449        450 
13.1673141 11.4843933 12.1323521  4.9672551 13.7098662 
       451        452        453        454        455 
14.6115890  0.9610718 15.5864054  4.0983718 12.2208804 
       456        457        458        459        460 
 6.6454748  5.2706808  5.1904478  7.2096316 10.1722365 
       461        462        463        464        465 
 2.9286533 13.3225914  9.5338093  0.2778315  8.8929403 
       466        467        468        469        470 
 7.0496788  4.0268000  7.1359808 17.4481298 17.2344133 
       471        472        473        474        475 
 4.2882469  8.7632897  4.7158973 12.2669619 11.9266099 
       476        477        478        479        480 
11.2827493  6.7014717 12.8616927 18.9772920 18.7863829 
       481        482        483        484        485 
 5.1872241  9.5567433 10.2248055  6.4858037 10.6556562 
       486        487        488        489        490 
 8.0957206 14.0745090  5.5651225  6.7527590  3.7917007 
       491        492        493        494        495 
 5.8743445  3.0356717 12.0490795 10.3353206  9.7561592 
       496        497        498 
14.5254259 10.1966343 13.0390695 
> 
