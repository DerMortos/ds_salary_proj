# original tutorial by ken jee, code in glassdoor_scraper.py file
# https://www.youtube.com/watch?v=GmW4F6MHqqs&list=PL2zq7klxX5AReJn7nZfqOKLZ3IpKj7fwc&index=26


# modified to work in conjunction with
# https://github.com/rohan-benjamin/Glassdoor-Scraper-Final/blob/main/glassdoor_scraper.ipynb


from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import time

#get_jobs(keyword, num_jobs, verbose, path, slp_time):
def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    options = Options()
    options.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(path, options=options)
    driver.get("https://www.glassdoor.com/Job/jobs.htm")

    search_input = driver.find_element(By.CLASS_NAME, "keyword")
    driver.find_element(By.CLASS_NAME, "loc").clear()

    location_input = driver.find_element(By.CLASS_NAME, "loc")
    search_input.send_keys(keyword)
    location_input.send_keys("United States")
    search_input.send_keys(Keys.ENTER)
    time.sleep(slp_time)
    
    
    company_name = []
    job_title = []
    location = []
    job_description = []
    salary_estimate = []
    company_size = []
    company_type = []
    company_sector = []
    company_industry = []
    company_founded = []
    company_revenue = []
    rating = []
    headquarters = []
    #type_of_ownership = []
    #competitors = []

    
    
    
    #Set current page to 1
    current_page = 1     
        
        
    time.sleep(slp_time)
    
    while current_page <= num_jobs:   
        
        done = False
        while not done:
            job_cards = driver.find_elements(By.XPATH, "//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")
            for card in job_cards:
                card.click()
                time.sleep(1)

                #Closes the signup prompt
                try:
                    driver.find_element(By.XPATH, ".//span[@class='SVGInline modal_closeIcon']").click()
                    time.sleep(2)
                except NoSuchElementException:
                    time.sleep(2)
                    pass

                #Expands the Description section by clicking on Show More
                try:
                    driver.find_element(By.XPATH, "//div[@class='css-t3xrds e856ufb4']").click()
                    time.sleep(1)
                except NoSuchElementException:
                    card.click()
                    print(str(current_page) + '#ERROR: no such element')
                    time.sleep(30)
                    driver.find_element(By.XPATH, "//div[@class='css-t3xrds e856ufb4']").click()
                except ElementNotInteractableException:
                    card.click()
                    driver.implicitly_wait(30)
                    print(str(current_page) + '#ERROR: not interactable')
                    driver.find_element(By.XPATH, "//div[@class='css-t3xrds e856ufb4']").click()

                #Scrape 

                try:
                    company_name.append(driver.find_element(By.XPATH, "//div[@class='css-87uc0g e1tk4kwz1']").text)
                except:
                    company_name.append("#N/A")
                    pass

                try:
                    job_title.append(driver.find_element(By.XPATH, "//div[@class='css-1j389vi e1tk4kwz2']").text)
                except:
                    job_title.append("#N/A")
                    pass

                try:
                    location.append(driver.find_element(By.XPATH, "//div[@class='css-56kyx5 e1tk4kwz5']").text)
                except:
                    location.append("#N/A")
                    pass

                try:
                    job_description.append(driver.find_element(By.XPATH, "//div[@id='JobDescriptionContainer']").text)
                except:
                    job_description.append("#N/A")
                    pass

                try:
                    salary_estimate.append(driver.find_element(By.XPATH, "//div[@class='css-1xe2xww e1wijj242']").text)
                except:
                    salary_estimate.append("#N/A")
                    pass
                
                try:
                    company_size.append(driver.find_element(By.XPATH, "//div[@id='CompanyContainer']//span[text()='Size']//following-sibling::*").text)
                except:
                    company_size.append("#N/A")
                    pass
                
                # try:
                #     company_type.append(driver.find_element(By.XPATH, "//div[@id='CompanyContainer']//span[text()='Type']//following-sibling::*").text)
                # except:
                #     company_type.append("#N/A")
                #     pass
                    
                try:
                    company_sector.append(driver.find_element(By.XPATH, "//div[@id='CompanyContainer']//span[text()='Sector']//following-sibling::*").text)
                except:
                    company_sector.append("#N/A")
                    pass
                    
                try:
                    company_industry.append(driver.find_element(By.XPATH, "//div[@id='CompanyContainer']//span[text()='Industry']//following-sibling::*").text)
                except:
                    company_industry.append("#N/A")
                    pass
                    
                try:
                    company_founded.append(driver.find_element(By.XPATH, "//div[@id='CompanyContainer']//span[text()='Founded']//following-sibling::*").text)
                except:
                    company_founded.append("#N/A")
                    pass
                    
                try:
                    company_revenue.append(driver.find_element(By.XPATH, "//div[@id='CompanyContainer']//span[text()='Revenue']//following-sibling::*").text)
                except:
                    company_revenue.append("#N/A")
                    pass

                try:
                    rating.append(driver.find_element(By.XPATH, "//span[@class='css-1m5m32b e1tk4kwz2']").text)
                except:
                    rating.append("#N/A")
                    pass

                try:
                    headquarters.append(driver.find_element(By.XPATH, '//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text)
                except:
                    headquarters.append("#N/A")
                    pass


                 #Printing for debugging
                if verbose:
                    print("Job Title: {}".format(job_title))
                    print("Salary Estimate: {}".format(salary_estimate))
                    print("Job Description: {}".format(job_description[:500]))
                    print("Rating: {}".format(rating))
                    print("Company Name: {}".format(company_name))
                    print("Location: {}".format(location))
                    print("Headquarters: {}".format(headquarters))
                    print("Company Size {}".format(company_size))
                    print("Company Founded {}".format(company_founded))
                    #print("Type of Ownership {}".format(type_of_ownership))
                    print("Company industry {}".format(company_industry))
                    print("Company Sector {}".format(company_sector))
                    print("Company Revenue {}".format(company_revenue))
                    #print("Competitors {}".format(competitors))                    
                    
                done = True
                
       # Moves to the next page         
        if done:
            print(str(current_page) + ' ' + 'out of' +' '+ str(num_jobs) + ' ' + 'pages done')
            driver.find_element(By.XPATH, "//span[@alt='next-icon']").click()   
            current_page = current_page + 1
            time.sleep(4)
            




    driver.close()
    df = pd.DataFrame({'job title': job_title,
    'salary estimate': salary_estimate,
    'job description': job_description,
    'rating': rating,
    'company': company_name,
    'location': location,
    "headquarters" : headquarters,
    'company_size': company_size,
    'company_founded' : company_founded,
    #"type of ownership" : type_of_ownership,
    'company_industry' : company_industry,
    'company_sector': company_sector,  
    'company_revenue': company_revenue#,
    #'competitors': competitors
    })
    
    df.to_csv(keyword + '2.csv')
    #return pd.DataFrame(df)