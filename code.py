import time
import random
import datetime as datetime
from pytz import timezone
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


#***   Date Time ****
india_time = timezone('Asia/Kolkata')
today      = datetime.datetime.now(india_time)
days       = datetime.timedelta(1)
yesterday = today - days
DB_yesterday = datetime.datetime.now(india_time) - datetime.timedelta(1)

driver = webdriver.Edge()
driver.get("https://www.linkedin.com")

sleep(2)


user_name = driver.find_element(By.ID,"session_key")
user_name.send_keys("email")
sleep(0.5)

password = driver.find_element(By.ID,"session_password")
password.send_keys("password")

sleep(0.5)

submit = driver.find_element(By.XPATH,'//*[@type="submit"]')
submit.click()
sleep(8)

# Urls of the company 
urls=[
"https://www.linkedin.com/company/cognizant/",
"https://www.linkedin.com/company/itc-limited/",
"https://www.linkedin.com/company/bajaj-auto-ltd/",
"https://www.linkedin.com/company/infosys/",
"https://www.linkedin.com/company/tata-motors/",
"https://www.linkedin.com/company/bpcl/",
"https://www.linkedin.com/company/ashok-leyland/",
"https://www.linkedin.com/company/larsen-&-toubro-limited/",
"https://www.linkedin.com/company/hcltech/"
"https://www.linkedin.com/company/tata-consultancy-services/",
"https://www.linkedin.com/company/unilever/",
"https://www.linkedin.com/company/adani-group/",
"https://www.linkedin.com/company/tataelxsi/",
"https://www.linkedin.com/company/zensar/",
"https://www.linkedin.com/company/empower-india/",
"https://www.linkedin.com/company/mindteck/",
"https://www.linkedin.com/company/accel-limited/",
"https://www.linkedin.com/company/trigyn-technologies/",
"https://www.linkedin.com/company/kellton/",
"https://www.linkedin.com/company/mphasis/",
"https://www.linkedin.com/company/asm-technologies/",
"https://www.linkedin.com/company/63-moons-%E2%84%A2/",
"https://www.linkedin.com/company/goldstone-technologies/",
"https://www.linkedin.com/company/cg-vak-software-&-exports-ltd/",
"https://www.linkedin.com/company/cybertech/",
"https://www.linkedin.com/company/sonata-software/",
"https://www.linkedin.com/company/orchasp-limited/",
"https://www.linkedin.com/company/softsol-india-ltd/",
"https://www.linkedin.com/company/california-software/", 
"https://www.linkedin.com/company/birlasoft/",
"https://www.linkedin.com/company/coforge-tech/",
"https://www.linkedin.com/company/3i-infotech/",
"https://www.linkedin.com/company/3i-infotech/",
"https://www.linkedin.com/company/aurionpro-solutions/",
"https://www.linkedin.com/company/persistent-systems/",
"https://www.linkedin.com/company/objectone-information-systems-ltd/",
"https://www.linkedin.com/company/ceinsys-tech-limited/",
"https://www.linkedin.com/company/intellect_design_arena/",
"https://www.linkedin.com/company/magellanic-cloud/?originalSubdomain=in",
"https://www.linkedin.com/company/hypersoft-technologies-ltd/about/",
"https://www.linkedin.com/company/ltimindtree/?originalSubdomain=in",
"https://www.linkedin.com/company/sagarsoft-india-ltd/?originalSubdomain=in",
"https://www.linkedin.com/company/globalspace-tech--pvt--ltd-/?originalSubdomain=in",
"https://www.linkedin.com/company/trejhara/?originalSubdomain=in",
"https://www.linkedin.com/company/kpit/?originalSubdomain=in",
"https://www.linkedin.com/company/alphalogic-inc/?originalSubdomain=in",
"https://www.linkedin.com/company/happiest-minds-technologies/?originalSubdomain=in",
"https://www.linkedin.com/company/secmark-consultancy-limited/?originalSubdomain=in",
"https://www.linkedin.com/company/drc-systems/?originalSubdomain=in",
"https://www.linkedin.com/company/latentview-analytics/?originalSubdomain=in",
"https://www.linkedin.com/company/rategain/?originalSubdomain=in",
"https://www.linkedin.com/company/softtechengineersltd/?originalSubdomain=in",
"https://www.linkedin.com/company/ksolves/?originalSubdomain=in",
"https://www.linkedin.com/company/accelerate-business-solutions/?originalSubdomain=in",
"https://www.linkedin.com/company/saksoft/?originalSubdomain=in"

]

final_data=[]
for i in urls:
    driver.get(i)
    time.sleep(random.uniform(2.5,5.1))
    company = driver.find_element(By.TAG_NAME,"h1")
    com=company.text

    details = driver.find_elements(By.CLASS_NAME,'org-top-card-summary-info-list__info-item')
    list=[]
    for detail in details:
        list.append(detail.text)
    
    followers=list[-2].split()
    employees=list[-1].split()
    follow=followers[0]
    employ=employees[0]

    data={
        'Company': com,
        'Followers':follow,
        'Employees':employ,
        'Runtime':today.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    final_data.append(data)
    
    time.sleep(random.uniform(0.6,2.1))

df=pd.DataFrame(final_data)
df.index=df.index + 1

# DataFrame of the final Data
display(df)

#quiting the driver
driver.quit()
