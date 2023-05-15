# -*- coding: utf-8 -*-
"""
url: https://github.com/PlayingNumbers/ds_salary_proj
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_est'] = df['Salary Estimate'].apply(lambda x: 1 if '(Employer Est.)' in x else 0)
df['glassdoor_est'] = df['Salary Estimate'].apply(lambda x: 1 if '(Glassdoor Est.)' in x else 0)
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
# remove k and $ in salary
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))
# remove text in salary
salary_cln = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('(Glassdoor Est.)', '').replace('(Employer Est.)', ''))

df['min_salary'] = salary_cln.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = salary_cln.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

# Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)

# age of company
df['Age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# parsing of job description (python, etc.)

# python
df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# r
df['R'] = df['Job Description'].apply(lambda x: 1 if 'R' in x else 0)
# spark
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# SQL
df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
# AWS
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
# excel
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# Tableau
df['Tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
# PowerBI
df['PowerBI'] = df['Job Description'].apply(lambda x: 1 if 'powerbi' in x.lower() or 'power bi' in x.lower() else 0)
# Azure
df['Azure'] = df['Job Description'].apply(lambda x: 1 if 'azure' in x.lower() else 0)
# French
df['French'] = df['Job Description'].apply(lambda x: 1 if 'french' in x.lower() or 'bilingual' in x.lower() else 0)

# experience level
df['Junior'] = df['Job Title'].apply(lambda x: 1 if 'junior' in x.lower()
                                                    or 'jr' in x.lower()
                                                    or 'entry' in x.lower()
                                                    or 'new grad' in x.lower()
                                                    else 0)
# experience level
df['Senior'] = df['Job Title'].apply(lambda x: 1 if 'senior' in x.lower()
                                                    or 'sr' in x.lower()
                                                    or 'staff' in x.lower()
                                                    or 'director' in x.lower()
                                                    or 'principle' in x.lower()
                                                    else 0)


df.to_csv('data_processed.csv', index=False)
