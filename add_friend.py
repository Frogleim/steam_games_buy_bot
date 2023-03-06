from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import random
from app import run, confirm_order
import imaplib
import email
from email_sending import send_confirm_mail
from email.header import decode_header
import re
import os

login_url = "https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header"


def read_accounts():
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()
    account_to_remove = random.choice(accounts)
    accounts.remove(account_to_remove)
    print(len(accounts))
    with open('accounts.txt', 'w') as file:
        file.writelines(accounts)
    return account_to_remove


def get_verification_code():
    verification_code = None
    mail = imaplib.IMAP4_SSL('imap.rambler.ru')
    mail.login('andrewcorrea7s@rambler.ru', 'rAq9OtxTKV1978')
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    latest = messages[0].split()[-1]
    status, msg = mail.fetch(latest, "(RFC822)")
    msg = email.message_from_bytes(msg[0][1])
    print('From:', msg['From'])
    print('Subject:', msg['Subject'])
    text = msg.get_payload()[0]
    pattern = r'\b[A-Z0-9]{5}\b'
    match = re.search(pattern, str(text))
    if match:
        verification_code = match.group()
        print(f"Verification code: {verification_code}")
    else:
        print("Verification code not found")
    return verification_code


class Client:

    def __init__(self):
        # self.path = ChromeDriverManager().install()
        self.client_driver = uc.Chrome()
        self.user_id = None

    def login(self):
        accounts = read_accounts()
        client_username = accounts.split(":")[0]
        client_password = accounts.split(":")[1]
        client_email = accounts.split(":")[2]
        email_password = accounts.split(":")[3]
        user_account_dict = {
            "username": client_username,
            "password": client_password,
            "email": client_email,
            "email password": email_password
        }
        json_object = json.dumps(user_account_dict, indent=4)
        with open("./client_accounts/client_account.json", "w") as json_file:
            json_file.write(json_object)
        self.client_driver.get(login_url)
        time.sleep(2.2)
        e_mail = self.client_driver.find_element(By.XPATH,
                                                 '//*[@id="responsive_page_template_content"]/div/div['
                                                 '1]/div/div/div/div[ '
                                                 '2]/div/form/div[1]/input')
        e_mail.send_keys(user_account_dict["username"])
        time.sleep(1.3)
        password_input = self.client_driver.find_element(By.XPATH,
                                                         '//*[@id="responsive_page_template_content"]/div/div['
                                                         '1]/div/div/div/div[2]/div/form/div[2]/input')
        password_input.send_keys(user_account_dict["password"])
        button = self.client_driver.find_element(By.XPATH,
                                                 '//*[@id="responsive_page_template_content"]/div/div['
                                                 '1]/div/div/div/div[ '
                                                 '2]/div/form/div[4]/button')
        button.click()

    def get_steam_id(self):
        drop_menu = self.client_driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/span')
        drop_menu.click()
        time.sleep(1)
        view_profile_page = self.client_driver.find_element(By.XPATH,
                                                            '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div['
                                                            '3]/div/a[1]')
        view_profile_page.click()

        get_client_url = self.client_driver.current_url
        self.user_id = get_client_url.split('/')[-2]
        print(self.user_id)
        return self.user_id

    def submit_friend_request(self):
        notification = self.client_driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[2]/div[1]")
        notification.click()
        time.sleep(1)
        new_invite = self.client_driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[2]/div["
                                                     "2]/div/a[3]/span[2]")
        new_invite.click()
        time.sleep(2)
        accept = self.client_driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[2]/div["
                                                 "2]/div[ "
                                                 "3]/a[1]")
        accept.click()

    def submit_gift(self):
        drop_menu = self.client_driver.find_element(By.XPATH, '//*[@id="header_notification_link"]/span[2]')
        drop_menu.click()
        time.sleep(1.9)
        notifications_button = self.client_driver.find_element(By.XPATH,
                                                               "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div["
                                                               "2]/div[ "
                                                               "2]/div/a[4]/span[2]")
        notifications_button.click()
        time.sleep(3.5)
        accept_gift = self.client_driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div["
                                                      "2]/div[ "
                                                      "5]/div[2]/div[2]/div/div[1]/div[1]")
        accept_gift.click()
        time.sleep(2.8)
        accept = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[4]/div/div[1]/div[1]")
        accept.click()

    def run_all(self):
        self.login()
        time.sleep(8)


