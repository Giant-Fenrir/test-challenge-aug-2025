from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium import webdriver

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
    driver.implicitly_wait(10)
    test_pagination_PL(driver)
    driver.quit()


def test_pagination_PL(driver):
    """
    ID: TC-PL-02
    Title: Pagination checklist - Player List
    Description: Check every pagination function in Player List screen
    Steps:  1. Go to Player List
            2. Click any page number
            3. Click First
            4. Click Last
            5. Click Previous
            6. Click Next
    Expected result: Every click should lead to a diferent page  containing different players
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/list")

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
    
    test_result(status, result, "Player List", "TC-PL-02")
    
browser()
