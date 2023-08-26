import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import BOARD_NAME,card_titles, password , username ,card_title, new_card_description
from utils.utils import login,click_board
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


'''   
def edit_card_title(driver, card_title, new_title):

    card_xpath = f"//span[contains(text(), '{card_title}')]/ancestor::a[contains(@class, 'list-card')]"
    card_element = driver.find_element(By.XPATH, card_xpath)

    time.sleep(3)
    # Click the card to open it for editing
    card_element.click()
    time.sleep(3)

    # Wait for the title input to be present
    wait = WebDriverWait(driver, 10)
    title_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".js-card-detail-title-input")))

    # Find the card title element and clear the existing title
    title_input.clear()


    # Enter the new title
    title_input.send_keys(new_title)

    time.sleep(5)
    # Simulate a click outside the title area to trigger the save action
    actions = ActionChains(driver)
    actions.move_by_offset(1, 1)  # Move to a neutral position on the page
    actions.click()               # Perform a click action
    actions.perform()             # Perform the actions
    '''    
def edit_card_description(driver, card_title, new_card_description):
    card_xpath = f"//span[contains(text(), '{card_title}')]/ancestor::a[contains(@class, 'list-card')]"
    card_element = driver.find_element(By.XPATH, card_xpath)

    time.sleep(3)
    # Click the card to open it for editing
    card_element.click()
    time.sleep(3)

    # Check if there's an existing description
    try:
        edit_button = driver.find_element(By.CSS_SELECTOR, ".js-edit-desc")  # Edit button for existing description
        edit_button.click()

        # Wait for the description input to be present
        description_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ak-editor-textarea"))  # Update the locator as needed
        )
    except NoSuchElementException:
        # If no existing description, click to reveal the description input field
        description_link = driver.find_element(By.CSS_SELECTOR, ".js-description-fake-text-area")
        description_link.click()
        time.sleep(6)

        # Wait for the description input to be present
        description_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ak-editor-textarea"))  # Update the locator as needed
        )
    time.sleep(6)
    # Clear the existing content of the description input field
    description_input.clear()
    time.sleep(3)

    # Input the new description text
    description_input.send_keys(new_card_description)

    # click the Save button
    save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.confirm[type='button']"))
   )
    save_button.click()

    time.sleep(5)

    
    
def test_login_and_edit_card_Details(driver):


    login(driver, username, password)
    click_board(driver, BOARD_NAME)
    #edit_card_title(driver, "Requirement Analysis", "New Requirement Analysis rt")
    edit_card_description(driver, card_title, new_card_description)
    driver.quit()