class PreparedUser:
    def __init__(self, user_id, username, password, buying_games):
        # self.path = ChromeDriverManager().install()
        self.driver = uc.Chrome()
        self.user_id = user_id
        self.username = username
        self.password = password
        self.buying_games = buying_games

    def login(self):
        self.driver.get(login_url)
        time.sleep(3.8)
        e_mail = self.driver.find_element(By.XPATH,
                                          '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div['
                                          '2]/div/form/div[1]/input')
        e_mail.send_keys(self.username)
        time.sleep(1.3)
        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="responsive_page_template_content"]/div/div['
                                                  '1]/div/div/div/div[2]/div/form/div[2]/input')
        password_input.send_keys(self.password)
        button = self.driver.find_element(By.XPATH,
                                          '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div['
                                          '2]/div/form/div[4]/button')
        button.click()

    def verification(self, verification_code):
        verification_1 = self.driver.find_element(By.XPATH,
                                                  '//*[@id="responsive_page_template_content"]/div/div['
                                                  '1]/div/div/div/div[ '
                                                  '2]/form/div/div[2]/div/input[1]')
        verification_1.send_keys(verification_code[0])
        time.sleep(1)
        verification_2 = self.driver.find_element(By.XPATH,
                                                  '//*[@id="responsive_page_template_content"]/div/div['
                                                  '1]/div/div/div/div[ '
                                                  '2]/form/div/div[2]/div/input[2]')
        verification_2.send_keys(verification_code[1])
        time.sleep(1)
        verification_3 = self.driver.find_element(By.XPATH,
                                                  '//*[@id="responsive_page_template_content"]/div/div['
                                                  '1]/div/div/div/div[ '
                                                  '2]/form/div/div[2]/div/input[3]')
        verification_3.send_keys(verification_code[2])
        time.sleep(1)
        verification_4 = self.driver.find_element(By.XPATH,
                                                  '//*[@id="responsive_page_template_content"]/div/div['
                                                  '1]/div/div/div/div[ '
                                                  '2]/form/div/div[2]/div/input[4]')
        verification_4.send_keys(verification_code[3])
        time.sleep(1)
        verification_5 = self.driver.find_element(By.XPATH,
                                                  '//*[@id="responsive_page_template_content"]/div/div['
                                                  '1]/div/div/div/div[ '
                                                  '2]/form/div/div[2]/div/input[5]')
        verification_5.send_keys(verification_code[4])

    def add_friend(self):
        print(self.user_id)
        add_friend_url = "https://steamcommunity.com/id/Michael17199560567/friends/add"
        self.driver.get(add_friend_url)
        time.sleep(3)
        search_friend_input = self.driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div[2]/div['
                                                       '2]/div[4]/div/div[1]/div/input')
        search_friend_input.send_keys(self.user_id)
        time.sleep(0.5)
        search_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div['
                                                 '4]/div/div[2]')
        search_button.click()
        time.sleep(2)
        add_friend = self.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div[7]/div[2]/div/div[1]/div[2]/div/div/div[2]/div['
                                              '3]/a')
        add_friend.click()

    def buy_game(self):
        custom_url = 'https://store.steampowered.com/app/1332010/Stray/'
        self.driver.get(custom_url)

        time.sleep(1.7)
        search_game = self.driver.find_element_by_xpath('//*[@id="store_nav_search_term"]')
        search_game.send_keys(self.buying_games)
        time.sleep(0.8)
        search_game.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div["
                                          "3]/a[1]").click()
        time.sleep(1.9)
        add_to_cart = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[1]/div[3]/div[1]/div['
                                                         '5]/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/a')
        add_to_cart.click()
        print('Added to card...')
        time.sleep(2)
        send_as_gift = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div[4]/div[1]/div[3]/div["
                                           "3]/div[2]/a[1]")
        send_as_gift.click()

    def run(self):
        self.login()
        time.sleep(8)
        verification_code = get_verification_code()
        self.verification(verification_code=verification_code)
        time.sleep(3)
        self.add_friend()
        try:
            self.buy_game(self.buying_games)
            time.sleep(1)

        except Exception as e:
            print(f'Invalid card information\n{e}')


def run_bot():
    username = "andrewcorrea7s"
    password = "rAq9OtxTKV19782002"
    try:
        os.remove('./order.json')
    except Exception:
        print("order.json doesnt exist")
    games_to_buy = run()
    if games_to_buy == 'New Orders!':
        time.sleep(20)
        with open('./order.json', 'r') as file:
            data = json.load(file)
            for game_names in data:
                buying_games = game_names['game name']
                # self.login()
                client = Client()
                client.run_all()
                time.sleep(3)
                user_id = client.get_steam_id()
                prepared_account = PreparedUser(user_id, username, password, buying_games)
                prepared_account.run()
                time.sleep(4)
                client.submit_friend_request()
                time.sleep(2.75)
                client.submit_gift()
                confirm_order(game_names['order_id'])
                send_confirm_mail(game_names["buyer email"])
                print("All processes run successfully")
        return True

    else:
        print('Nothing to buy yet!')
        return False


if __name__ == "__main__":
    run_bot()
