import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import imaplib
import email
import re
from bs4 import BeautifulSoup as BS
from add_friend import get_verification_code


def verification():
    gmail_user = 'gameacseu@gmail.com'
    gmail_password = "vjadcjnzrndinjfa"
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(gmail_user, gmail_password)
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    latest = messages[0].split()[-1]
    status, msg = mail.fetch(latest, "(RFC822)")
    msg = email.message_from_bytes(msg[0][1])
    print('From:', msg['From'])
    print('Subject:', msg['Subject'])
    text = msg.get_payload()
    soup = BS(text, "html.parser")
    strong_tag = soup.find('strong')
    verification_code = re.search(r'\d+', strong_tag.text).group(0)
    print(verification_code)
    return verification_code


class GiftCard:
    def __init__(self, amount):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = uc.Chrome(options=self.options)
        self.username = "gameacseu@gmail.com"
        self.password = "mdS2022!!"
        self.activation_code = None
        self.amount = amount

    def login(self):
        self.driver.get('https://www.oyunfor.com/')
        time.sleep(4.5)
        login_page = self.driver.find_element(By.XPATH, "/html/body/div[9]/div[1]/div[3]/a[1]")
        login_page.click()
        time.sleep(5)
        try:
            pop_up_message = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/button")
            pop_up_message.click()
        except Exception as e:
            print("No pop up message!")

        time.sleep(3)
        username_input = self.driver.find_element(By.XPATH,
                                                  "/html/body/div[5]/div/div/div/div[1]/div[1]/div["
                                                  "2]/form/div/fieldset[ "
                                                  "1]/div/label/div/input")
        username_input.send_keys(self.username)
        time.sleep(3)
        password_input = self.driver.find_element(By.XPATH,
                                                  "/html/body/div[5]/div/div/div/div[1]/div[1]/div["
                                                  "2]/form/div/fieldset[ "
                                                  "2]/div/label/div/input")
        password_input.send_keys(self.password)
        time.sleep(2.8)
        login_button = self.driver.find_element(By.XPATH,
                                                "/html/body/div[5]/div/div/div/div[1]/div[1]/div[2]/form/div/button")
        login_button.click()
        time.sleep(4.3)
        verification_code = verification()
        verification_input = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[5]/div/div/div/div/form/div/div[2]/div/input[3]")
        verification_input.send_keys(verification_code)
        time.sleep(3.4)
        submit_verification = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/form/div/div["
                                                                 "3]/button")
        submit_verification.click()
        time.sleep(2.7)

    def buy_gift_card(self):
        gift_card_page = self.driver.find_element(By.XPATH, "/html/body/div[10]/div/div[1]/a[1]")
        gift_card_page.click()
        time.sleep(2.1)
        gift_card_urls = ["https://www.oyunfor.com/steam-wallet-card/steam-cuzdan-kodu/20-tl-steam-cuzdan",
                          "https://www.oyunfor.com/steam-wallet-card/steam-cuzdan-kodu/50-tl-steam-cuzdan",
                          "https://www.oyunfor.com/steam-wallet-card/steam-cuzdan-kodu/100-tl-steam-cuzdan",
                          "https://www.oyunfor.com/steam-wallet-card/steam-cuzdan-kodu/200-tl-steam-cuzdan",
                          "https://www.oyunfor.com/steam-wallet-card/steam-cuzdan-kodu/300-tl-steam-cuzdan"]
        # user_input = int(input("Enter gift card: "))
        if self.amount == 20:
            self.driver.get(gift_card_urls[0])
        elif self.amount == 50:
            self.driver.get(gift_card_urls[1])
        elif self.amount == 100:
            self.driver.get(gift_card_urls[2])
        elif self.amount == 200:
            self.driver.get(gift_card_urls[3])
        else:
            self.driver.get(gift_card_urls[4])
        time.sleep(2.5)
        add_to_card = driver.find_element(By.XPATH, "/html/body/div[13]/div/div[2]/div[4]/div[2]")
        add_to_card.click()
        time.sleep(2.3)
        buy = self.driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[2]/div[1]/div[2]/div[2]/button")
        buy.click()
        time.sleep(2.78)
        activate_code = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[5]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div["
                                                 "3]/div[1]/div[2]/div[3]/div[2]/span")
        self.activation_code = activate_code.text
        return self.activation_code


