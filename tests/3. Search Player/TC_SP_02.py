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
    test_search_player_by_valid_name(driver)
    driver.quit()


def test_search_player_by_valid_name(driver):
    """
    ID: TC-SP-02
    Title: Search players by valid name
    Description: Verify if the search returns all players with given valid name
    Steps:  1. Go to Search Player
            2. Click Clear filters
            3. Enter a valid name
            4. Click search
    Expected result: A list with all players containing the given name should be displayed
    """
    status = True
    result = ""
    driver.get("http://localhost:3001/search")

    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div[1]/input").send_keys("Neymar")

    driver.find_element(By.CLASS_NAME, "search").click()

    try:
        driver.find_element(By.XPATH, "//span[@class='playerName' and contains(text(), 'Neymar')]")
        result += "[SUCCESS]:Player name displayed in the first page"
    except:
        result += "[FAIL]:Player name not found in the first page"
        status = False


    test_result(status, result, "Player List", "TC-SP-02")

browser()
