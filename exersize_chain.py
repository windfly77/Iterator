from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import InvalidSessionIdException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseHandler:
    def __init__(self):
        self.next = None
        self.driver = None

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, driver):
        self.driver = driver
        if self.next:
            return self.next.handle(driver)
        return None

    def get_element_when_located(self, by_type, path: str, time_to_wait: int = 5):
        try:
            return WebDriverWait(self.driver, time_to_wait).until(
                EC.presence_of_element_located((by_type, path))
            )
        except (InvalidSessionIdException, TimeoutException):
            return None


class OpenPageHandler(BaseHandler):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def handle(self, driver):
        self.driver = driver
        print(f"Opening page {self.url}")
        driver.get(self.url)
        sleep(1)
        return super().handle(driver)


class NameInputHandler(BaseHandler):
    def __init__(self, name):
        super().__init__()
        self.first_name = name

    def handle(self, driver):
        self.driver = driver
        self.fill_name()
        return super().handle(driver)

    def fill_name(self):
        if self.first_name:
            xpath = '//div/input[contains (@id, "firstName")]'
            user_input = self.get_element_when_located(By.XPATH, xpath)
            if user_input:
                user_input.clear()
                user_input.send_keys(self.first_name)
                print(f"First name ({self.first_name}) entered successfully")
            else:
                print("Name can't be entered")
        else:
            print("First name not found")


class LNameInputHandler(BaseHandler):
    def __init__(self, name):
        super().__init__()
        self.last_name = name

    def handle(self, driver):
        self.driver = driver
        self.fill_l_name()
        return super().handle(driver)

    def fill_l_name(self):
        if self.last_name:
            xpath = '//div/input[contains (@id, "lastName")]'
            user_input = self.get_element_when_located(By.XPATH, xpath)
            if user_input:
                user_input.clear()
                user_input.send_keys(self.last_name)
                print(f"Last name '{self.last_name}' entered successfully")
            else:
                print("Last Name can't be entered")
        else:
            print("Last name not found")


class EmailInputHandler(BaseHandler):
    def __init__(self, email):
        super().__init__()
        self.email = email

    def handle(self, driver):
        self.driver = driver
        self.fill_email()
        return super().handle(driver)

    def fill_email(self):
        if self.email:
            xpath = '//div/input[contains (@id, "userEmail")]'
            email_input = self.get_element_when_located(By.XPATH, xpath)
            if email_input:
                email_input.clear()
                email_input.send_keys(self.email)
                print(f"Email '{self.email}' entered successfully")
            else:
                print("Email can't be entered")
        else:
            print("Email not found")

class GenderInputHandler(BaseHandler):
    def __init__(self, gender):
        super().__init__()
        self.gender = gender
        self.genders = {
            "Male": '//input[contains(@id, "gender-radio-1")]',
            "Female": '//input[contains(@id, "gender-radio-2")]',
            "Other": '//input[contains(@id, "gender-radio-3")]',
        }

    def handle(self, driver):
        self.driver = driver
        self.fill_gender()
        return super().handle(driver)

    def fill_gender(self):
        if self.gender in self.genders:
            choice = self.get_element_when_located(By.XPATH, self.genders[self.gender])
            if choice:
                choice.click()
                print(f"Gender '{self.gender}' selected successfully")
            else:
                print("Gender can't be selected")
        else:
            print("Invalid gender")

class MobileInputHandler(BaseHandler):
    def __init__(self, mobile):
        super().__init__()
        self.mobile = mobile

    def handle(self, driver):
        self.driver = driver
        self.fill_mobile()
        return super().handle(driver)

    def fill_mobile(self):
        if self.mobile:
            xpath = '//div/input[contains (@id, "userNumber")]'
            mobile_input = self.get_element_when_located(By.XPATH, xpath)
            if mobile_input:
                mobile_input.clear()
                mobile_input.send_keys(self.mobile)
                print(f"Mobile '{self.mobile}' entered successfully")
            else:
                print("Mobile can't be entered")
        else:
            print("Mobile not found")


class BirthdayInputHandler(BaseHandler):
    def __init__(self, date):
        super().__init__()
        self.date = date

    def handle(self, driver):
        self.driver = driver
        self.fill_birthday()
        return super().handle(driver)

    def fill_birthday(self):
        xpath = '//div/input[contains (@id, "dateOfBirthInput")]'
        birthday_input = self.get_element_when_located(By.XPATH, xpath)
        if birthday_input:
            birthday_input.clear()
            birthday_input.send_keys(self.date)
            print(f"Birthday '{self.date}' entered successfully")
        else:
            print("Birthday can't be entered")


