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
    test_top_players_all_players(driver)
    driver.quit()


def test_top_players_all_players(driver):
    """
    ID: TC-TP-01
    Title: List top players by their overall
    Description: To verify if a list of top player by their overall will be shown by default
    Steps:  1. Go to Top Players
    Expected result: A list with 2 pages and a total of 5 players will be displayed
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/top")

    players = driver.find_elements(By.CLASS_NAME, "player")
    if len(players) == 4:
        result += "[SUCCESS]:4 players displayed"
    else:
        result += "[FAIL]:Wrong amount of players displayed"
        status = False
    
    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='2']")
        result += "\n[SUCCESS]:2 pages displayed"
    except:
        result += "\n[FAIL]:Wrong amount of pages displayed"
        status = False

    test_result(status, result, "Top Player", "TC-TP-01")

browser()
