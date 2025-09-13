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
    test_pagination_TP(driver)
    driver.quit()


def test_pagination_TP(driver):
    """
    ID: TC-TP-12
    Title: Pagination checklist - Top Player
    Description: Check every pagination function in Top Player screen
    Steps:  1. Go to Top Players
            2. Click Clear filters
            3. Click Search
            4. Click any page number
            5. Click First
            6. Click Last
            7. Click Previous
            8. Click Next
    Expected result: Every click should lead to a diferent page  containing different players
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/top")

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='2']").click()
        result += "[SUCCESS]:Could click page 2"
    except:
        result += "[FAIL]:Could not click page 2"
        status = False

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcut' and text()='First']").click()
        result += "\n[SUCCESS]:Could click First"
    except:
        result += "\n[FAIL]:Could not click First"
        status = False

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcut' and text()='Last']").click()
        result += "\n[SUCCESS]:Could click Last"
    except:
        result += "\n[FAIL]:Could not click Last"
        status = False

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcut' and text()='Previous']").click()
        result += "\n[SUCCESS]:Could click Previous"
    except:
        result += "\n[FAIL]:Could not click Previous"
        status = False

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcut' and text()='Next']").click()
        result += "\n[SUCCESS]:Could click Next"
    except:
        result += "\n[FAIL]:Could not click Next"
        status = False
    
    test_result(status, result, "Top Player", "TC-TP-12")
    
browser()
