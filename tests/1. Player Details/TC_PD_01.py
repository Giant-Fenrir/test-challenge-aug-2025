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
    test_player_data(driver)
    driver.quit()

def test_player_data(driver):
    """
    ID:TC-PD-01
    Title: Check a player data in Player List screen
    Description: Verify if when clicking on a player, window with the player's data will pop up.
    Steps:  1. Go to Player List
            2. Click the first player
            3. Check data and close window
            4. Repeat steps 2 and 3 with player 2 and 3
    Expected result: A window containg the picked player's picture, name, team, general info, links, skills and traits, should appear
    """
    status = True
    result = ""
    i = 1

    driver.get("http://localhost:3001/")

    startScreen = driver.find_element(By.CLASS_NAME, "startScreen")
    startScreen.click()

    players = driver.find_elements(By.CLASS_NAME, "player")
    
    for player in players[:3]:
        player.click()
        img = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/img')
        loaded = driver.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0;", img)
        if loaded:
            result += f"[SUCCESS]: Player number {i} picture displayed"
        else:
            result += f"[FAIL]: Player number {i} picture not displayed"
            status = False

        title = driver.find_element(By.CLASS_NAME, "title")
        club = driver.find_element(By.CLASS_NAME, "club")
        value = driver.find_element(By.CLASS_NAME, "value")
        if title and club and value:
            result += f"\n[SUCCESS]: Player number {i} basic info displayed"
        else:
            result += f"\n[FAIL]: Player number {i} basic info not displayed"
            status = False

        generalInfo = driver.find_element(By.CLASS_NAME, "generalInfo")
        generalInfo = generalInfo.find_elements(By.CLASS_NAME, "team")
        if len(generalInfo) == 4:
            result += f"\n[SUCCESS]: Player number {i} general info displayed"
        else:
            result += f"\n[FAIL]: Player number {i} general info not displayed"
            status = False

        links = driver.find_element(By.CLASS_NAME, "links")
        links = links.find_elements(By.CLASS_NAME, "link")
        if len(links) == 3:
            result += f"\n[SUCCESS]: Player number {i} links displayed"
        else:
            result += f"\n[FAIL]: Player number {i} links not displayed"
            status = False

        skills = driver.find_element(By.CLASS_NAME, "skills")
        skills = skills.find_elements(By.CLASS_NAME, "skill")
        if len(skills) == 4:
            result += f"\n[SUCCESS]: Player number {i} skills displayed"
        else:
            result += f"\n[FAIL]: Player number {i} skills not displayed"
            status = False

        traits = driver.find_element(By.CLASS_NAME, "traits")
        traits = traits.find_elements(By.CLASS_NAME, "trait")
        if len(traits) >= 1:
            result += f"\n[SUCCESS]: Player number {i} traits displayed"
        else:
            result += f"\n[FAIL]: Player number {i} traits not displayed"
            status = False
        
        driver.find_element(By.CLASS_NAME, "close").click()
        result += "\n\n"
        i += 1

    test_result(status, result, "Player Details", "TC-PD-01")

browser()

