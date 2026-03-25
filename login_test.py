from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting Selenium Login Test...")

# Create a new Chrome browser instance
driver = webdriver.Chrome()

try:
    # Step 1: Open the login page
    print("Opening login page...")
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(3)  # Wait for page to load

    # Step 2: Enter username
    print("Entering username...")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    time.sleep(2)

    # Step 3: Enter password
    print("Entering password...")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(2)

    # Step 4: Click login button
    print("Clicking login button...")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(3)

    # Step 5: Verify login was successful
    # Check if we're on the secure area page
    current_url = driver.current_url
    if "secure" in current_url:
        print("✅ TEST PASSED: Successfully logged in!")
        
        # Look for success message
        try:
            success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
            print(f"Message: {success_message.text}")
        except:
            print("No success message found")
    else:
        print("❌ TEST FAILED: Login unsuccessful")

    # Step 6: Take a screenshot (for your lab submission)
    driver.save_screenshot("login_test_result.png")
    print("Screenshot saved as 'login_test_result.png'")

except Exception as e:
    print(f"❌ ERROR: {e}")

finally:
    # Wait a bit before closing
    time.sleep(5)
    # Close the browser
    driver.quit()
    print("Test completed!")