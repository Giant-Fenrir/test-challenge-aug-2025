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
    test_best_team_by_nationality(driver)
    driver.quit()


def test_best_team_by_nationality(driver):
    """
    ID: TC-TT-03
    Title: List the best players from a nationality to form a team
    Description: Verify if, given a nationality, the best players to form a team will be shown
    Steps:  1. Go to Top Team
            2. Click Clear Filters
            3. Select a nationality
            4. Click Search
    Expected result: A top team filtered by nationality should be displayed
    """
    status = True
    result = ""

    driver.get("http://localhost:3001/team")

    Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[2]/select")).select_by_value("Brazil")
    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)

    try:
        driver.find_element(By.XPATH, ("//span[@class='title' and text()='Alisson']"))
        result += "[SUCCESS]:Filter applied"
    except:
        result += "[FAIL]:Filter not applied"
        status = False

    test_result(status, result, "Top Team", "TC-TT-03")

browser()