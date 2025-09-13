import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    test_filter_top_10(driver)
    driver.quit()


def test_filter_top_10(driver):
    """
    ID: TC-TP-04
    Title: Filter Top 10
    Description: To verify if returns a list with top 10 players with 3 pages
    Steps:  1. Go to Top Players
            2. Click Clear filters
            3. Select top 10
            4. Click search
    Expected result: A list with 3 pages and a total of 10 players will be displayed
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/top")

    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[1]/select").click()
    driver.find_element(By.XPATH, "//option[@value='10']").click()
    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)
    
    driver.find_element(By.XPATH, "//div[@class='number ' and text()='3']").click()
    time.sleep(0.5)

    players = driver.find_elements(By.CLASS_NAME, "player")
    print(len(players))

    if len(players) == 2:
        result += "[SUCCESS]: Top 10 players returned by filter"
    else:
        result += "[FAIL]: Top 10 players not returned by filter"
        status = False

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='4']")
        result += "\n[FAIL]: Result with incorrect amount of pages"
        status = False
    except:
        result += "\n[SUCCESS]: Result with 3 pages, as expected"
    
    test_result(status, result, "Top Player", "TC-TP-04")

browser()
