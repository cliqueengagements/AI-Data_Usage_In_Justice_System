def rf(decile, priors, isviolent, sex, age, race, charge, score):
    if(sex=='Male'):
        sex_Male = 1
        sex_Female=0
    else:
        sex_Male = 0
        sex_Female=1
    race_Asian=0
    race_AfricanAmerican=0
    race_Caucasian=0
    race_Hispanic=0
    race_NativeAmerican=0
    race_Other=0
    if(race=='Asian'):
        race_Asian=1        
    elif(race=='African American'):
        race_AfricanAmerican=1
    elif(race=='race_Caucasian'):
        race_Caucasian=1
    elif(race=='race_Hispanic'):
        race_Hispanic=1
    elif(race=='race_NativeAmerican'):
        race_NativeAmerican=1
    elif(race=='Other'):
        race_Other=1
    score_H=0
    score_L=0
    score_M=0
    charge_M=0
    charge_F=0
    if(score=='High'):
        score_H=1
    elif(score=='Low'):
        score_L=1
    elif(score=='Medium'):
        score_M=1
    if(charge=='First'):
        charge_F=1
    elif(charge=='Multiple'):
        charge_M=1
    age_cat_25_45=0
    age_cat_Greater=0
    age_cat_Less=0
    if(age>25 and age<45):
        age_cat_25_45=1
    elif(age>=45):
        age_cat_Greater=1
    elif(age<=25):
        age_cat_Less=1
    
    df = pd.DataFrame({'decile':[decile],'priors_count':[priors],'is_violent_recid':[isviolent],'sex_Female':[sex_Female],'sex_Male':[sex_Male],'age_cat_25 - 45':[age_cat_25_45],'age_cat_Greater than 45':[age_cat_Greater],'age_cat_Less than 25':[age_cat_Less],'race_African-American':[race_AfricanAmerican],'race_Asian':[race_Asian],'race_Caucasian':[race_Caucasian],'race_Hispanic':[race_Hispanic],'race_Native':[race_NativeAmerican],'race_Other':[race_Other],'c_charge_degree_F':[charge_F],'c_charge_degree_M':[charge_M],'score_text_High':[score_H],'score_text_Low':[score_L],'score_text_Medium':[score_M]})
    rfprisoner = joblib.load('filename.pkl')
    prediction = rfprisoner.predict(df)

