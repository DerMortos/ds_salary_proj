import pandas as pd
import glassdoor_scraper as gs
path = "/usr/bin/chromedriver"

df = gs.get_jobs('data scientist', 10, False, path, 10)