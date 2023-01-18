# Code-for-Resume

# Educational and Demographic Predictors of Earning a College Degree
# This project is designed 1) to evaluate which educational and demographic indicators measured during adolescence predict having earned a college degree by middle adulthood; and 2) to showcase my programming skills across modern statistical platforms (R, SAS, and Python) and data visualization packages.
# Products: 
# R Script and Results
# SAS Script and Results
# Python Script and Results
Data visualization in Excel, Tableau, R, SAS, and Python
Data: Data were drawn from wave 1 and wave 5 of The National Longitudinal Study of Adolescent to Adult Health (AddHealth), a longitudinal study of a nationally representative sample of adolescents who were in grades 7-12 during the 1994-95 school year and followed over 5 waves, most recently in 2016-18. The sample included 4191 individuals who participated in wave 1 and wave 5 of the study and who were part of the publicly available portion of the study sample. https://addhealth.cpc.unc.edu/data/ 
Predictors: race (mutually exclusive groupings including Hispanic, Black, Asian and White=reference group), gender (male/female), whether at least 1 parent had completed college (yes/no), grade point average at wave 1, whether ever expelled from school (yes/no), getting in trouble with teachers (yes/no), trouble paying attention in school (yes/no), trouble getting homework done (yes/no), trouble getting along with other students (yes/no), feeling close to people at school (yes/no), feeling part of school (yes/no), having prejudiced students at school (yes/no), being happy at school (yes/no), teachers treating students fairly (yes/no), feeling safe at school (yes/no), whether mom would be disappointed if participant did not attend college (yes/no), whether data would be disappointed if participant did not attend college (yes/no), number of days in past week at least one parent was in the room when participant ate their evening meal (0 to 7), grade level at wave 1 (7 through 12). 
Outcome: Completion of a college degree (yes/no)
Analyses: Following data management and an examination of resulting frequency tables, three multivariate regression models were run: 
o	Logistic regression controlling for all predictors simultaneously
o	Stepwise logistic regression with forward selection retaining only those predictors associated with the outcome at p.<.05. 
o	Lasso regression a machine learning algorithm that handles both variable selection and regularization. 

Results: The results of regression models showed that race and gender are the only consistent predictors of having earned a college degree by mid adulthood. None of the parental or educational indicators were either significant (multiple regression) or retained (stepwise and lasso regression) in the final models. 

Females were significantly more likely to earn a college degree than males (OR=1.6, CI 1.32- 1.83). Hispanic (OR=0.5, CU 0.38- 0.69) and Black (OR=0.8, CI 0.62-0.94) participants were less likely than those who were White to earn a college degree, while Asian participants were more likely to have earned a college degree compared to White participants (OR=1.7, CI 1.08- 2.63).

To evaluate whether gender moderates the association between race and having earned a college degree, Chi Square Tests of Independence were run with race by gender predicting college degree status. Post hoc paired comparisons used a Bonferroni adjustment of p<.001. Figure 1 presents the association between race and college degree stratified by gender. Both male and female participants who were Hispanic or Black earned a college degree at lower rates than Asian participants of both genders and White females. Black females earned a college degree at a higher rate than Black and Hispanic males. 

Figure 1. The Association between Race and Earning a College Degree by Gender.
 
Next, possible parental and educational predictors of college degree status were evaluated using the three regression methods for each race/gender subgroup individually. The small sample size available for both Asian males and females yielded unstable estimates. For the remaining race/gender groups, parental and educational indicators were not found to consistently predict college degree status across the three types of regression models. The exception were the models examining White males. For this group, logistic regression, stepwise regression, and lasso regression showed that having at least one parent that completed college and feeling close to their school during adolescence was associated with lower rates of earning a college degree.  

