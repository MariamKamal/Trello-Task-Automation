import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import BOARD_NAME,card_titles, password , username
from utils.utils import login,click_board

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def add_cards(driver, card_titles):
    for card_title in card_titles:
        # Find the "Add Card" button and click it (only for the first card)
        if card_titles.index(card_title) == 0:
            add_card_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-composer-container .open-card-composer"))
            )
            add_card_button.click()

        # Wait for the card title input field to be visible
        card_title_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-card-composer-textarea"))
        )
        card_title_input.send_keys(card_title)

        # Find the "Add Card" or "Add Card" submit button and click it
        if card_titles.index(card_title) == 0:
            button_locator = (By.CSS_SELECTOR, ".nch-button.nch-button--primary.confirm.mod-compact.js-add-card")
        else:
            button_locator = (By.CSS_SELECTOR, ".js-add-card")
        
        add_card_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        add_card_submit_button.click()

def test_login_and_add_cards(driver):    

    login(driver, username, password)
    click_board(driver, BOARD_NAME)
    add_cards(driver, card_titles)
    driver.quit()
