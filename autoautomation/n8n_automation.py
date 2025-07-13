import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def open_n8n_workflow(driver):
    url = "https://samarthnaik.app.n8n.cloud/workflow/new?projectId=24sqPJwfo6bt66lv"
    driver.get(url)
    time.sleep(3)

def fill_login_credentials(driver):
    try:
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
        )
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )

        email_input.clear()
        email_input.send_keys("samarth.naik024@gmail.com")
        password_input.clear()
        password_input.send_keys("doskaM-vednu3-ravsat")

        print("✅ Email and password filled. Please click 'Sign In' manually.")
    except Exception as e:
        print("❌ Could not fill credentials:", e)
        driver.save_screenshot("error_login_fill.png")

def add_webhook_node(driver, method="GET"):
    print("🚀 Configuring Webhook node...")
    wait = WebDriverWait(driver, 20)

    try:
        driver.save_screenshot("webhook_opened.png")

        # === Set HTTP Method ===
        combobox_inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[role='combobox']")))
        ActionChains(driver).move_to_element(combobox_inputs[0]).click().send_keys(method).pause(1).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        print(f"✅ HTTP Method: {method}")
        time.sleep(1.5)

        # === Back to Canvas ===
        print("Attempting to return to canvas...")
        back_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test-id='back-to-canvas']")))
        driver.execute_script("arguments[0].click();", back_btn)
        print("🔙 Returned to canvas.")

    except Exception as e:
        print("❌ Failed to configure Webhook node:", e)
        driver.save_screenshot("webhook_node_error.png")

def add_node(driver, node_name):
    """Adds a new node to the canvas by pressing TAB and then searching."""
    print(f"🚀 Adding '{node_name}' node...")
    wait = WebDriverWait(driver, 20)
    try:
        # Press TAB to focus the search input on the existing node
        ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(1)

        # Type the node name and press Enter
        ActionChains(driver).send_keys(node_name).pause(1).send_keys(Keys.ENTER).perform()
        print(f"✅ '{node_name}' node added via search.")
        time.sleep(3)

        # === Back to Canvas ===
        print("Attempting to return to canvas...")
        back_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test-id='back-to-canvas']")))
        driver.execute_script("arguments[0].click();", back_btn)
        print("🔙 Returned to canvas.")

    except Exception as e:
        print(f"❌ Failed to add '{node_name}' node:", e)
        driver.save_screenshot(f"{node_name.lower().replace(' ', '_')}_node_error.png")

def add_brave_search_node(driver):
    """Adds the Brave Search node with a double enter."""
    print("🚀 Adding 'Brave Search' node...")
    wait = WebDriverWait(driver, 20)
    try:
        # Press TAB to focus the search input on the existing node
        ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(1)

        # Type the node name and press Enter twice
        ActionChains(driver).send_keys("Brave Search").pause(1).send_keys(Keys.ENTER).pause(1).send_keys(Keys.ENTER).perform()
        print("✅ 'Brave Search' node added via search.")
        time.sleep(3)

        # === Back to Canvas ===
        print("Attempting to return to canvas...")
        back_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test-id='back-to-canvas']")))
        driver.execute_script("arguments[0].click();", back_btn)
        print("🔙 Returned to canvas.")

    except Exception as e:
        print("❌ Failed to add 'Brave Search' node:", e)
        driver.save_screenshot("brave_search_node_error.png")

def add_google_sheets_node(driver):
    """Adds a Google Sheets node and selects an action within it."""
    print("🚀 Adding 'Google Sheets' node...")
    wait = WebDriverWait(driver, 20)
    try:
        # Press TAB to focus the search input on the existing node
        ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(1)

        # Type the node name and press Enter
        ActionChains(driver).send_keys("Google Sheets").pause(1).send_keys(Keys.ENTER).perform()
        print("✅ 'Google Sheets' node added via search.")
        time.sleep(3)

        # The internal search is already focused. Type the action and press Enter.
        ActionChains(driver).send_keys("Append row in sheet").pause(1).send_keys(Keys.ENTER).perform()
        print("✅ Selected 'Append row in sheet' action.")
        time.sleep(3)

        # === Back to Canvas ===
        print("Attempting to return to canvas...")
        back_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test-id='back-to-canvas']")))
        driver.execute_script("arguments[0].click();", back_btn)
        print("🔙 Returned to canvas.")

    except Exception as e:
        print("❌ Failed to add 'Google Sheets' node:", e)
        driver.save_screenshot("google_sheets_node_error.png")


def wait_for_plus_and_click(driver):
    try:
        WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='canvas-plus-button']"))
        )
        add_button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='canvas-plus-button']")
        driver.execute_script("arguments[0].click();", add_button)
        print("✅ '+' button clicked.")
        time.sleep(2)
    except Exception as e:
        print("❌ '+' button failed:", e)
        driver.save_screenshot("error_plus_button.png")

def search_and_add_webhook(driver):
    try:
        # After clicking the plus button, the search input is focused.
        actions = ActionChains(driver)
        actions.send_keys("Webhook").pause(1).send_keys(Keys.ENTER).perform()
        print("✅ Webhook node added via search.")
        time.sleep(3)
    except Exception as e:
        print("❌ Webhook search/add failed:", e)
        driver.save_screenshot("error_webhook_add.png")

def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        open_n8n_workflow(driver)
        fill_login_credentials(driver)
        wait_for_plus_and_click(driver)
        search_and_add_webhook(driver)
        add_webhook_node(driver, method="POST")
        add_brave_search_node(driver)
        add_node(driver, "AI Agent")
        add_google_sheets_node(driver)
        print("⏳ Waiting for 5 seconds to observe the result...")
        time.sleep(5)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()