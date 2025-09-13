import time
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
    test_search_player_by_invalid_team(driver)
    driver.quit()


def test_search_player_by_invalid_team(driver):
    """
    ID: TC-SP-05
    Title: Search players by invalid team
    Description: Verify if the search returns any players with given team that is not in the list of players, team composed of numbers and team compose of special characters
    Steps:  1. Go to Search Player
            2. Click Clear filters
            3. Enter team that is not in the list.
            4. Click search
            5. Enter team composed of numbers
            6. Click search
            7. Enter team composed of special characters
            8. Click search
    Expected result: No players should be returned in any searches
    """
    status = True
    result = ""

    invalidChars = list("!@#$%^&*_=+[]{}|;:',<>?")
    driver.get("http://localhost:3001/search")

    for invalidChar in invalidChars:
    
        driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[2]/input").send_keys(invalidChar)
        driver.find_element(By.CLASS_NAME, "search").click()
        time.sleep(0.5)

        try:
            driver.find_element(By.CLASS_NAME, "player")
            result += f"[FAIL]:Invalid Character {invalidChar} returned a club's player"
            status = False
        except:
            result += f"[SUCCESS]:Invalid Character {invalidChar} did not return a club's player"

        driver.find_element(By.CLASS_NAME, "clear").click()
        result += "\n"

    test_result(status, result, "Player List", "TC-SP-05")

browser()
