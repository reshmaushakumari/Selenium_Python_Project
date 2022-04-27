class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "inputEmail"
        self.password_textbox_id = "inputPassword"
        self.submit_button_id = "login"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def enter_submit(self):
        self.driver.find_element_by_name(self.submit_button_id).click()