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
    driver.implicitly_wait(10)
    test_search_player_all_players(driver)
    driver.quit()


def test_search_player_all_players(driver):
    """
    ID: TC-SP-01
    Title: List all players in Search Player
    Description: Verify if returns all players by default
    Steps:  1. Go to Search Player
    Expected result: A list with 4736 pages and a total of 18.944 players will be displayed
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/search")

    players = driver.find_elements(By.CLASS_NAME, "player")
    if len(players) == 4:
        result += "[SUCCESS]:4 players displayed"
    else:
        result += "[FAIL]:Wrong amount of players displayed"
        status = False
    
    try:
        driver.find_element(By.XPATH, "//div[@class='number ' and text()='4736']")
        result += "\n[SUCCESS]:4736 pages displayed"
    except:
        result += "\n[FAIL]:Wrong amount of pages displayed"
        status = False

    test_result(status, result, "Search Player", "TC-SP-01")

browser()
        