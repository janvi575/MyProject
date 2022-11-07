
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# driver = webdriver.Chrome()
driver = webdriver.Chrome(r"/usr/lib/chromium-browser/chromedriver")

# driver.get(r"https://www.google.com/")
# driver.find_element(By.NAME,"q").send_keys('javatpoint')
# time.sleep(2)
# driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
# print("javatpoint")
# driver.quit()


# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element(By.NAME, "q")
# search_bar.clear()
# time.sleep(2)
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.quit()


driver.get("https://www.imdb.com/search/title/")
time.sleep(2)

title = driver.find_element(By.XPATH,'//*[@id="main"]/div[1]/div[2]/input')
title.send_keys('abc')
time.sleep(1)

title_type = driver.find_element(By.XPATH, '//*[@id="title_type-2"]')
title_type.click()
time.sleep(2)

rel_date = driver.find_element(By.NAME, 'release_date-min')
rel_date.send_keys('2022-1-12')
time.sleep(1)

rel_date1 = driver.find_element(By.NAME, 'release_date-max')
rel_date1.send_keys('2022-8-25')
time.sleep(1)

user_rating = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[2]/select[1]/option[12]').click()
time.sleep(1)

user_rating2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[2]/select[2]/option[37]').click()
time.sleep(1)

num_vote = driver.find_element(By.NAME, 'num_votes-min')
num_vote.send_keys('5')
time.sleep(1)

num_vote1 = driver.find_element(By.NAME, 'num_votes-max')
num_vote1.send_keys('8')
time.sleep(1)

geners = driver.find_element(By.ID, 'genres-1')
geners.click()
time.sleep(1)

geners1 = driver.find_element(By.ID, 'genres-5')
geners1.click()
time.sleep(1)

title_group = driver.find_element(By.XPATH, '//*[@id="groups-1"]')
title_group.click()
time.sleep(1)

title_group = driver.find_element(By.XPATH, '//*[@id="main"]/div[8]/div[2]/select/option[4]')
title_group.click()
time.sleep(1)

title_data = driver.find_element(By.XPATH, '//*[@id="main"]/div[8]/div[2]/select/option[4]')
title_data.click()
time.sleep(1)

com = driver.find_element(By.ID, 'companies-3')
com.click()
time.sleep(1)

watch = driver.find_element(By.ID, 'online_availability-1')
watch.click()
time.sleep(1)

certificate = driver.find_element(By.ID, 'certificates-1')
certificate.click()
time.sleep(1)

color_info = driver.find_element(By.ID, 'colors-1')
color_info .click()
time.sleep(1)

contry = driver.find_element(By.XPATH, '//*[@id="main"]/div[13]/div[2]/select/option[108]')
contry.click()
time.sleep(1)

key = driver.find_element(By.XPATH, '//*[@id="keywords"]')
key.send_keys('ab')
time.sleep(1)

lang = driver.find_element(By.XPATH, '//*[@id="main"]/div[8]/div[2]/select/option[4]')
lang.click()
time.sleep(1)

locations = driver.find_element(By.XPATH, '//*[@id="main"]/div[16]/div[2]/input')
locations.send_keys('ahmedabad')
time.sleep(1)

popularity = driver.find_element(By.NAME, 'moviemeter-min')
popularity .send_keys('100')
time.sleep(1)

sound_mix = driver.find_element(By.XPATH, '//*[@id="sound_mixes-5"]')
sound_mix.click()
time.sleep(1)

rating = driver.find_element(By.XPATH, '//*[@id="my_ratings|"]')
rating.click()
time.sleep(1)

in_theaters = driver.find_element(By.XPATH, '//*[@id="now_playing"]')
in_theaters .click()
time.sleep(2)

btn = driver.find_element(By.XPATH, '//*[@id="main"]/p[3]/button')
btn.click()

# driver.quit()