import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook

def test_result(status, result, item, name):
    try:
        wb = load_workbook("res/test_results.xlsx")
        ws = wb.active
        ws.append([item, name, result, "PASS" if status else "FAIL"])
        wb.save("res/test_results.xlsx")
    except:
        print("Please run all tests with init.py")

def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(0.5)
    test_search_player_by_nationality(driver)
    driver.quit()


def test_search_player_by_nationality(driver):
    """
    ID: TC-SP-07
    Title: Search players by nationality
    Description: Verify if the search returns all players from given nationality
    Steps:  1. Go to Search Player
            2. Click Clear filters
            3. Select a nationality
            4. Click search
    Expected result: A list with all players containig the selected nationality should be displayed
    """
    status = True
    result = ""

    driver.get("http://localhost:3001/search")

    Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[4]/select")).select_by_value("Brazil")
    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='4736']")
        result += "[FAIL]:Filter not applied"
        status = False
    except:
        result += "[SUCCESS]:Filter applied"
    
    test_result(status, result, "Player List", "TC-SP-07")

browser()