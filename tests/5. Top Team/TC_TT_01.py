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
    test_list_best_team(driver)
    driver.quit()


def test_list_best_team(driver):
    """
    ID: TC-TT-01
    Title: List best players to form a team
    Description: Verify if, by default, the best players to form a team will be shown
    Steps:  1. Go to Top Team
    Expected result: A top team should be displayed with valid players and without duplicates
    """
    status = True
    result = ""
    list_player = []

    driver.get("http://localhost:3001/team")

    team = driver.find_element(By.CLASS_NAME, "entireTeam")
    time.sleep(0.5)
    players = team.find_elements(By.CLASS_NAME, "title")
    players = [player.text for player in players]
    
    for player in players:
        if player in list_player:
            result += f"[FAIL]: {player} is duplicated"
            status = False
        else:
            list_player.append(player)    

    if status:
        result += "[SUCCESS]: Players displayed correctly"

    test_result(status, result, "Top Team", "TC-TT-01")

browser()
