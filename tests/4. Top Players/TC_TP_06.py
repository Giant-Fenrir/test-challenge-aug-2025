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
    test_filter_top_50(driver)
    driver.quit()


def test_filter_top_50(driver):
    """
    ID: TC-TP-06
    Title: Filter Top 50
    Description: To verify if returns a list with top 50 players with 13 pages
    Steps:  1. Go to Top Players
            2. Click Clear filters
            3. Select top 50
            4. Click search
    Expected result: A list with 13 pages and a total of 50 players will be displayed
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/top")

    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[1]/select").click()
    driver.find_element(By.XPATH, "//option[@value='50']").click()
    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)
    
    driver.find_element(By.XPATH, "//div[@class='number ' and text()='13']").click()
    time.sleep(0.5)

    players = driver.find_elements(By.CLASS_NAME, "player")
    print(len(players))

    if len(players) == 2:
        result += "[SUCCESS]: Top 50 players returned by filter"
    else:
        result += "[FAIL]: Top 50 players not returned by filter"
        status = False

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='14']")
        result += "\n[FAIL]: Result with incorrect amount of pages"
        status = False
    except:
        result += "\n[SUCCESS]: Result with 13 pages, as expected"
    
    test_result(status, result, "Top Player", "TC-TP-06")

browser()
