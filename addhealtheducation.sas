options ps=50 ls=95; 

libname in1 "G:\My Drive\nsmith\addhealth\wave1"; 
libname in4 "G:\My Drive\nsmith\addhealth\wave4"; 
libname in5 "G:\My Drive\nsmith\addhealth\wave5"; 

data new1; set in1.addhealthwave1; 
wave=1;
proc sort; by aid; 

data new4; set in4.addhealthwave4; 
wave=4;
proc sort; by aid; 

data new5; set in5.addhealthwave5; 
wave=5;
proc sort; by aid; 

data end1; merge new1 new4;
proc sort; by aid;

data end2; merge end1 new5;
*parents education wave1;
if (h1rm1=8 or h1rm1=9) or (h1nm4=8 or h1nm4=9) then momcollege=1;
else if h1rm1 le 7 or h1nm4 le 7 then momcollege=2;

if (h1rf1=8 or h1rf1=9) or (h1nf4=8 or h1nf4=9) then dadcollege=1;
else if h1rf1 le 7 or h1nf4 le 7 then dadcollege=2;

if momcollege=1 or dadcollege=1 then parentcollege=1;
else if momcollege ne . or dadcollege ne . then parentcollege=2;
else parentcollege=.;

if momcollege=1 then mompartcollege=.;
else if h1rm1=7 or h1nm4=7 then mompartcollege=1;
else mompartcollege=2;

if dadcollege=1 then mompartcollege=.;
else if h1rf1=7 or h1nf4=7 then dadpartcollege=1;
else dadpartcollege=2;

if mompartcollege=1 or dadpartcollege=1 then ppartcollege=1;
else if mompartcollege ne . or dadpartcollege ne . then ppartcollege=2;

*college degree wave5;
if h5od11 ge 10 then collegedegree=1;
else if h5od11 ne . then collegedegree=0;

*education wave1;
if h1ed9=1 then expelled=1;
else if h1ed9=0 then expelled=2;

if h1ed11=1 then english=4;
else if h1ed11=2 then english=3;
else if h1ed11=3 then english=2;
else if h1ed11=4 then english=1;

if h1ed12=1 then math=4;
else if h1ed12=2 then math=3;
else if h1ed12=3 then math=2;
else if h1ed12=4 then math=1;

if h1ed13=1 then socialst=4;
else if h1ed13=2 then socialst=3;
else if h1ed13=3 then socialst=2;
else if h1ed13=4 then socialst=1;

if h1ed14=1 then science=4;
else if h1ed14=2 then science=3;
else if h1ed14=3 then science=2;
else if h1ed14=4 then science=1;

gpa=mean (of english math socialst science);

if h1ed15 ge 6 then teachertrouble=.;
else if h1ed15 ge 2 then teachertrouble=1;
else if h1ed15 le 1 then teachertrouble=2;

if h1ed16 ge 6 then attentiontrouble=.;
else if h1ed16 ge 2 then attentiontrouble=1;
else if h1ed16 le 1 then attentiontrouble=2;

if h1ed17 ge 6 then hwtrouble=.;
else if h1ed17 ge 2 then hwtrouble=1;
else if h1ed17 le 1 then hwtrouble=2;

if h1ed18 ge 6 then socialtrouble=.;
else if h1ed18 ge 2 then socialtrouble=1;
else if h1ed18 le 1 then socialtrouble=2;

if h1ed19 ge 6 then closeschool=.;
else if h1ed19=1 or h1ed19=2 then closeschool=1;
else if h1ed19 ge 3 then closeschool=2;

if h1ed20 ge 6 then partschool=.;
else if h1ed20=1 or h1ed20=2 then partschool=1;
else if h1ed20 ge 3 then partschool=2;

if h1ed21 ge 6 then prejschool=.;
else if h1ed21=1 or h1ed21=2 then prejschool=1;
else if h1ed21 ge 3 then prejschool=2;

