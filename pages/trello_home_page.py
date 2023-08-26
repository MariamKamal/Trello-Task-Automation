# trello_home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TrelloHomePage:
    def __init__(self, driver):
        self.driver = driver

    def create_board_directly(self, board_name, api_key, api_token):
        create_board_button = self.driver.find_element(By.XPATH, "//button[contains(@data-testid, 'header-create-board-button')]")
        create_board_button.click()

        board_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-testid='create-board-title-input']"))
        )
        board_name_input.send_keys(board_name)
        board_name_input.send_keys(Keys.ENTER)

        # Use api_key and api_token for API requests
        print("API Key:", api_key)
        print("API Token:", api_token)
