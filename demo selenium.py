from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
service = Service("chromedriver.exe")  # Update the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Accept cookies (if the cookie consent banner appears)
    try:
        accept_cookies_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept all')]"))
        )
        accept_cookies_button.click()
    except Exception:
        print("No cookie consent button found, continuing...")

    # Wait for the search box to load
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Enter the search query
    search_query = "Selenium Python"
    search_box.send_keys(search_query)

    # Submit the search
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load and capture the title of the results page
    WebDriverWait(driver, 10).until(EC.title_contains(search_query))
    print("Page Title:", driver.title)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
