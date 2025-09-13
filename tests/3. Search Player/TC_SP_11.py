from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    test_pagination_restrictions_SP(driver)
    driver.quit()


def test_pagination_restrictions_SP(driver):
    """
    ID: TC-SP-11
    Title: Pagination restriction checklist - Search Player
    Description: Check every restriction to pagination function in Search Player screen
    Steps:  1. Go to Search Player
            2. Click Clear filters
            3. Click Search
            4. Click any page number
            5. Click First
            6. Click Last
            7. Click Previous
            8.Click Next
    Expected result: The first|previous buttons should not be clickable while in the first page and the last|next buttons should not be clickable in the last page
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/search")

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
        

    driver.find_element(By.XPATH, "//div[@class='number ' and text()='4736']").click()

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
        

    test_result(status, result, "Player List", "TC-SP-11")

browser()