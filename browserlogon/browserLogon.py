from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# TODO refactor accounts schema
accounts = {'@gmail.com':'acct1', '@gmail.com':'acct2', '@yahoo.com':'acct3'}
accounts2 ={'@gmail.com':'acct4', '@gmail.com':'acct5', '@gmail.com':'acct6'}

# Set page to log into
loginpage = 'http://stellar-test.mit.edu/S/login/?u=%2FS%2Fproject%2Fdatanerdtest%2F'

# Account type is an option found on form
# Add new options for checkboxes, radio buttons, dropdowns, etc
accountType = str(raw_input('tests or admin connection? '))
password = str(raw_input('Enter password: '))

# Initialize other objects required for script
driver_instances = {}
account_instances = {}

# Function takes an accountType as a string
# and logs into the web site
# Designed for MIT activities but can be refactored
def startBrowser(type='admin'):
    if type == "tests" or type == "tests2":
    	if type == 'tests':
    		holder = accounts
    	if type == 'tests2':
    		holder = accounts2
        count = 0
        for account in holder:
            count += 1
            driver_instances[count] = webdriver.Firefox()
            account_instances[count] = {'username':account, 'password':password}
            driver_instances[count].get(loginpage)
            collab = driver_instances[count].find_element_by_xpath('/html/body/div/div[2]/form/fieldset/div/p[1]/select/optgroup[1]/option[2]').click()
            submit = driver_instances[count].find_element_by_xpath('/html/body/div/div[2]/form/fieldset/div/p[1]/input').click()
            username = driver_instances[count].find_element_by_name('j_username')
            username.send_keys(account_instances[count]['username'])
            value = driver_instances[count].find_element_by_name('j_password')
            value.send_keys(account_instances[count]['password'])
            submit = driver_instances[count].find_element_by_xpath('/html/body/div[2]/form/fieldset/label[2]/input[2]').click()
    elif type in accounts:
        driver = webdriver.Firefox()
        account = {'username':type, 'password':password}
        driver.get(loginpage)
        collab = driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/div/p[1]/select/optgroup[1]/option[2]').click()
        submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/div/p[1]/input').click()
        username = driver.find_element_by_name('j_username')
        username.send_keys(account['username'])
        value = driver.find_element_by_name('j_password')
        value.send_keys(account['password'])
        submit = driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/label[2]/input[2]').click()
    else:
        driver = webdriver.Firefox()
        account = {'username':'jjpierre', 'password':password}
        driver.get(loginpage)
        submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/div/p[1]/input').click()
        username = driver.find_element_by_name('j_username')
        username.send_keys(account['username'])
        value = driver.find_element_by_name('j_password')
        value.send_keys(account['password'])
        submit = driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/label[2]/input[2]').click()

# Invoke script to start browser windows
# and log into administrative accounts 
startBrowser(accountType)