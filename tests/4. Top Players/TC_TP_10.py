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
    test_top_players_by_league(driver)
    driver.quit()


def test_top_players_by_league(driver):
    """
    ID: TC-TP-10
    Title: List all top players given a league
    Description: Verify if a list of top players will be shown given a league
    Steps:  1. Go to Top Players
            2. Click Clear filters
            3. Select any top x
            4. Select a league
            5. Click Search
    Expected result: A list of top X players from the selected league should be displayed
    """
    status = True
    result = ""

    driver.get("http://localhost:3001/top")

    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[1]/select").click()
    driver.find_element(By.XPATH, "//option[@value='3']").click()
    Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[2]/select")).select_by_value("Italian Serie A")
    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='2']")
        result += "[FAIL]:Filter not applied"
        status = False
    except:
        result += "[SUCCESS]:Filter applied"
    
    test_result(status, result, "Top Player", "TC-TP-10")

browser()
