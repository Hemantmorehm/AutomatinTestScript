from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

user = "8871426113"
password = "Panther$28"
options = Options()
options.add_experimental_option("detach", True)


class Test_global:
    driver = None


def test_navigate_to_website():
    Test_global.driver = webdriver.Edge(options=options)
    Test_global.driver.get("https://www.amazon.in/")
    Test_global.driver.maximize_window()


def test_login_to_website():
    login = Test_global.driver.find_element(By.XPATH, "//*[@id = 'nav-link-accountList-nav-line-1']")
    login.click()
    email_id = Test_global.driver.find_element(By.XPATH, "//input[@id = 'ap_email']")
    email_id.send_keys(user)
    time.sleep(1)
    continue_button = Test_global.driver.find_element(By.CSS_SELECTOR, "span#continue")
    continue_button.click()
    Password = Test_global.driver.find_element(By.XPATH, "//input[@type = 'password']")
    time.sleep(1)
    Password.send_keys(password)
    time.sleep(1)
    check_box = Test_global.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/label/div/label/span")
    check_box.click()
    time.sleep(1)
    sign_in = Test_global.driver.find_element(By.XPATH, "//input[@id = 'signInSubmit']")
    sign_in.click()
    time.sleep(10)


def test_add_product_to_cart():
    search_box = Test_global.driver.find_element(By.XPATH, "//input[@id = 'twotabsearchtextbox']")
    time.sleep(1)
    search_box.send_keys("power of your subconscious mind book")
    time.sleep(2)
    search_icon = Test_global.driver.find_element(By.ID, "nav-search-submit-button")
    search_icon.click()
    time.sleep(2)
    results = Test_global.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/span/div/div/span")
    Test_global.driver.execute_script("arguments[0].scrollIntoView(true)", results)
    time.sleep(3)
    Test_global.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span").click()
    time.sleep(2)
    after_window = Test_global.driver.window_handles[1]
    Test_global.driver.switch_to.window(after_window)
    Test_global.driver.get("https://www.amazon.in/Power-Your-Subconscious-Mind/dp/8194790832/ref=sr_1_1_sspa?crid=AM0ZZLLLZUB2&dib=eyJ2IjoiMSJ9.Gilzs6NcapyuWuYljboHW3_iDpJyONYXYBGGuL5cwf4pzGV8SuhLmg5H64TVqm99tsh1caYJg6Ryk7W7aJv-84-ueiKBRNhpP9vqujUCVMyGzSskzKIV3XMm4c-ejPq1B2lSGINbQAZ37XXw-r70aPrC-fitfgkBhLjCcP8ffcTlD9ey_ZnAXMmBh9baQX3pLLxKNCtiEsIU17XGDm5h03sP_URfNH9s8edPAM2blSs.qGRUGy4bSyxRRW8ZI_VRMBAEMT4-PtOh5OJkVD2hiOE&dib_tag=se&keywords=power+of+your+subconscious+mind+book&qid=1711778707&sprefix=power+of+your+subconscious+mind+book%2Caps%2C250&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
    time.sleep(3)
    Test_global.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
    time.sleep(3)


def test_go_to_homepage():
    home_page = Test_global.driver.find_element(By.XPATH, "//a[@aria-label = 'Amazon.in']")
    home_page.click()
    time.sleep(2)


def test_verify_cart():
    cart = Test_global.driver.find_element(By.XPATH, "//a[@id = 'nav-cart']")
    cart.click()
    cart_item_count = Test_global.driver.find_element(By.CSS_SELECTOR, "#a-autoid-0-announce > span.a-dropdown-prompt").text
    expected_item_count = 1
    assert int(cart_item_count) == expected_item_count, f"Expected {expected_item_count} item(s) in the cart!"
