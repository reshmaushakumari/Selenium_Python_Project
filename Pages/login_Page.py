from selenium.webdriver.common.by import By

class LoginPage():
    "Login Page class"
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "inputEmail"
        self.password_textbox_id = "inputPassword"
        self.submit_button_id = "login"

    def enter_username(self, username):
        "Find username locator and enter value in it."
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(
            username
        )

    def enter_password(self, password):
        "Find password locator and enter value in it."
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(
            password
        )

    def enter_submit(self):
        "Find submit button locator and click submit."
        self.driver.find_element(By.NAME,self.submit_button_id).click()
