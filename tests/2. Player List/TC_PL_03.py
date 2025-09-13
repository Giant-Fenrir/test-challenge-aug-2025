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
    driver.implicitly_wait(10)
    test_pagination_restrictions_PL(driver)
    driver.quit()


def test_pagination_restrictions_PL(driver):
    """
    ID: TC-PL-03
    Title: Pagination restriction checklist - Player List
    Description: Check every restriction to pagination function in Player List screen
    Steps:  1. Go to Player List
            2. Select the fisrt page
            3. Click Previous
            4. Click First
            5. Select the last page
            6. Click Next
            7. Click Last
    Expected result: The first|previous buttons should not be clickable while in the first page and the last|next buttons should not be clickable in the last page
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/list")

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcutunavailable' and text()='First']")
        result += "[SUCCESS]:Could not click First in first page, as expected"
    except:
        result += "[FAIL]:First should not be clickable in first page"
        status = False
        
    
    try:
        driver.find_element(By.XPATH, "//span[@class='shortcutunavailable' and text()='Previous']")
        result += "\n[SUCCESS]:Could not click Previous in first page, as expected"
    except:
        result += "\n[FAIL]:Previous should not be clickable in first page"
        status = False
        

    driver.find_element(By.XPATH, "//div[@class='number ' and text()='3789']").click()

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcutunavailable' and text()='Next']")
        result += "\n[SUCCESS]:Could not click Next in last page, as expected"
    except:
        result += "\n[FAIL]:Next should not be clickable in last page"
        status = False
        

    try:
        driver.find_element(By.XPATH, "//span[@class='shortcutunavailable' and text()='Last']")
        result += "\n[SUCCESS]:Could not click Last in last page, as expected"
    except:
        result += "\n[FAIL]:Last should not be clickable in last page"
        status = False
        

    test_result(status, result, "Player List", "TC-PL-03")

browser()
