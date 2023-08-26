# Trello Automation Test Project

This project aims to automate testing of Trello task management functionality using both the both through its UI and REST API.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Using a Virtual Environment](#using-a-virtual-environment)
- [Running Tests](#running-tests)
- [Tests](#tests)
  - [Create Board API Test](#create-board-api-test)
  - [Add Lists to Board API Test](#add-lists-to-board-api-test)
  - [Add Cards to List UI Test](#add-cards-to-list-ui-test)
  - [Verify Cards Created via API](#verify-cards-created-via-api)
  - [Move Cards between Lists UI Test](#move-cards-between-lists-ui-test)
  - [Edit Card via UI Test](#edit-card-via-ui-test)
- [Potential Improvements and Future Work](#potential-improvements-and-future-work)
  - [UI Test Considerations](#ui-test-considerations)
  - [Project Structure and Design Improvements](#project-structure-and-design-improvements)


## Introduction
This project automates testing scenarios for the Trello task management tool. It combines API tests using Python's requests library and UI tests using Selenium to ensure the functionality is working as expected.

## Prerequisites
- Python 3.x installed
- Trello account
- Trello API key and token
- Selenium WebDriver (e.g., ChromeDriver) installed
- Chrome browser (or the browser supported by the WebDriver)

## Installation
1. Clone the repository: `git clone ??
2. Navigate to the project folder: `cd trello-automation`
3. Install dependencies: `pip install -r requirements.txt`

## Configuration
Edit the `config.py` file to set up your Trello API key, token, and other configuration parameters.
Using a Virtual Environment
It's highly recommended to use a virtual environment to manage your project's dependencies, ensuring they don't interfere with other projects or your system-wide Python installation. Here's a step-by-step guide to set it up:

Navigate to your project directory using the terminal.

Create a virtual environment (replace 'venv_name' with your preferred environment name):

On Windows:

bash
Copy code
python -m venv venv_name
On macOS and Linux:

bash
Copy code
python3 -m venv venv_name
Activate the virtual environment:

On Windows:

bash
Copy code
venv_name\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv_name/bin/activate
With the virtual environment active, install the necessary project dependencies using pip:

bash
Copy code
pip install pytest requests selenium beautifulsoup4 pytest-html pytest-json
By following these steps, you'll create an isolated environment for your project's dependencies, promoting a seamless development experience while working on your automation tasks.



### Running Tests


Before you run the tests, make sure you have completed the necessary configurations and installations as mentioned in the previous sections.

1. **Activate Virtual Environment:** If you're using a virtual environment, activate it using the appropriate command:
   
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate

2. **Navigate to the Project Directory:** Open a terminal and navigate to the project directory that contains your test files.

3. **Execute the Test Suite:** To run the test suite, use the following command:

`pytest --html=report.html --json=report.json -s tests/Test_name.py`
- The `-s` option allows output to be printed directly to the console in real-time as the tests run. This is useful for debugging purposes, as it provides immediate feedback on the progress of the test suite.
- The `--html=report.html` option generates an HTML report of the test results and saves it in a file named `report.html`.
- The `--json=report.json` option generates a JSON report of the test results and saves it in a file named `report.json`.

The generated HTML report (`report.html`) provides an interactive view of the test results, including detailed information about test cases, failures, and other relevant statistics.

**Note:** The HTML and JSON reports will be generated in the same directory where you executed the `pytest` command.

The test suite will run through the specified test cases, both API and UI, and provide you with comprehensive results in the generated reports. This will help you assess the status of your Trello Automation Test Project.

### Tests

### Create Board API Test
This test verifies the successful creation of a new Trello board using the API.
Before running the test, make sure to edit the `config.py` file to set the appropriate parameters:

1. Open the `config.py` file located in the project directory.
2. Locate the following line:
   ```python
   BOARD_NAME = "Test Board1"
Replace "Test Board1" with your desired board name.
Running the Test
Once you have configured the board name in the config.py file, you can run the test as follows:


Run the test using the following command:
`pytest  --html=report.html --json=report.json -s tests/test_create_board.py`


The test will use the board name you configured in the config.py file to create a Trello board via the API and verify its successful creation.

Note: When creating a board, Trello automatically adds three default lists ("To Do", "Doing", "Done"). To start with a clean slate, I've included a step in the test case to archive these default lists before proceeding to create my own lists.

To ensure this we need to run the following command:
 `pytest -s tests/test_Archive_Lists.py`


### Add Lists to Board API Test
This test adds lists to a created board using the Trello API and verifies their addition.

Before running the test, configure the desired list names in `config.py`.

To run the test:
1. Set up the list names in `config.py`.
2. Run the test using the command:
   `pytest --html=report.html --json=report.json -s tests/test_add_lists_to_board.py`



### Add Cards to List UI Test
This UI test uses Selenium to log in to Trello, navigate to a board, and add cards to a list. It then verifies the addition of cards.

Before running the test, make sure to edit the `config.py` file to set the appropriate parameters:
- `card_titles` = ["Requirement Analysis", "Scenario Identification"]

Replace this list with your desired card titles.

To run the test:
1. Configure the desired card titles in `config.py`.
2. Run the test using the command:
   `pytest --html=report.html --json=report.json -s tests/test_create_cards_viaUI.py`

### Verify Cards Created via API
This test retrieves cards created via the API and verifies their presence on the Trello board.
Before running the test, make sure to edit the `config.py` file to set the appropriate parameters:
Before running the test, make sure to edit the `config.py` file to set the appropriate parameters:
- `BOARD_NAME` = "Test final"
- `LIST_NAME` = "To Do"
- `card_titles` = ["Requirement Analysis", "Scenario Identification"]

Replace these parameters with your desired board name, list name, and card titles.

To run the test:
1. Configure the board name, list name, and card titles in `config.py`.
2. Run the test using the command:
   `pytest --html=report.html --json=report.json -s tests/test_verify_created_cards_viaAPI.py`

The console output will provide the status of each card created, indicating whether it was successfully created or if there were any failures.
eated or if there were any failures during the creation process. This will help you quickly assess the results of the test run and identify any issues that may have occurred during card creation.

### Edit Card via UI Test
This UI test uses Selenium to verifies the ability to edit card details using the Trello user interface editing description.

Before running the test, make sure to edit the `config.py` file to set the appropriate parameters:
- `card_title` = "Scenario Identification"
- `new_card_description` = "this is updated card description"

Replace these parameters with your desired card title and new card description.

To run the test:
1. Configure the card title and new card description in `config.py`.
2. Run the test using the command:
   `pytest --html=report.html --json=report.json -s tests/test_edit_card_viaUI.py`


### Move Cards between Lists UI Test
This UI test uses Selenium to move cards from one list to another on a Trello board. It verifies the successful movement of cards.

Before running the test, make sure to edit the `config.py` file to set the appropriate parameters:
- `card_title` = "Scenario Identification"
- `destination_list` = "Done"

Replace these parameters with your desired card title and destination list name.

To run the test:
1. Configure the card title and destination list name in `config.py`.
2. Run the test using the command:
   `pytest --html=report.html --json=report.json -s tests/test_move_cards_betweenLists_viaUI.py`





### Potential Improvements and Future Work

While I've completed the automation tasks outlined in this project, there are always opportunities for improvement and additional features. If I had more time, here are a few things I might consider

## UI Test Considerations

While my UI tests successfully validate the application's behavior, there are certain areas where improvements could be made for increased flexibility and robustness. Notably, the current implementation relies heavily on HTML element identifiers, which can be limiting in some scenarios. Here are a few insights and considerations:

### Flexible Element Identification

In some UI tests, like the one for creating cards on a list, I observed that the test is currently designed to focus on the first list using specific HTML element identifiers. While this works for the provided scenario, it can lead to issues if the structure of the page changes or if the test needs to interact with different lists.

**What I Would Improve:** To enhance the flexibility of my UI tests, I would explore using more dynamic and robust ways to locate elements, such as using CSS classes, data attributes, or XPath queries. This approach would make the tests less dependent on specific HTML structures and better equipped to handle changes in the application's layout.

### Data-Driven Testing

Another consideration is implementing data-driven testing, where test data is stored externally and fed into the tests. This approach would allow for testing various scenarios using different datasets without modifying the test code.

**What I Would Improve:** I would implement data-driven testing by creating data files or using a test data management tool. This would make it easy to test different lists, cards, and user interactions without modifying the test logic each time.

### Comprehensive Validation

While my current tests validate basic functionality, adding more assertions to verify UI elements, text, and layouts could provide a more comprehensive validation of the user interface.

**What I Would Improve:** I would extend the test assertions to cover additional UI elements and their properties, ensuring a thorough validation of the application's visual components.

By addressing these considerations and implementing more flexible and robust strategies, the UI tests could be enhanced to handle a wider range of scenarios and better accommodate changes in the application over time.


## Project Structure and Design Improvements

While building this test automation project, I recognized opportunities to enhance the project's structure and design, making it more organized, maintainable, and reusable. Here are a few key areas where I believe improvements could have been made:

### Applying the Page Object Model (POM)

In the current project structure, each UI test interacts with HTML elements directly, which can lead to code duplication and maintenance challenges as the application evolves. One effective way to address this is by adopting the Page Object Model (POM) design pattern.

**What I Could Have Done Differently:** I could have organized my code by creating separate classes for each page or screen of the application. These classes, known as Page Objects, encapsulate the interactions and operations specific to that page. This approach would have made my tests more modular, readable, and maintainable, as any changes to the UI would only require updating a single location—the corresponding Page Object.

### Enhancing Code Reusability

While my current test scripts effectively validate the specified scenarios, I've already taken steps to enhance code reusability by creating separate functions for common interactions. For example:

- I've encapsulated the login process into a reusable `login` function. This allows me to perform consistent and controlled logins across multiple tests, eliminating the need to duplicate the login code in each test script.

- I've also created a function `click_board` that abstracts the process of selecting a specific board to work with. This function helps me avoid repeating the same steps to navigate to the desired board, making my test scripts cleaner and more focused on the test objectives.

**What I Could Have Done Differently:** While these initial steps have improved code reusability, I could further extend this concept by identifying additional common interactions or actions across different parts of the application. By encapsulating these interactions into functions, I could ensure consistency, reduce code duplication, and make it even easier to add new tests without the burden of redundant setup and navigation code.

By applying this approach more extensively, I would create a more streamlined testing process that emphasizes code reusability, maintainability, and scalability.

### Centralized Configuration Management

While my project includes a configuration file, I could have enhanced its capabilities to manage test data, URLs, and other settings centrally.

**What I Could Have Done Differently:** I could have used a configuration management library or approach to store and retrieve configuration values dynamically. This would have allowed for easier modification of test parameters without editing code directly.

By incorporating these improvements into the project structure and design, I would have created a more scalable and maintainable automation framework that supports efficient test development, maintenance, and expansion over time.
