from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from credentials import username , password
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
'''
driver = webdriver.Chrome()

driver.get('https://instagram.com/accounts/login/')
time.sleep(5)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
user = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
user.click()

#driver.find_element_by_link_text("//button[contains(text(), 'Not Now')]").click()
ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()
time.sleep(20)


'''
class InstaUnfollowers:
    def __init__(self, username, password):
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        # instagram login
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        user.click()

        #driver.find_element_by_link_text("//button[contains(text(), 'Not Now')]").click()
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()
        time.sleep(5)
        
    def get_unfollowers(self):
        usernames = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
        usernames.click()
        profile = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
        time.sleep(3)
        Following = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        Following.click()
        following = self.get_people()
        Followers = self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
        Followers.click()
        followers = self.get_people()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def get_people(self):
        time.sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        prev_height, height = 0, 1
        while prev_height != height:
            prev_height = height
            time.sleep(1)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        close = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
        close.click()
        return names


my_bot = InstaUnfollowers(username, password)
my_bot.get_unfollowers()
try:
    my_bot.driver.close()
except:
    print("Fail")
    my_bot.driver.close()