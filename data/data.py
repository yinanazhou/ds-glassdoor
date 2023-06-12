# -*- coding: utf-8 -*-

import glassdoor_scraper as gs
import pandas as pd

path = "./chromedriver_mac_arm64/"

df = gs.get_jobs('data scientist', 'Canada', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)