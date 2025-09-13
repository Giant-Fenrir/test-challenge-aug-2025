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
    test_list_all_players(driver)
    driver.quit()


def test_list_all_players(driver):
    """
    ID: TC-PL-01
    Title: List all players
    Description: Verify if all players are being displayed.
    Steps:  1.Go to Player List
    Expected result: A list with 3789 pages and a total of 18.944 players will be displayed
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/list")

    players = driver.find_elements(By.CLASS_NAME, "player")
    if len(players) == 5:
        result += "[SUCCESS]: 5 players displayed on default page"
    else:
        result += "[FAIL]: Incorrect amount of players displayed on default page"
        status = False
    
    numbers = driver.find_elements(By.CLASS_NAME, "number")
    if numbers[3].text == "3789":
        result += "\n[SUCCESS]: 3789 pages displayed correctly"
    else:
        result += "\n[FAIL]: Incorrect amount of pages displayed"
        status = False

    test_result(status, result, "Player List", "TC-PL-01")

browser()