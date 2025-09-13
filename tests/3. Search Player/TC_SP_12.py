import time
from selenium import webdriver
from openpyxl import load_workbook
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
    test_pagination_adjust_SP(driver)
    driver.quit()


def test_pagination_adjust_SP(driver):
    """
    ID: TC-SP-12
    Title: Pagination according with number of players - Search Player
    Description: Verify if pagination is set according to number of players
    Steps:  1. Go to Search Player
            2. Click Clear filters
            3. Add filters that will return only 1 player.
            4. Click search
    Expected result: Search should return only 1 player and number of pages should adjust to 1.
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/search")

    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[1]/input").send_keys("Neymar")

    driver.find_element(By.CLASS_NAME, "search").click()
    time.sleep(0.5)

    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='2']")
        result += "[FAIL]:1 Player should not return more than 1 page"
        status = False
    except:
        result += "[SUCCESS]:Only one page, as expected"

    test_result(status, result, "Player List", "TC-SP-12")

browser()
