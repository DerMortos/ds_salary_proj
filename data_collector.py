import pandas as pd
import glassdoor_scraperUpdated as gs
path = "/usr/bin/chromedriver"

# get_jobs(keyword, num_jobs, verbose, path, slp_time)
df = gs.get_jobs('data scientist', 1, True, path, 5)