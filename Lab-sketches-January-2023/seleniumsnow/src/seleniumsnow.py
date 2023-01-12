# imports
import time, sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# collect url data
with open(r'Scrap-Yard\Lab-sketches-January-2023\seleniumsnow\data\url-data.txt','r') as file:
    
    # read data from file
    url_data = file.readlines()
    pass

# collect email/password credentails
with open(r'Scrap-Yard\Lab-sketches-January-2023\seleniumsnow\data\genesisgir-github-credentials.txt','r') as file:
    
    # read data from file
    creds = file.readlines()
    pass

# chromeoptions
# usb_device_handle log warning fix 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# driver instance
driver = webdriver.Chrome(executable_path=r'Scrap-Yard\Lab-sketches-January-2023\seleniumsnow\driver\chromedriver.exe',
                            service_log_path=r'Scrap-Yard\Lab-sketches-January-2023\seleniumsnow\log\service-logger.log',
                            options=options)

# welcome user

print(""" 
                        █▀ █▀▀ █░░ █▀▀ █▄░█ █ █░█ █▀▄▀█   █▀ █▄░█ █▀█ █░█░█
                        ▄█ ██▄ █▄▄ ██▄ █░▀█ █ █▄█ █░▀░█   ▄█ █░▀█ █▄█ ▀▄▀▄▀

                                ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺

Snow is a program that signs you into your github profile and is exclusive for you genesis!,
it was created for you and by you and is a simple program that uses selenium for web api automation and is very
useful when you dont want to go to chrome to sign in by yourself. just launch your github from visual studio code!
""")

# selenium methods/functions
def signin(): # signs into github profile
    
    # refer global driver
    global driver
    
    # boot url
    driver.get(url_data[0].strip())
    driver.maximize_window()
    
    # search for sign-in element and click element
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a')
    driver.implicitly_wait(3) # implicitly wait
    ActionChains(driver=driver).move_to_element(to_element=element).click().perform() # click sign-in element
    
    
    # enter login email
    print("sending github your email. . .")
    element = driver.find_element_by_xpath('//*[@id="login_field"]')
    element.clear()
    element.send_keys(creds[0].strip())
    
    # enter login password
    print("sending github your password. . .")
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.clear()
    element.send_keys(creds[1].strip())
    element.send_keys(Keys.RETURN)
    
    # go to github profile
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/summary/img') # open summary
    ActionChains(driver=driver).move_to_element(to_element=element).click().perform()
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/details-menu/a[1]') # go to profile
    ActionChains(driver=driver).move_to_element(to_element=element).click().perform() # click profile
    print("Login success!")
    
    # signout prompt
    signout()
    pass

def signout():
    
    # refer global driver
    global driver
    
    # flow controls
    while True: # loop prompt until satisfied
        # sign-out prompt
        resp = input("Sign-out of github? [y/n] ")

        if resp == 'y': # user decides to sign out of their account
            element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/summary/img')
            ActionChains(driver=driver).move_to_element(to_element=element).click().perform()
            signout_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/details-menu/form/button')
            ActionChains(driver=driver).move_to_element(to_element=signout_element).click().perform()
            break # escape while loop
            pass
        
        elif resp == 'n': # user wishes to stay logged-in
            continue # re-iterate prompt
            pass
        
        else: # invalid values entered
            continue # re-iterate prompt
            pass
    
    while True:
        # re-login prompt
        resp = input("You have been successfully logged out your github, would you like to sign in again? [y/n] ")

        if resp == 'y':
            signin()
            break
            pass
        
        elif resp == 'n':
            
            print("Selenium Snow is now closing. . ")
            sys.exit() # terminate program
        
        else: # user input values other than 'y' or 'n' so iterate again
            continue
            pass
    pass

# sign-in github
signin()
