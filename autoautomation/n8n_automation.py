import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Setup Chrome driver
service = ChromeService()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Go to the workflow editor (redirects to login if needed)
    driver.get("https://samarthnaik.app.n8n.cloud/workflow/new?projectId=24sqPJwfo6bt66lv")
    time.sleep(3)

    try:
        # Use lower-case 'type' for selectors — always lowercase in HTML
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
        )
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )

        # Fill email and password
        email_input.clear()
        email_input.send_keys("samarth.naik024@gmail.com")
        password_input.clear()
        password_input.send_keys("doskaM-vednu3-ravsat")

        print("✅ Email and password filled. Please click 'Sign In' manually.")
    except Exception as e:
        print("❌ Could not fill credentials:", e)
        driver.save_screenshot("error_login_fill.png")

    # Wait up to 2 mins for '+' button (after manual login)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='canvas-plus-button']"))
    )
    print("✅ '+' button detected. Clicking to add node.")
    add_button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='canvas-plus-button']")
    driver.execute_script("arguments[0].click();", add_button)
    time.sleep(1)

    # Just type 'Webhook' and press Enter (search bar is already focused)
    actions = webdriver.ActionChains(driver)
    actions.send_keys("Webhook").pause(1).send_keys(Keys.ENTER).perform()

    print("✅ Typed 'Webhook' and pressed Enter.")
    time.sleep(3)  # Wait for the node to appear


finally:
    driver.quit()
