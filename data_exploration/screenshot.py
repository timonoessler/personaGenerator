import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from meta import question_meta

BASE_URL = "http://localhost:8501"
OUTDIR   = "screenshots"
os.makedirs(OUTDIR, exist_ok=True)

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

keys = [k for k, m in question_meta.items() if m['type'] != 'group']

for key in keys:
    url = f"{BASE_URL}?selection={key}&compare=true"
    driver.get(url)
    time.sleep(2)
    fname = os.path.join(OUTDIR, f"{key}.png")
    driver.save_screenshot(fname)
    print(f"→ saved screenshot: {fname}")

driver.quit()
