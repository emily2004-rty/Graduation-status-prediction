## Graduation status prediction
## Overview 
This project focuses on building a machine learning model to predict a student’s graduation status based on their skill level and academic attributes.
The system analyzes key indicators such as technical skills, academic performance, engagement, and other relevant factors to estimate whether a student is likely to graduate successfully.

The goal is to help educational institutions identify at-risk students early and provide targeted support to improve outcomes.
## Problem definition
EverthingData educational institute struggle with student retention and graduation rates.ldentifying at-risk students early is challenging leading to reactive rather than proactive support.This results in wasted resources for the institution and negative outcome for students 
## ML problem
This ia a classification problem .the goal is to predict whether a student will graduate(1) or not graduate(0),based on their motivation,demographic  and institute data 
## Objective
The objective of this  project is to create a machine learning model that predicts graduatation status of the mentorship program students.this will allow academic advisors and support teams to intervene early with targeted resources thereby improving overall graduation rates 

## Tech Stack
The prediction was bult using the following tools and technologies
1.Python libraries:

Pandas Numpy for data exploration and manipulation

Matplotlib and seaborn for data visualization

Scikit-learn for model loading,training and testing 

Streamlit for testing of the working of the model

2. Machine learning model
Random forest

Logistic Regression

Support Vector Machine

3 Model storage

Pickle and Joblib

4.Development environment

Jupyter Notebook

## Insights
<img width="314" height="277" alt="image" src="https://github.com/user-attachments/assets/2695765c-71a2-4a23-8219-8d5288d83e1b" />

A large percentage of applicants were not able to make it to the graduation compared to those who were able to graduate 

<img width="878" height="519" alt="image" src="https://github.com/user-attachments/assets/bdd96b9c-33b7-4c38-a063-d978728fc027" />

Applicants who graduated are those with low performance compared to those with high score.Futhermore the applicants in the datascience track  outperformed those in data analysis track 
 
<img width="647" height="493" alt="image" src="https://github.com/user-attachments/assets/a58f2b6d-7c51-4f7f-9870-55e96db92aab" />

Monday , Tuesday and Wednesday showed highest participation of application Thursday and Friday showing moderate engagement with Weekend a lower engagement 

<img width="729" height="610" alt="image" src="https://github.com/user-attachments/assets/29b18b79-fef0-4c62-82b3-d5fe3722acd2" />

A lot of applicants they want to upskill their data knowledge while some want to connect 
,build projects,learn afresh,network.A lot of graduates are the onces who want to upskill their knowledge although applicants whose aim are learning more and both connect and upskill shows a good number of graduates as all of they graduate

<img width="658" height="506" alt="image" src="https://github.com/user-attachments/assets/9503ac90-3f38-4601-9f4e-3625c82fa5c3" />

Many of applicants are in the elementary skill level followed with the beginner skill level.Advanced being the least significant. 

<img width="1790" height="490" alt="image2" src="https://github.com/user-attachments/assets/0abc23a2-05db-4154-8a9d-68f88a3283cb" />
<img width="1790" height="490" alt="image" src="https://github.com/user-attachments/assets/ac2fdb80-bc77-48e7-bd74-d3e255e25396" />
<img width="1790" height="490" alt="image3" src="https://github.com/user-attachments/assets/97a6bd86-77fe-4a01-aaf6-9c414d0a6899" />

Graduation trends 

Track:The distrubition of participants by graduation status indicated a higher number of graduates in the data analysis track than in datascience despite data analysis having a few applicants compared to data science 

Age_range:The majority of applicants are between 18-24 years have graduated indicating that many individuals are completing their education before entering the workforce.for those in between 25-34 years there is anoticeable number of individuals who have not graduated which could imply that some are seeing to enter the field without degrees 

Hear_about_us:Whatsapp appears to be the most common source for applicants with significant number of graduates indicating they heard about the program through these medium.Other platform like Twitter and LinkeldIn also show noticeble counts though they are less than whatsapp.Instagrm and through friend have lesser presentation suggesting these platform are less effective in reaching potential candidates. 

Learning_experience:A large portion of applicants have less than six month of experience with many of them categorized as graduates.the high number of graduates with less learning experience may suggest that the progrm is effective in quickly preparing individuals for the workforce  

Country distribution :Kenya shows a significantly higher count compared to south Africa indicating a greater applicants are from Kenya,Kenya has a high graduation rate compared to southAfrica which suggest that education is important to individuals in this country 

## Conclusion:  
The  models appears to have a strong performnce on class 0 that is No  but struggles with class 1 as indicated by recall and F1-Score  suggesting a need for more data.
Support vector machine algorithm is best fitted for prediction as it has accuracy of 73% 

Model Algorithm used 	Accuracy Score 

Logistic Regression model 	46% 

Random Forest Classifier 	70% 

KNeighbors Classifier 	63% 

Support Vector Machine 	73% 
 	 
 
Recommended data driven suggestion that can improve graduation rates 

•	Conduction of regional analysis and understand why graduation rates differ between Kenya and South Africa. Hiring program facilitators or mentors around South Africa to provide local support and relevance. 

•	Offering more flexible scheduling like recorded lectures to accommodate work and family commitments. Provide a career counselling focused on how the program benefits someone already in the workforce 

•	Conduction of survey both graduates and drop outs to identify the main pain points and introduce mandatory check-ins, supplemental workshops or peer mentoring. 

•	Allocation of more marketing time and effort to channels that bring in the most engaged applicants not just the most applicants 







 
