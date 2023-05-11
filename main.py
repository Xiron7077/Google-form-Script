from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path='C:\Domain\Apps\chromedriver.exe', options=option)

#Link added in get to open the website you want to open
browser.get("")

for count_form in range(100):

    xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div'
    time.sleep(2)

    for count_question in range(52):

        random_number = str(random.choice([1, 2, 3, 4, 5]))

        option = xpath.split('/')
        option[14] = 'div[' + random_number + ']'
        xpath = ''
        end = False

        for c in option:
            xpath += c

            if end:
                break

            if c == 'label':
                end = True

            xpath += '/'

        print(xpath)
        click_it = browser.find_element(by=By.XPATH, value=xpath)
        click_it.click()

        question = xpath.split('/')
        question_count = int(question[6].split('[')[1].split(']')[0])
        question_count += 1
        if question_count == 17 or question_count == 26 or question_count == 44 or question_count == 51:
            question_count += 1

        question[6] = 'div[' + str(question_count) + ']'
        xpath = ''
        end = False

        for c in question:
            xpath += c

            if end:
                break

            if c == 'label':
                end = True

            xpath += '/'

    submit_button = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
    submit_button.click()

    another_response = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

browser.close()
