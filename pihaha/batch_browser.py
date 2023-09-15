from selenium import webdriver
import time

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox") # linux only
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(executable_path=r"D:\A_Code\Project\python\ytt\chromedriver_win32\chromedriver.exe", options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver

driver = getDriver()

# chromedriver_path = r"D:\A_Code\Project\python\ytt\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chromedriver_path)

f = open("./browser_list.txt", encoding="UTF-8")
url = f.readline().strip()
while url:
    print(url)
    driver.get(url)
    js = "window.open('" + url + "')"
    driver.execute_script(js)
    url = f.readline().strip()
print("finish1")
time.sleep(30)
print("finish2")
f.close()