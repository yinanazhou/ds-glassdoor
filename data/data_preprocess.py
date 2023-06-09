# -*- coding: utf-8 -*-
"""
url: https://github.com/PlayingNumbers/ds_salary_proj
"""

import pandas as pd
import parse_info

df = pd.read_csv('glassdoor_jobs.csv')

# get province
province_map = parse_info.get_province_map(df['Location'])
df['Province'] = df['Location'].map(province_map)

# salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
# print('# hourly: ', df.hourly.sum()) # no hourly rate
df['salary_src'] = df['Salary Estimate'].apply(parse_info.get_salary_src)

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
df['company_txt'] = df['Company Name'].apply(lambda x: x.split('\n')[0])

# age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# parsing of job description (python, etc.)

# python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# r
df['r'] = df['Job Description'].apply(lambda x: 1 if 'R,' in x else 0)
# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# SQL
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
# AWS
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() or 'amazon' in x.lower() else 0)
# excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# Tableau
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
# PowerBI
df['powerBI'] = df['Job Description'].apply(lambda x: 1 if 'powerbi' in x.lower() or 'power bi' in x.lower() else 0)
# Azure
df['azure'] = df['Job Description'].apply(lambda x: 1 if 'azure' in x.lower() else 0)
# French
df['french'] = df['Job Description'].apply(lambda x: 1 if 'french' in x.lower() or 'bilingual' in x.lower() else 0)

# experience level
df['exp_level'] = df['Job Title'].apply(parse_info.get_exp_level)

# work field
df['field'] = df['Job Title'].apply(parse_info.get_work_field)


df.to_csv('data_processed.csv', index=False)
