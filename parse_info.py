import requests
import os

geocodio_key = os.environ['GEOCODIO_API_KEY']
def get_province_map(locations):
    cities = locations.unique()
    city_to_province = {}
    for city in cities:
        url = f'https://api.geocod.io/v1.6/geocode?q={city}&country=CA&api_key={geocodio_key}'
        response = requests.get(url)
        data = response.json()
        
        if 'results' in data and len(data['results']) > 0:
            # Extract the province from the API response
            province = data['results'][0]['address_components']['state']
            
            # Add the city and province to the dictionary
            city_to_province[city] = province
        else:
            city_to_province[city] = city
    return city_to_province

def get_salary_src(src):
    if '(Employer Est.)' in src:
        return 'Employer'
    elif '(Glassdoor Est.)' in src:
        return 'Glassdoor'
    else:
        return 'Not Specified'


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
        return 'Not Specified'


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
        return 'Not Specified'
