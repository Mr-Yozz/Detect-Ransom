from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# Path to the ChromeDriver executable
# webdriver_path = r"C:\Users\Yogeshwaran\Downloads\chromedriver.exe"


def search_hash(hash):

    # Initialize the WebDriver
    # service = Service(webdriver_path)
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    try:
        # URL of the webpage containing the shadow root
        url = "https://www.virustotal.com/gui/file/" + hash

        # Open the webpage
        driver.get(url)

        element = driver.find_element(By.XPATH,'//*[@id="view-container"]')

        # element = driver.find_element(By.XPATH,'//*[@id="view-container"]/file-view')
        # script = driver.execute_script('document.querySelector("#body > vt-ui-shell").shadowRoot.querySelector("#joinUsCaptchaContainer")')
        # data = script.find_elements(By.XPATH,'//*[@id="report"]')
        print(element.text)

    except WebDriverException as e:
        print("An error occurred:", e)