class SubjectInputHandler(BaseHandler):
    def __init__(self, subject):
        super().__init__()
        self.subject = subject

    def handle(self, driver):
        self.driver = driver
        self.fill_subject()
        return super().handle(driver)

    def fill_subject(self):
        if self.subject:
            xpath = '//input[contains(@id, "subjectsInput")]'
            subject_input = self.get_element_when_located(By.XPATH, xpath)
            if subject_input:
                subject_input.send_keys(self.subject)
                sleep(0.5)
                subject_input.send_keys("\n")
                print(f"Subject '{self.subject}' entered successfully")
            else:
                print("Subject can't be entered")


class HobbyInputHandler(BaseHandler):
    def __init__(self, hobby):
        super().__init__()
        self.hobby = hobby
        self.hobbies = {
            "Sports": '//input[contains(@id, "hobbies-checkbox-1")]',
            "Reading": '//input[contains(@id, "hobbies-checkbox-2")]',
            "Music": '//input[contains(@id, "hobbies-checkbox-3")]',
        }

    def handle(self, driver):
        self.driver = driver
        self.fill_hobby()
        return super().handle(driver)

    def fill_hobby(self):
        if self.hobby in self.hobbies:
            choice = self.get_element_when_located(By.XPATH, self.hobbies[self.hobby])
            if choice:
                choice.click()
                print(f"Hobby '{self.hobby}' selected successfully")
            else:
                print("Hobby can't be selected")


class PictureInputHandler(BaseHandler):
    def __init__(self, picture_path):
        super().__init__()
        self.picture_path = picture_path

    def handle(self, driver):
        self.driver = driver
        self.upload_picture()
        return super().handle(driver)

    def upload_picture(self):
        if self.picture_path:
            xpath = '//input[contains (@id, "uploadPicture")]'
            picture_input = self.get_element_when_located(By.XPATH, xpath)
            if picture_input:
                picture_input.send_keys(self.picture_path)
                print(f"Picture uploaded successfully")
            else:
                print("Picture can't be uploaded")


class AddressInputHandler(BaseHandler):
    def __init__(self, address):
        super().__init__()
        self.address = address

    def handle(self, driver):
        self.driver = driver
        self.fill_address()
        return super().handle(driver)

    def fill_address(self):
        if self.address:
            xpath = '//textarea[contains (@id, "currentAddress")]'
            address_input = self.get_element_when_located(By.XPATH, xpath)
            if address_input:
                address_input.clear()
                address_input.send_keys(self.address)
                print(f"Address entered successfully")
            else:
                print("Address can't be entered")


class StateInputHandler(BaseHandler):
    def __init__(self, state):
        super().__init__()
        self.state = state

    def handle(self, driver):
        self.driver = driver
        self.fill_state()
        return super().handle(driver)

    def fill_state(self):
        if self.state:
            xpath = '//div[contains(@id, "state")]'
            state_input = self.get_element_when_located(By.XPATH, xpath)
            if state_input:
                state_input.click()
                sleep(0.5)
                option_xpath = f'//div[text()="{self.state}"]'
                option = self.get_element_when_located(By.XPATH, option_xpath)
                if option:
                    option.click()
                    print(f"State '{self.state}' selected successfully")
            else:
                print("State can't be selected")


class CityInputHandler(BaseHandler):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def handle(self, driver):
        self.driver = driver
        self.fill_city()
        return super().handle(driver)

    def fill_city(self):
        if self.city:
            xpath = '//div[contains(@id, "city")]'
            city_input = self.get_element_when_located(By.XPATH, xpath)
            if city_input:
                city_input.click()
                sleep(0.5)
                option_xpath = f'//div[text()="{self.city}"]'
                option = self.get_element_when_located(By.XPATH, option_xpath)
                if option:
                    option.click()
                    print(f"City '{self.city}' selected successfully")
            else:
                print("City can't be selected")
class SubmitHandler(BaseHandler):
    def handle(self, driver):
        self.driver = driver
        self.submit_form()
        return super().handle(driver)

    def submit_form(self):
        xpath = '//button[contains(@id, "submit")]'
        submit_button = self.get_element_when_located(By.XPATH, xpath)
        if submit_button:
            submit_button.click()
            print("Form submitted successfully")
            sleep(2)
        else:
            print("Submit button not found")
