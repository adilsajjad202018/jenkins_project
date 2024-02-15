import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import  time

def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://alnafi.com/auth/sign-in')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('xyz@gmail.com', 'xyz@123'),
        ('abc@gmail.com', 'abc@123'),
        ('abd@gmail.com', 'abd@123')
    ]
@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.NAME,'email').send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME,'password').send_keys(password)
    time.sleep(1)
