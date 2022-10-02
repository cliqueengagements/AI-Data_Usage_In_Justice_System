# MLH AIHACK4Good 2022 

PROJECT NAME: AI Data Usage In The Justice System

Run the RF_Prison.py to make it work

# Who is ready to leave (Criminal version)
Yang Chang, Dongting Ma

Abstract
Across the nation, judges, probation and parole officers are increasingly using
algorithms to assess a criminal defendant’s likelihood of becoming a recidivist. A tool called
COMPAS is introduced and used in many jurisdictions around the U.S. to predict if a
convicted criminal is likely to re-offend. COMPAS algorithms assign a score to each
defendant ranging from 1 to 10 with ten being the highest risk.With quantifiable data, we
could potentially build a model to predict if a criminal defendant will commit crime again or
not. Therefore, Our goal for this project is to train a model using crime history data, predict
criminal defendants’ likelihood of becoming recidivists and thus help decide which inmates
are ready for parole.
1. Data background
We looked at more than 7,000 criminal defendants data obtained two years’ worth of
COMPAS scores from the Broward County Sheriff’s Office in Florida and compared the
predicted recidivism rates with the rate that actually occurred over a two-year period. These
7,000 criminal defendants’ age range from 18 to 96 with a mean age of 34. Most defendants
are booked in jail where they respond to a COMPAS questionnaire. Their answers are fed
into the COMPAS software to generate several scores including predictions of “Risk of
Recidivism” and “Risk of Violent Recidivism.”
2. Messy data and data cleaning
There are over 50 predictor variables in the raw dataset. However, there are over
fifteen variables which have more than 50% missing value. For those variables, it is really
hard to fill them so we decide to drop them. Furthermore, we also find repeat columns which
have exactly the same data in them. We choose to keep one and drop another so that it will
not affect training our model. There is one variable named ‘days_b_screening_arrest’ which
means days between arrest and screening. According to a study conducted earlier about
COMPAS score , if it is over 30 days, it has low data quality.So we filter observations with an absolute value of ‘days_b_screening_arrest’ more than 30 . Lastly, We also drop variables
that have only one category in them because it is not helpful when fitting our model.
