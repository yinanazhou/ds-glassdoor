def get_salary_src(src):
    if '(Employer Est.)' in src:
        return 'Employer'
    elif '(Glassdoor Est.)' in src:
        return 'Glassdoor'
    else:
        return 'NA'


def get_exp_level(title):
    if 'intern' in title.lower() or \
            'coop' in title.lower() or \
            'co-op' in title.lower():
        return 'Intern'
    elif 'junior' in title.lower() or \
            'jr' in title.lower() or \
            'new grad' in title.lower():
        return 'Junior'
    elif 'senior' in title.lower() or \
            'sr' in title.lower() or \
            'staff' in title.lower() or \
            'director' in title.lower() or \
            'principle' in title.lower() or \
            'manager' in title.lower() or \
            'lead' in title.lower() or \
            'president' in title.lower():
        return 'Senior'
    else:
        return 'NA'


def get_work_field(title):
    if 'data scientist' in title.lower():
        return 'Data Scientist'
    elif 'data engineer' in title.lower():
        return 'Data Engineer'
    elif 'analyst' in title.lower():
        return 'Data Analyst'
    elif 'machine learning' in title.lower():
        return 'MLE'
    elif 'manager' in title.lower() or 'lead' in title.lower():
        return 'Manager'
    elif 'director' in title.lower():
        return 'Director'
    else:
        return 'NA'
