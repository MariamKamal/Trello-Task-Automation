from config import BOARD_NAME,card_titles, password , username
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def login(driver, username, password):
    driver.get("https://trello.com/login")
    
    username_input = driver.find_element(By.ID, "user")
    username_input.send_keys(username)

    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    wait = WebDriverWait(driver, 10)
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, "#login-submit")
    login_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "boards-page-board-section-list-item")))

def click_board(driver, BOARD_NAME):
    board_xpath = f"//div[contains(text(), '{BOARD_NAME}')]"
    board_element = driver.find_element(By.XPATH, board_xpath)
    board_element.click()

    time.sleep(2)