import pandas as pd
import glassdoor_scraperUpdated as gs
path = "/usr/bin/chromedriver"

df = gs.get_jobs('data scientist', "United States", 23, False, path)