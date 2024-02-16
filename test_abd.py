import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://alnafi.com/auth/sign-in')
    driver.maximize_window()
    yield driver
    driver.quit()

def my_cred():
    return [
        ('xyz@gmail.com', 'xyz@123'),
        ('abc@gmail.com', 'abc@123'),
        ('abd@gmail.com', 'abd@123')
    ]

@pytest.mark.parametrize("username,password", my_cred())
def test_login(setup_teardown, username, password):
    driver = setup_teardown
    print("My pytest login")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    email_input.send_keys(username)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys(password)

    # Add your assertions or further actions here