def collect_user_input():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email(it has to have an '@' and '.'): ")
    if "@" and "." in email:
        pass
    else:
        print("Email incorrect.. try again")
        email = input("Enter email again: ")
    print("Are you?\n"
          "Male\n"
          "Female\n"
          "Other\n")
    genders = {
        "Male": '//input[contains(@id, "gender-ratio-1")]',
        "Female": '//input[contains(@id, "gender-ratio-2")]',
        "Other": '//input[contains(@id, "gender-ratio-3")]',
    }
    gender = input("Gender?:")
    if gender in genders:
        pass
    else:
        print("Invalid input. try again")
        gender = input("Enter gender again: ")
    mobile = input("Mobile number(it has to have 10 digits): ")
    if mobile.isdigit() and len(mobile) == 10:
        pass
    else:
        print("Invalid mobile number.. try again")
        mobile = input("Mobile number: ")
    date = input("What is your date of birth?(Enter it in MM/DD/YYYY)")
    if len(date) == 10:
        if "/" and "/" and "/" in date:
            pass
        else:
            print("Incorrect number of slashes. try again")
            date = input("Enter it in MM/DD/YYYY: ")
    else:
        print("Incorrect date format. try again")
        date = input("Enter it in MM/DD/YYYY: ")
    print("Available subjects:\n"
          "Accounting\n"
          "Arts \n"
          "Biology\n"
          "Chemistry\n"
          "Civics\n"
          "Computer Science\n"
          "Commerce\n"
          "English\n"
          "Economics\n"
          "Hindi\n"
          "History\n"
          "Maths\n"
          "Physics\n"
          "Social Studies\n")
    subjects = {
        "Accounting",
        "Arts",
        "Biology",
        "Chemistry",
        "Civics",
        "Computer Science",
        "Commerce",
        "English",
        "Economics",
        "Hindi",
        "History",
        "Maths",
        "Physics",
        "Social Studies"
    }
    subject = input("Enter subject name: ")
    if subject in subjects:
        pass
    else:
        print("Invalid subject.. try again")
        subject = input("Enter subject name: ")
    print("Hobbies to choose from:\n"
          "- Sports\n"
          "- Reading\n"
          "- Music\n")
    hobbies = {
        "Sports",
        "Reading",
        "Music",
    }
    hobby = input("Enter your hobby: ")
    if hobby in hobbies:
        pass
    else:
        print("Invalid hobby.. try again")
        hobby = input("Enter your hobby: ")
    picture = "C:\windf\OneDrive\Obrazy\CGameslogo.png"
    adress = input("Enter your adress: ")
    print("States to choose from:\n"
          "NCR\n"
          "Uttar Pradesh\n"
          "Haryana\n"
          "Rajasthan")
    states = {
        "NCR",
        "Uttar Pradesh",
        "Haryana",
        "Rajasthan"
    }
    state = input("Enter your state: ")
    if state in states:
        pass
    else:
        print("Invalid state. try again")
        state = input("Enter your state again: ")
    if state == "NCR":
        cities = {
            "Delhi",
            "Gurgaon",
            "Noida",
        }
        print("Citiess to choose from:\n"
              "Delhi\n"
              "Gurgaon\n"
              "Noida\n")
        city = input("Enter your city: ")
        if city in cities:
            pass
        else:
            print("Invalid city. try again")
            city = input("Enter your city again: ")
        if state == "Uttar Pradesh":
            cities = {
                "Agra",
                "Lucknow",
                "Merrut",
            }
            print("Cities to choose from:\n"
                  "Agra\n"
                  "Lucknow\n"
                  "Merrut\n")
            city = input("Enter your city: ")
            if city in cities:
                pass
            else:
                print("Invalid city. try again")
                city = input("Enter your city again: ")
        if state == "Haryana":
            print("Cities to choose from:\n"
                  "Karnal\n"
                  "Panipat\n")
            cities = {
                "Karnal",
                "Panipat",
            }
            city = input("Enter your city: ")
            if city in cities:
                pass
            else:
                print("Invalid city. try again")
                city = input("Enter your city again: ")
        if state == "Rajasthan":
            cities = {
                "Jaipur",
                "Jailselmer",
            }
            print("Cities to choose from:\n"
                  "Jaipur\n"
                  "Jailselmer\n")
            city = input("Enter your city: ")
            if city in cities:
                pass
            else:
                print("Invalid city. try again")
                city = input("Enter your city again: ")
        else:
            print("Invalid state. try again")
            state = input("Enter your state: ")

if __name__ == "__main__":
    user_data = collect_user_input()

    print("\n!Starting Form Automation!\n")

    driver = webdriver.Chrome()
    try:
        chain = OpenPageHandler("https://demoqa.com/automation-practice-form")
        chain.set_next(NameInputHandler(user_data["first_name"]))
        chain.set_next(LNameInputHandler(user_data["last_name"]))
        chain.set_next(EmailInputHandler(user_data["email"]))
        chain.set_next(GenderInputHandler(user_data["gender"]))
        chain.set_next(MobileInputHandler(user_data["mobile"]))
        chain.set_next(BirthdayInputHandler(user_data["date"]))
        chain.set_next(SubjectInputHandler(user_data["subject"]))
        chain.set_next(HobbyInputHandler(user_data["hobby"]))
        if user_data["picture"]:
            chain.set_next(PictureInputHandler(user_data["picture"]))

        chain.set_next(AddressInputHandler(user_data["address"]))
        chain.set_next(StateInputHandler(user_data["state"]))
        chain.set_next(CityInputHandler(user_data["city"]))
        chain.set_next(SubmitHandler())

        chain.handle(driver)
        print("\n🎉 Test completed successfully!")

    except Exception as e:
        print("❌ Test error:", e)
    finally:
        input("\nPress Enter to close browser...")
        driver.quit()