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
    test_pagination_adjust_TP(driver)
    driver.quit()


def test_pagination_adjust_TP(driver):
    """
    ID: TC-TP-14
    Title: Pagination according with number of players - Top Players
    Description: Verify if pagination is set according to number of players
    Steps:  1. Go to Top Players
            2. Click Clear filters
            3. Select Top 3
            4. Select a filter that will return only 1 player
            5. Click Search
            6. Repeat steps 3,4 and 5 for top 5, 10, 25, 50 and 100
    Expected result: Search should return only 1 player and number of pages should remain 1 with all top X options.
    """
    status = True
    result = ""

    driver.get("http://localhost:3001/top")

    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[1]/select").click()
    driver.find_element(By.XPATH, "//option[@value='100']").click()
    Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[2]/select")).select_by_value("English Premier League")
    Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[3]/select")).select_by_value("Poland")
    Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[4]/select")).select_by_value("GK")
    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='2']")
        result += "[FAIL]:Pagination adjusted incorrectly, more than 1 page"
        status = False
    except:
        result += "[SUCCESS]:Pagination adjusted correctly, only 1 page"
    
    test_result(status, result, "Top Player", "TC-TP-14")

browser()