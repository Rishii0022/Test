from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chromedriver_path = r"C:\\Program Files (x86)\\chromedriver.exe"
proxy_ip = "115.114.77.133:9090"

options = Options()
options.add_argument(f"--proxy-server=http://{proxy_ip}")

driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
driver.get("https://affidavit.eci.gov.in")

wait = WebDriverWait(driver, 20)

form = wait.until(EC.presence_of_element_located((By.ID, "CandidateCustomFilter")))
-
select1 = Select(form.find_element(By.ID, "electionType"))
select1.select_by_visible_text("Election-Oct-Dec-2023")
time.sleep(2)

select2 = Select(form.find_element(By.ID, "election"))
select2.select_by_visible_text("AC - GENERAL")
time.sleep(2)

select3 = Select(form.find_element(By.ID, "states"))
select3.select_by_visible_text("Telangana")
time.sleep(2)

phase_dropdown = wait.until(EC.presence_of_element_located((By.ID, "phase")))
Select(phase_dropdown).select_by_index(1)  # skip "Select Phase"
time.sleep(2)

const_dropdown = wait.until(EC.presence_of_element_located((By.ID, "constId")))
Select(const_dropdown).select_by_visible_text("Select Constituency")
time.sleep(2)

filter_button = form.find_element(By.CSS_SELECTOR, "button.btn.search.btn-primary")
filter_button.click()



time.sleep(20)
