import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import BOARD_NAME,card_titles, password , username,card_title,destination_list
from utils.utils import login,click_board

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def move_cards(driver, card_title, destination_list):
    card_xpath = f"//span[contains(text(), '{card_title}')]/ancestor::a[contains(@class, 'list-card')]"
    card_element = driver.find_element(By.XPATH, card_xpath)

    time.sleep(3)
    # Click the card to open it for editing
    card_element.click()
    time.sleep(3)

    move_button = driver.find_element(By.CLASS_NAME, "button-link.js-move-card")
    move_button.click()

    list_dropdown_xpath = "//select[@class='js-select-list']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, list_dropdown_xpath)))

    # Wait for the "List" options to appear
    #list_options_xpath = "//select[@class='js-select-list']//option[contains(text(), 'Doing')]"
    list_option_xpath = f"//select[@class='js-select-list']//option[text()='{destination_list}']"
    list_options_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, list_option_xpath)))

    # Click the list options and choose "Doing"
    list_options_element.click()
    time.sleep(3)
    
    # Click the "Move" button
    move_button_xpath = "//input[@data-testid='move-card-popover-move-button']"
    move_button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, move_button_xpath)))

    # Click the "Move" button
    move_button_element.click()


def test_login_and_move_card(driver):


    login(driver, username, password)
    click_board(driver, BOARD_NAME)
    move_cards(driver,card_title,destination_list)
    driver.quit()
