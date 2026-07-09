import pandas as pd
df1=pd.read_csv("linkedIn_jobs.csv")
df2=pd.read_csv("clean_jobs.csv")
print(df1.head())
print(df2.head())
df1.info()
df1.duplicated().sum()
df1.drop_duplicates(inplace=True)
drop_cols=['job_posting_url','application_url','company_id','zip_code','fips','closed_time','expiry','posting_domain']
df1.drop(columns=drop_cols,inplace=True)
df1.columns
df1.isnull().sum()
df1.dropna(subset=['title','company_name','location'],inplace=True)
df1.info
df1[['min_salary','max_salary','med_salary']].isnull().sum()
df1['min_salary'].fillna(df1['min_salary'].median(), inplace=True)
df1['max_salary'].fillna(df1['max_salary'].median(), inplace=True)
df1['med_salary'].fillna(df1['med_salary'].median(), inplace=True)
df1['title'] = df1['title'].str.lower().str.strip()
df1['company_name'] = df1['company_name'].str.lower().str.strip()
df1['location'] = df1['location'].str.lower().str.strip()
df1['remote_allowed']=df1['remote_allowed'].fillna(0)
df1['formatted_work_type'].value_counts()
df1.shape
df1.isnull().sum()
df1.drop(columns=['skills_desc'],inplace=True)
df1['views']=df1['views'].fillna(df1['views'].median)
df1['applies']=df1['applies'].fillna(1000)
df1['formatted_experience_level'].value_counts()
df1['formatted_experience_level']=df1['formatted_experience_level'].fillna('Not Specified')
df1[['min_salary','max_salary','med_salary','normalized_salary']].isnull().sum()
drop_cols=['normalized_salary','pay_period','currency','compensation_type']
df1.drop(columns=drop_cols,inplace=True)
df1['applies']=df1['applies'].replace(1000,0)
df1.info()

df1['views']=pd.to_numeric(df1['views'],errors='coerce')
df1['views']=df1['views'].fillna(df1['views'].median())
df1['avg_salary']=(df1['min_salary']+df1['max_salary'])/2
df1['remote_status']=df1['remote_allowed'].map({1:'Remote',0:'Onsite'})
df1['remote_status'].value_counts()
df1.info()
df1.to_csv("Clean_linkedin_jobs.csv",index=False)
df2.info()
df2.isnull().sum()
df2.drop(columns=['link','work_type','employment_type'],inplace=True)
df2.dropna(subset=['company','location'],inplace=True)
df2['source']=df2['source'].fillna('Unknown')
df2['date_posted']=pd.to_datetime(df2['date_posted'],errors='coerce')
df2['date_posted']=df2['date_posted'].ffill()
df2['title'] = df2['title'].str.lower().str.strip()
df2['company'] = df2['company'].str.lower().str.strip()
df2['location'] = df2['location'].str.lower().str.strip()
df2.info()
df2.isnull().sum()
df2.to_csv("Clean_jobs_linkedin.csv",index=False)

import pandas as pd
df=pd.read_csv("Clean_linkedin_jobs.csv")
df.to_csv("linkedin_jobs_mysql.csv",index=False,encoding="utf-8")



import pandas as pd
df1=pd.read_csv("clean_linkedin_jobs.csv")
df1.info()

df2=pd.read_csv("clean_data_linkedin_jobs.csv")
df2.info()