from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = r"C:\\Program Files (x86)\\chromedriver.exe"
proxy_ip = "115.114.77.133:9090"

options = Options()
options.add_argument(f"--proxy-server=http://{proxy_ip}")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://affidavit.eci.gov.in")

form = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "CandidateCustomFilter"))
)

election_type = form.find_element(By.ID, "electionType")
election_type.send_keys("Election-Oct-Dec-2023")
election_type.send_keys(Keys.RETURN)

time.sleep(2)

election = form.find_element(By.ID, "election")
election.click()
election.send_keys("AC - GENERAL")
election.send_keys(Keys.RETURN)

time.sleep(2)

state_name = form.find_element(By.ID, "states")
state_name.click()
state_name.send_keys("Telangana")
state_name.send_keys(Keys.RETURN)

phase = form.find_element(By.ID, "phase")
phase.click()
phase.send_keys("1")
phase.send_keys(Keys.RETURN)

constituency = form.find_element(By.ID, "constId")
constituency.click()
constituency.send_keys("Select Constituency")
constituency.send_keys(Keys.RETURN)

time.sleep(7)

filter_button = form.find_element(By.CSS_SELECTOR, "button.btn.search.btn-primary")
filter_button.click()
