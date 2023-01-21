# -*- coding: utf-8 -*-
"""
Spyder Editor

author@nsmith
"""
FILE_LOCATION = 'G:/My Drive/nsmith/addhealth/wave5/mergedaddhealth.sas7bdat'

import pandas
import numpy
import seaborn

dataAH = pandas.read_sas(FILE_LOCATION, encoding='latin-1')
#lower-case all DataFrame column names
dataAH.columns = map(str.lower, dataAH.columns)
#parents education wave1
def momcollege (row) : 
    if row['h1rm1'] == 8 or row['h1rm1'] == 9 or row['h1nm4'] == 8 or row['h1nm4'] == 9 :
        return 1 
    elif row['h1rm1'] <= 7 or row['h1nm4'] <= 7 : 
        return 2
    elif row ['h1rm1'] > 9 or row['h1nm4'] > 9 : 
        return 'NaN'
dataAH['momcollege'] = dataAH.apply(lambda row: momcollege (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c1 = dataAH['momcollege'].value_counts(sort=False)
print (c1)

def dadcollege (row) : 
    if (row['h1rf1'] == 8 or row['h1rf1'] == 9) or (row['h1nf4'] == 8 or row['h1nf4'] == 9) : 
        return 1 
    elif row['h1rf1'] <= 7 or row['h1nf4'] <= 7: 
        return 2
    elif row['h1rf1'] > 9 or row['h1nf4'] > 9:
        return 'NaN'
dataAH['dadcollege'] = dataAH.apply(lambda row: dadcollege (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c2 = dataAH['dadcollege'].value_counts(sort=False)
print (c2)

dataAH['h1wp11']= dataAH['h1wp11'].replace(6, numpy.nan)
dataAH['h1wp11']= dataAH['h1wp11'].replace(7, numpy.nan)
dataAH['h1wp11']= dataAH['h1wp11'].replace(8, numpy.nan)
dataAH.rename(columns={'h1wp11':'momdisappointed'}, inplace=True)

#counts and percentages (i.e. frequency distributions)
c3 = dataAH['momdisappointed'].value_counts(sort=False)
print (c3)

dataAH['h1wp15']= dataAH['h1wp15'].replace(6, numpy.nan)
dataAH['h1wp15']= dataAH['h1wp15'].replace(7, numpy.nan)
dataAH['h1wp15']= dataAH['h1wp15'].replace(8, numpy.nan)
dataAH['h1wp15']= dataAH['h1wp15'].replace(9, numpy.nan)
dataAH.rename(columns={'h1wp15':'daddisappointed'}, inplace=True)

#counts and percentages (i.e. frequency distributions)
c4 = dataAH['daddisappointed'].value_counts(sort=False)
print (c4)

def expelled (row) : 
    if row['h1ed9'] == 1: 
        return 1 
    elif row['h1ed9'] == 0: 
        return 2
dataAH['expelled'] = dataAH.apply(lambda row: expelled (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c5 = dataAH['expelled'].value_counts(sort=False)
print (c5)

def english (row) : 
    if row['h1ed11'] == 1: 
        return 4 
    elif row['h1ed11'] == 2: 
        return 3
    elif row['h1ed11'] == 3: 
        return 2
    elif row['h1ed11'] == 4: 
        return 1
dataAH['english'] = dataAH.apply(lambda row: english (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c6 = dataAH['english'].value_counts(sort=False)
print (c6)

def math (row) : 
    if row['h1ed12'] == 1: 
        return 4 
    elif row['h1ed12'] == 2: 
        return 3
    elif row['h1ed12'] == 3: 
        return 2
    elif row['h1ed12'] == 4: 
        return 1
dataAH['math'] = dataAH.apply(lambda row: math (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c7 = dataAH['math'].value_counts(sort=False)
print (c7)

def socialst (row) : 
    if row['h1ed13'] == 1: 
        return 4 
    elif row['h1ed13'] == 2: 
        return 3
    elif row['h1ed13'] == 3: 
        return 2
    elif row['h1ed13'] == 4: 
        return 1
dataAH['socialst'] = dataAH.apply(lambda row: socialst (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c8 = dataAH['math'].value_counts(sort=False)
print (c8)

def science (row) : 
    if row['h1ed14'] == 1: 
        return 4 
    elif row['h1ed14'] == 2: 
        return 3
    elif row['h1ed14'] == 3: 
        return 2
    elif row['h1ed14'] == 4: 
        return 1
dataAH['science'] = dataAH.apply(lambda row: science (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c9 = dataAH['science'].value_counts(sort=False)
print (c9)

dataAH['gpa'] = dataAH[['english', 'math', 'socialst', 'science']].mean(axis=1)

#counts and percentages (i.e. frequency distributions)
c10 = dataAH['gpa'].value_counts(sort=False)
print (c10)

def teachertrouble (row) : 
    if row['h1ed15'] >= 6: 
        return 'Nan'
    elif row['h1ed15'] <= 1: 
        return 2
    elif row['h1ed15'] >= 2: 
        return 1
dataAH['teachertrouble'] = dataAH.apply(lambda row: teachertrouble (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c11 = dataAH['teachertrouble'].value_counts(sort=False)
print (c11)

def attentiontrouble (row) : 
    if row['h1ed16'] >= 6: 
        return 'Nan'
    elif row['h1ed16'] <= 1: 
        return 2
    elif row['h1ed16'] >= 2: 
        return 1
dataAH['attentiontrouble'] = dataAH.apply(lambda row: attentiontrouble (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c12 = dataAH['attentiontrouble'].value_counts(sort=False)
print (c12)

def hwtrouble (row) : 
    if row['h1ed17'] >= 6: 
        return 'Nan'
    elif row['h1ed17'] <= 1: 
        return 2
    elif row['h1ed17'] >= 2: 
        return 1
dataAH['hwtrouble'] = dataAH.apply(lambda row: hwtrouble (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c13 = dataAH['hwtrouble'].value_counts(sort=False)
print (c13)

def socialtrouble (row) : 
    if row['h1ed18'] >= 6: 
        return 'Nan'
    if row['h1ed18'] <= 1: 
        return 2
    elif row['h1ed18'] >= 2: 
        return 1
dataAH['socialtrouble'] = dataAH.apply(lambda row: socialtrouble (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c14 = dataAH['socialtrouble'].value_counts(sort=False)
print (c14)

def closeschool (row) : 
    if row['h1ed19'] >= 6: 
        return 'Nan'
    elif (row['h1ed19'] == 1 or row['h1ed19'] == 2): 
        return 1
    elif row['h1ed19'] >= 3: 
        return 2
dataAH['closeschool'] = dataAH.apply(lambda row: closeschool (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c15 = dataAH['closeschool'].value_counts(sort=False)
print (c15)

def partschool (row) : 
    if row['h1ed20'] >= 6: 
        return 'Nan'
    elif (row['h1ed20'] == 1 or row['h1ed20'] == 2): 
        return 1
    elif row['h1ed20'] >= 3: 
        return 2
dataAH['partschool'] = dataAH.apply(lambda row: partschool (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c16 = dataAH['partschool'].value_counts(sort=False)
print (c16)

def prejschool (row) : 
    if row['h1ed21'] >= 6: 
        return 'Nan'
    elif (row['h1ed21'] == 1 or row['h1ed21'] == 2): 
        return 1
    elif row['h1ed21'] >= 3: 
        return 2
dataAH['prejschool'] = dataAH.apply(lambda row: prejschool (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c17 = dataAH['prejschool'].value_counts(sort=False)
print (c17)

def happyschool (row) : 
    if row['h1ed22'] >= 6: 
        return 'Nan'
    elif (row['h1ed22'] == 1 or row['h1ed22'] == 2): 
        return 1
    elif row['h1ed22'] >= 3: 
        return 2
dataAH['happyschool'] = dataAH.apply(lambda row: happyschool (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c18 = dataAH['happyschool'].value_counts(sort=False)
print (c18)

def fairschool (row) : 
    if row['h1ed23'] >= 6: 
        return 'Nan'
    elif (row['h1ed23'] == 1 or row['h1ed23'] == 2): 
        return 1
    elif row['h1ed23'] >= 3: 
        return 2
dataAH['fairschool'] = dataAH.apply(lambda row: fairschool (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c19 = dataAH['fairschool'].value_counts(sort=False)
print (c19)

def safeschool (row) : 
    if row['h1ed24'] >= 6: 
        return 'Nan'
    elif (row['h1ed24'] == 1 or row['h1ed24'] == 2): 
        return 1
    elif row['h1ed24'] >= 3: 
        return 2
dataAH['safeschool'] = dataAH.apply(lambda row: safeschool (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c20 = dataAH['safeschool'].value_counts(sort=False)
print (c20)

#dataAH['h1gi20']= dataAH['h1gi20'].replace(96, numpy.nan)
#dataAH['h1gi20']= dataAH['h1gi20'].replace(97, numpy.nan)
#dataAH['h1gi20']= dataAH['h1gi20'].replace(98, numpy.nan)
#dataAH['h1gi20']= dataAH['h1gi20'].replace(99, numpy.nan)
#dataAH.rename(columns={'h1gi20':'wave1grade'}, inplace=True)

#counts and percentages (i.e. frequency distributions)
c21 = dataAH['wave1grade'].value_counts(sort=False)
print (c21)

#dataAH['h1wp8']= dataAH['h1wp8'].replace(96, numpy.nan)
#dataAH['h1wp8']= dataAH['h1wp8'].replace(97, numpy.nan)
#dataAH['h1wp8']= dataAH['h1wp8'].replace(98, numpy.nan)
#dataAH['h1wp8']= dataAH['h1wp8'].replace(99, numpy.nan)
#dataAH.rename(columns={'h1wp8':'parenteat'}, inplace=True)

#counts and percentages (i.e. frequency distributions)
c22 = dataAH['parenteat'].value_counts(sort=False)
print (c22)

#figure out number of NaN for each variable
dataAH.isnull().sum()
dataAH.head(100)

def collegedegree (row) : 
    if row['h5od11'] == 10 or row['h5od11'] == 11 or row['h5od11'] == 12 or row['h5od11'] == 13 \
        or row['h5od11'] == 14 or row['h5od11'] == 15 or row['h5od11'] == 16:
        return 1 
    elif row['h5od11'] == 2 or row['h5od11'] == 3 or row['h5od11'] == 4 or row['h5od11'] == 5 \
        or row['h5od11'] == 6 or row['h5od11'] == 7 or row['h5od11'] == 8 or row['h5od11'] == 9: 
        return 0
dataAH['collegedegree'] = dataAH.apply(lambda row: collegedegree (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c23 = dataAH['collegedegree'].value_counts(sort=False)
print (c23)

#gender
dataAH.rename(columns={'h5od2a':'gender'}, inplace=True)
c24 = dataAH['gender'].value_counts(sort=False)
print (c24)

#race
def white (row) : 
    if row['h5od4a'] == 1: 
        return 1
    elif row['h5od4a'] == 0: 
        return 2
dataAH['white'] = dataAH.apply(lambda row: white (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c25 = dataAH['white'].value_counts(sort=False)
print (c25)

def black (row) : 
    if row['h5od4b'] == 1: 
        return 1
    elif row['h5od4b'] == 0: 
        return 2
dataAH['black'] = dataAH.apply(lambda row: black (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c26 = dataAH['black'].value_counts(sort=False)
print (c26)

def hispanic (row) : 
    if row['h5od4c'] == 1: 
        return 1
    elif row['h5od4c'] == 0: 
        return 2
dataAH['hispanic'] = dataAH.apply(lambda row: hispanic (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c27 = dataAH['hispanic'].value_counts(sort=False)
print (c27)

def asian (row) : 
    if row['h5od4d'] == 1: 
        return 1
    elif row['h5od4d'] == 0: 
        return 2
dataAH['asian'] = dataAH.apply(lambda row: asian (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c28 = dataAH['asian'].value_counts(sort=False)
print (c28)

def race (row) : 
    if row['hispanic'] == 1: 
        return 'Hispanic'
    elif row['black'] == 1: 
        return 'Black'
    elif row['asian'] == 1: 
        return 'Asian'
    elif row['white'] == 1: 
        return 'White'
dataAH['race'] = dataAH.apply(lambda row: race (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c29 = dataAH['race'].value_counts(sort=False)
print (c29)

#household income proxy
def hhincome (row) : 
    if row['h5ec2'] == 1: 
        return 2500
    elif row['h5ec2'] == 2: 
        return 7500
    elif row['h5ec2'] == 3: 
        return 12500
    elif row['h5ec2'] == 4: 
        return 17500
    elif row['h5ec2'] == 5: 
        return 22500
    elif row['h5ec2'] == 6: 
        return 27500
    elif row['h5ec2'] == 7: 
        return 35000
    elif row['h5ec2'] == 8: 
        return 45000
    elif row['h5ec2'] == 9: 
        return 62500
    elif row['h5ec2'] == 10: 
        return 87500
    elif row['h5ec2'] == 11: 
        return 125000
    elif row['h5ec2'] == 12: 
        return 175000
    elif row['h5ec2'] == 13: 
        return 250000
dataAH['hhincome'] = dataAH.apply(lambda row: hhincome (row), axis = 1)

#counts and percentages (i.e. frequency distributions)
c30 = dataAH['hhincome'].value_counts(sort=False)
print (c30)

#figure out number of NaN for each variable
dataAH.isnull().sum()

#addhealth_merged = pandas.merge(data1, data5, on='aid', how='right')
dataAH.head(100)
#dataAH.shape[0]
print (len(dataAH)) #number of observations (rows)
#print (len(dataAH.columns)) # number of variables (columns)


import statsmodels.formula.api as smf
# logistic regression
lreg1 = smf.logit(formula = 'collegedegree ~ C(gender) + C(race) + gpa + C(parentcollege) \
                 + C(expelled) + C(teachertrouble) + C(attentiontrouble) + C(hwtrouble) \
                     + C(socialtrouble) + C(closeschool) + C(partschool) + C(prejschool) \
                         + C(happyschool) + C(fairschool) +C(safeschool) + wave1grade \
                         + parenteat + momdisappointed + daddisappointed', data=dataAH).fit()
print (lreg1.summary())
# odd ratios with 95% confidence intervals
params = lreg1.params
conf = lreg1.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))

import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoLarsCV

data_clean=dataAH.dropna()
recode1 = {1:1, 0:2}
data_clean['gender1'] = data_clean['gender'].map(recode1)

predvar=data_clean[['gender1', 'race', 'parentcollege',  'gpa', 'expelled', 'teachertrouble', \
                    'attentiontrouble', 'hwtrouble', 'socialtrouble', 'closeschool', \
                    'partschool', 'prejschool', 'happyschool', 'fairschool', 'safeschool',\
                    'wave1grade', 'parenteat', 'momdisappointed', 'daddisappointed']]
    
target=data_clean.collegedegree

predictors=predvar.copy()
from sklearn import preprocessing
predictors['gender1']=preprocessing.scale(predictors['gender1'].astype('float64'))
predictors['race']=preprocessing.scale(predictors['race'].astype('float64'))
predictors['parentcollege']=preprocessing.scale(predictors['parentcollege'].astype('float64'))
predictors['gpa']=preprocessing.scale(predictors['gpa'].astype('float64'))
predictors['expelled']=preprocessing.scale(predictors['expelled'].astype('float64'))
predictors['teachertrouble']=preprocessing.scale(predictors['teachertrouble'].astype('float64'))
predictors['attentiontrouble']=preprocessing.scale(predictors['attentiontrouble'].astype('float64'))
predictors['hwtrouble']=preprocessing.scale(predictors['hwtrouble'].astype('float64'))
predictors['socialtrouble']=preprocessing.scale(predictors['socialtrouble'].astype('float64'))
predictors['closeschool']=preprocessing.scale(predictors['closeschool'].astype('float64'))
predictors['partschool']=preprocessing.scale(predictors['partschool'].astype('float64'))
predictors['prejschool']=preprocessing.scale(predictors['prejschool'].astype('float64'))
predictors['happyschool']=preprocessing.scale(predictors['happyschool'].astype('float64'))
predictors['fairschool']=preprocessing.scale(predictors['fairschool'].astype('float64'))
predictors['safeschool']=preprocessing.scale(predictors['safeschool'].astype('float64'))
predictors['wave1grade']=preprocessing.scale(predictors['wave1grade'].astype('float64'))
predictors['parenteat']=preprocessing.scale(predictors['parenteat'].astype('float64'))
predictors['momdisappointed']=preprocessing.scale(predictors['momdisappointed'].astype('float64'))
predictors['daddisappointed']=preprocessing.scale(predictors['daddisappointed'].astype('float64'))

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, target, test_size=.3,
                    random_state=123)

# specify the lasso regression model
model=LassoLarsCV(cv=10, precompute=False).fit(pred_train,tar_train)

# print variable names and regression coefficients
dict(zip(predictors.columns, model.coef_))

# plot coefficient progression
m_log_alphas = -numpy.log10(model.alphas_)
ax = plt.gca()
plt.plot(m_log_alphas, model.coef_path_.T)
plt.axvline(-numpy.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.ylabel('Regression Coefficients')
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Paths')

# plot mean square error for each fold
m_log_alphascv = -numpy.log10(model.cv_alphas_)
plt.figure()
plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k',
         label='Average across the folds', linewidth=2)
plt.axvline(-numpy.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean squared error')
plt.title('Mean squared error on each fold')
         
# MSE from training and test data
from sklearn.metrics import mean_squared_error
train_error = mean_squared_error(tar_train, model.predict(pred_train))
test_error = mean_squared_error(tar_test, model.predict(pred_test))
print ('training data MSE')
print(train_error)
print ('test data MSE')
print(test_error)

# R-square from training and test data
rsquared_train=model.score(pred_train,tar_train)
rsquared_test=model.score(pred_test,tar_test)
print ('training data R-square')
print(rsquared_train)
print ('test data R-square')
print(rsquared_test)


# bug fix for display formats to avoid run time errors
#pandas.set_option('display.float_format', lambda x:'%f'%x)