class MainAccount:
    def __init__(self, activation_code):
        self.username = "andrewcorrea7s"
        self.password = "rAq9OtxTKV19782002"
        self.login_url = "https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header"
        self.path = ChromeDriverManager().install()
        self.steam_driver = webdriver.Chrome(path)
        self.activation_code = activation_code

    def login(self):
        steam_driver.get(login_url)
        time.sleep(1.2)
        email = self.steam_driver.find_element(By.XPATH,
                                               '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div['
                                               '2]/div/form/div[1]/input')
        email.send_keys(username)
        time.sleep(1.3)
        password_input = self.steam_driver.find_element(By.XPATH,
                                                        '//*[@id="responsive_page_template_content"]/div/div['
                                                        '1]/div/div/div/div[2]/div/form/div[2]/input')
        password_input.send_keys(password)
        button = self.steam_driver.find_element(By.XPATH,
                                                '//*[@id="responsive_page_template_content"]/div/div['
                                                '1]/div/div/div/div[ '
                                                '2]/div/form/div[4]/button')
        button.click()
        time.sleep(6)
        verification_code = get_verification_code()
        verification_1 = self.steam_driver.find_element(By.XPATH,
                                                        '//*[@id="responsive_page_template_content"]/div/div['
                                                        '1]/div/div/div/div[2]/form/div/div[2]/div/input[1]')
        verification_1.send_keys(verification_code[0])
        time.sleep(1)
        verification_2 = self.steam_driver.find_element(By.XPATH,
                                                        '//*[@id="responsive_page_template_content"]/div/div['
                                                        '1]/div/div/div/div[2]/form/div/div[2]/div/input[2]')
        verification_2.send_keys(verification_code[1])
        time.sleep(1)
        verification_3 = self.steam_driver.find_element(By.XPATH,
                                                        '//*[@id="responsive_page_template_content"]/div/div['
                                                        '1]/div/div/div/div[2]/form/div/div[2]/div/input[3]')
        verification_3.send_keys(verification_code[2])
        time.sleep(1)
        verification_4 = self.steam_driver.find_element(By.XPATH,
                                                        '//*[@id="responsive_page_template_content"]/div/div['
                                                        '1]/div/div/div/div[2]/form/div/div[2]/div/input[4]')
        verification_4.send_keys(verification_code[3])
        time.sleep(1)
        verification_5 = self.steam_driver.find_element(By.XPATH,
                                                        '//*[@id="responsive_page_template_content"]/div/div['
                                                        '1]/div/div/div/div[2]/form/div/div[2]/div/input[5]')
        verification_5.send_keys(verification_code[4])
        time.sleep(4.3)

    def get_gift_card(self):
        self.steam_driver.get("https://store.steampowered.com/account/redeemwalletcode")
        time.sleep(3.7)
        activate_code_input = self.steam_driver.find_element(By.XPATH,
                                                             "/html/body/div[1]/div[7]/div[6]/div[2]/div/div[1]/div["
                                                             "1]/div[1]/div[2]/input")
        activate_code_input.send_keys(self.activation_code)
        time.sleep(2.9)
        continue_button = self.steam_driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div[7]/div[6]/div[2]/div/div[1]/div[1]/div["
                                                         "1]/div[2]/a/span")
        continue_button.click()


if __name__ == "__main__":
    gift_card = GiftCard()
    gift_card.login()
    time.sleep(4)
    activate_code = gift_card.buy_gift_card()
    print(activate_code)
    time.sleep(4.8)
    main_account = MainAccount(activation_code=activate_code)
    main_account.login()
    time.sleep(3.3)
    main_account.get_gift_card()