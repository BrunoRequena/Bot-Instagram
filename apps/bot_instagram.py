from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


EMAIL = "user@email.com"
PASSWORD = "coxinha123"
USERNAME = "omelhorperfil"
INSTAGRAM_URL = "https://www.instagram.com/"
servico = Service(ChromeDriverManager().install())


class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(service=servico)

    def login(self, url, email, password):
        #   open instagram
        self.driver.get(url=url)
        sleep(5)

        #   login
        email_input = self.driver.find_element(By.NAME, "username")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        sleep(2)
        password_input.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self, url, account):
        #   get profile
        sleep(5)
        self.driver.get(url=f"{url}{account}")
        sleep(10)

        #   click on followers
        followers = self.driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        sleep(15)

        modal = self.driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')

        # while True:
        for _ in range(2):
            sleep(5)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

        sleep(5)

        print("Find followers end")

    def follow(self):
        print("Follow start")
        sleep(5)
        # buttons = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Seguir")

        buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div div button")

        print(buttons)

        for button in buttons:
            button.click()
            print(button.text)
            sleep(2)

        print("Follow end")


bot = InstaFollower(driver=servico)

#   login instagram
bot.login(url=INSTAGRAM_URL, email=EMAIL, password=PASSWORD)

#   find followers
bot.find_followers(url=INSTAGRAM_URL, account=USERNAME)

#   follow
bot.follow()