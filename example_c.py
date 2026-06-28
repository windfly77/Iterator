from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class BaseHandler:
    def __init__(self):
        self.next = None  # następny krok

    def set_next(self, handler):
        self.next = handler
        return handler # pozwala łączyć .set_next()

    def handle(self, driver):
        if self.next:
            return self.next.handle(driver)
        return None

# --- Konkretne kroki ---
class OpenPageHandler(BaseHandler):
    def __init__(self, url):
        super().__init__()
        self.url = url
    def handle(self, driver):
        print(f"🌐 Otwieram stronę: {self.url}")
        driver.get(self.url)
        sleep(1)
        return super().handle(driver)
class CheckTitleHandler(BaseHandler):
    def __init__(self, expected_title):
        super().__init__()
        self.expected_title = expected_title
    def handle(self, driver):
        print("🔍 Sprawdzam tytuł strony...")
        assert self.expected_title in driver.title, f"Tytuł nie pasuje! ({driver.title})"
        print("✅ Tytuł poprawny!")
        return super().handle(driver)

class ClickLinkHandler(BaseHandler):
    def __init__(self, selector):
        super().__init__()
        self.selector = selector

    def handle(self, driver):
        print(f"🖱️ Klikam element: {self.selector}")
        link = driver.find_element(By.CSS_SELECTOR, self.selector)
        link.click()
        sleep(1)
        return super().handle(driver)# --- Uruchomienie ---
if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
# Tworzymy łańcuch kroków testu
        chain = (
            OpenPageHandler("https://example.com")
            .set_next(CheckTitleHandler("Example Domain"))
            .set_next(ClickLinkHandler("a")))
# Uruchamiamy łańcuch
        chain.handle(driver)
        print("🎉 Test zakończony sukcesem!")
    except Exception as e:
        print("❌ Błąd testu:", e)
    finally:
        driver.quit()