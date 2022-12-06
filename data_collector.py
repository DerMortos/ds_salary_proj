import pandas as pd
import glassdoor_scraper as gs
path = "/usr/bin/chromedriver"

# get_jobs(keyword, num_jobs, verbose, path, slp_time)
df = gs.fetch_jobs('data scientist', 10, False, path, 5)