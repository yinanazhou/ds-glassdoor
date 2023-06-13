# -*- coding: utf-8 -*-
"""
url: https://github.com/arapfaik/scraping-glassdoor-selenium
url: https://github.com/PlayingNumbers/ds_salary_proj
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def close_pop_window(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, '[alt="Close"]').click()  # clicking to the X.
    except NoSuchElementException:
        pass


def get_jobs(keyword, location, num_jobs, verbose, path, slp_time):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    # Initializing the webdriver
    options = webdriver.ChromeOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.maximize_window()

    url = "https://www.glassdoor.ca/Job/" + location.lower() + \
          "-" + keyword.lower().replace(' ', '-') + \
          "-jobs-SRCH_IL.0,6_IN3_KO7,21.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=" + \
          location + "&context=Jobs&dropdown=0"
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  # If true, should be still looking for new jobs.

        # Let the page load. Change this number based on your internet speed.
        # Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        # Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element(By.CLASS_NAME, "selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        close_pop_window(driver)

        # Going through each job in this page
        job_buttons = driver.find_elements(By.XPATH, './/a[@data-test="job-link"]')
        for job_button in job_buttons:

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            close_pop_window(driver)
            try:
                job_button.click()  # You might
            except:
                continue

            time.sleep(1)
            collected_successfully = False

            close_pop_window(driver)

            while not collected_successfully:
                try:
                    company_name = driver.find_element(By.XPATH, './/div[@data-test="employerName"]').text
                    location = driver.find_element(By.XPATH, './/div[@data-test="location"]').text
                    job_title = driver.find_element(By.XPATH, './/div[@data-test="jobTitle"]').text
                    job_description = driver.find_element(By.XPATH, './/div[@class="jobDescriptionContent desc"]').get_attribute('innerText')
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element(By.XPATH, './/span[@data-test="detailSalary"]').text
            except NoSuchElementException:
                salary_estimate = -1  # You need to set a "not found value. It's important."

            try:
                rating = driver.find_element(By.XPATH, './/span[@data-test="detailRating"]').text
            except NoSuchElementException:
                rating = -1  # You need to set a "not found value. It's important."

            # Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            # Going to the Company tab...
            try:
                headquarters = driver.find_element(By.XPATH,
                                                   './/div[@id="EmpBasicInfo"]//span[text()="Headquarters"]//following-sibling::*').text
            except NoSuchElementException:
                headquarters = -1

            try:
                size = driver.find_element(By.XPATH,
                                           './/div[@id="EmpBasicInfo"]//span[text()="Size"]//following-sibling::*').text
            except NoSuchElementException:
                size = -1

            try:
                founded = driver.find_element(By.XPATH,
                                              './/div[@id="EmpBasicInfo"]//span[text()="Founded"]//following-sibling::*').text
            except NoSuchElementException:
                founded = -1

            try:
                type_of_ownership = driver.find_element(By.XPATH,
                                                        './/div[@id="EmpBasicInfo"]//span[text()="Type"]//following-sibling::*').text
            except NoSuchElementException:
                type_of_ownership = -1

            try:
                industry = driver.find_element(By.XPATH,
                                               './/div[@id="EmpBasicInfo"]//span[text()="Industry"]//following-sibling::*').text
            except NoSuchElementException:
                industry = -1

            try:
                sector = driver.find_element(By.XPATH,
                                             './/div[@id="EmpBasicInfo"]//span[text()="Sector"]//following-sibling::*').text
            except NoSuchElementException:
                sector = -1

            try:
                revenue = driver.find_element(By.XPATH,
                                              './/div[@id="EmpBasicInfo"]//span[text()="Revenue"]//following-sibling::*').text
            except NoSuchElementException:
                revenue = -1

            try:
                competitors = driver.find_element(By.XPATH,
                                                  './/div[@id="EmpBasicInfo"]//span[text()="Competitors"]//following-sibling::*').text
            except NoSuchElementException:
                competitors = -1

            try:
                recommend = driver.find_element(By.XPATH,
                                                  './/div[@id="employerStats"]//div[text()="Recommend to a friend"]//preceding-sibling::*').text
            except NoSuchElementException:
                recommend = -1

            try:
                ceo = driver.find_element(By.XPATH,
                                                  './/div[@id="employerStats"]//span[text()="Approve of CEO"]//preceding-sibling::*').text
            except NoSuchElementException:
                ceo = -1

            try:
                career = driver.find_element(By.XPATH,
                                                  './/div[@data-test="company-ratings"]//ul//span[text()="Career Opportunities"]//following-sibling::span[2]').text
            except NoSuchElementException:
                career = -1

            try:
                benefit = driver.find_element(By.XPATH,
                                                  './/div[@data-test="company-ratings"]//ul//span[text()="Comp & Benefits"]//following-sibling::span[2]').text
            except NoSuchElementException:
                benefit = -1

            try:
                culture = driver.find_element(By.XPATH,
                                                  './/div[@data-test="company-ratings"]//ul//span[text()="Culture & Values"]//following-sibling::span[2]').text
            except NoSuchElementException:
                culture = -1

            try:
                management = driver.find_element(By.XPATH,
                                                  './/div[@data-test="company-ratings"]//ul//span[text()="Senior Management"]//following-sibling::span[2]').text
            except NoSuchElementException:
                management = -1

            try:
                wlb = driver.find_element(By.XPATH,
                                                  './/div[@data-test="company-ratings"]//ul//span[text()="Work/Life Balance"]//following-sibling::span[2]').text
            except NoSuchElementException:
                wlb = -1

            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title": job_title,
                         "Salary Estimate": salary_estimate,
                         "Job Description": job_description,
                         "Rating": rating,
                         "Company Name": company_name,
                         "Location": location,
                         "Headquarters": headquarters,
                         "Size": size,
                         "Founded": founded,
                         "Type of ownership": type_of_ownership,
                         "Industry": industry,
                         "Sector": sector,
                         "Revenue": revenue,
                         "Competitors": competitors,
                         "Recommend Rating": recommend,
                         "CEO Rating": ceo,
                         "Career Opportunities": career,
                         "Comp & Benefits": benefit,
                         "Culture & Values": culture,
                         "Senior Management": management,
                         "Work/Life Balance": wlb})
            # add job to jobs

        # Clicking on the "next page" button

        next_button = driver.find_element(By.XPATH, './/button[@data-test="pagination-next"]')
        if (next_button.is_enabled()):
            next_button.click()
        else:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs,
                                                                                                         len(jobs)))
            break

    return pd.DataFrame(jobs)  # This line converts the dictionary object into a pandas DataFrame.

