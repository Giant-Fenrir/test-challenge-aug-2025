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
    test_five_top_team(driver)
    driver.quit()


def test_five_top_team(driver):
    """
    ID: TC-TT-05
    Title: List 5 different top teams
    Description: Verify if all the 5 top teams are composed correctly
    Steps:  1. Go to Top Team
            2. Click Clear Filters
            3. Select the first nationality
            4. Click Search
            5. Repeat step 3 and 4 for the second until fifth nationality.
    Expected result: 5 top teams should be displayed with valid players and without duplicates
    """
    status = True
    result = ""
    list_players = []
    nations = ["Argentina", "Portugal", "Slovenia", "Poland", "Brazil"]

    driver.get("http://localhost:3001/team")

    for nation in nations:
        Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[2]/select")).select_by_value(nation)
        driver.find_element(By.CLASS_NAME, "search").click()

        team = driver.find_element(By.CLASS_NAME, "entireTeam")
        time.sleep(0.5)
        players = team.find_elements(By.CLASS_NAME, "title")
        players = [player.text for player in players]
        
        for player in players:
            if player in list_players:
                result += f"[FAIL]: {player} is duplicated for {nation}'s top team\n"
                status = False
            else:
                list_players.append(player)    

        if len(list_players) == len(players):
            result += f"[SUCCESS]: Players displayed correctly for {nation}\n"

        list_players = []
    test_result(status, result, "Top Team", "TC-TT-05")

browser()