if h1ed22 ge 6 then happyschool=.;
else if h1ed22=1 or h1ed22=2 then happyschool=1;
else if h1ed22 ge 3 then happyschool=2;

if h1ed23 ge 6 then fairschool=.;
else if h1ed23=1 or h1ed23=2 then fairschool=1;
else if h1ed23 ge 3 then fairschool=2;

if h1ed24 ge 6 then safeschool=.;
else if h1ed24=1 or h1ed24=2 then safeschool=1;
else if h1ed24 ge 3 then safeschool=2;

if h1gi20 ge 96 then h1gi20=.;
rename h1gi20=wave1grade;

*gender;
rename h5od2a=gender; 

*race;
if h5od4a=1 then white=1;
else if h5od4a ne . then white=0;

if h5od4b=1 then black=1;
else if h5od4b ne . then black=0;

if h5od4c=1 then hispanic=1;
else if h5od4c ne . then hispanic=0;

if h5od4d=1 then asian=1;
else if h5od4d ne . then asian=0;

if hispanic=1 then race=1;
else if black=1 then race=2;
else if asian=1 then race=3;
else if white=1 then race=4;
else race=.;

*household income proxy;
if h5ec2=1 then hhincome=2500;
else if h5ec2=2 then hhincome=7500;
else if h5ec2=3 then hhincome=12500;
else if h5ec2=4 then hhincome=17500;
else if h5ec2=5 then hhincome=22500;
else if h5ec2=6 then hhincome=27500;
else if h5ec2=7 then hhincome=35000;
else if h5ec2=8 then hhincome=45000;
else if h5ec2=9 then hhincome=62500;
else if h5ec2=10 then hhincome=87500;
else if h5ec2=11 then hhincome=125000;
else if h5ec2=12 then hhincome=175000;
else if h5ec2=13 then hhincome=250000;

*subset to wave5 participants; 
if wave=5;
proc sort; by aid;

*descriptive analyses by collegedegree;
data descriptives; set end2;
proc sort; by aid;

proc freq; tables white black hispanic asian race gpa H5OD11 collegedegree parentcollege gender h1nm4 momcollege 
h1nf4 dadcollege H5hr1 H5LM10 H5EC1 H5EC2 hhincome H5EC9 teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool wave1grade; 

proc freq; tables (race gender parentcollege expelled teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool)*collegedegree /chisq;

proc anova; class collegedegree;
model wave1grade gpa=collegedegree; 
means collegedegree;

*multiple linear regression;
data regression; set end2; 
proc sort; by aid;

proc logistic data=regression; class race gender parentcollege teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool;
model collegedegree(event='1')=race gender parentcollege gpa expelled teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool wave1grade; 
run; 

*stepwise selection regression;
data stepwise; set end2;  
proc sort; by aid;

proc sort; by gender; 
proc logistic data=stepwise outest=betas covout;
class race gender parentcollege teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool;
model collegedegree(event='1')=race gender parentcollege gpa expelled teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool wave1grade
                / selection=stepwise
                  slentry=0.10
                  slstay=0.05
                  details
                  lackfit; by gender; 
   output out=pred p=phat lower=lcl upper=ucl
          predprob=(individual crossvalidate);
   ods output Association=Association;
run;


*lasso regression;
data lasso; set end2; 
*if cmiss(of _all_) then delete;  

ods graphics on;

proc surveyselect data=lasso out=traintest seed=123 samprate=0.7 method=srs outall;

proc sort; by gender; 
proc glmselect data=traintest plots=all seed=123; 
*partition ROLE=selected (train='1' test='0');
model collegedegree=race gender parentcollege gpa expelled teachertrouble attentiontrouble hwtrouble socialtrouble
closeschool partschool prejschool happyschool fairschool safeschool wave1grade /selection=lar (choose=cv stop=none)
cvmethod=random(10); by gender; 
run; 


run; 

