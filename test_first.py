from selenium.webdriver.common.keys import Keys


def test_1():
    from pages.main_page import MainPage
    main_page = MainPage()
    main_page.open_main_page()
    assert "Google" in main_page.get_title()
    element = main_page.search()
    element.clear()
    element.send_keys("Hello")
    element.send_keys(Keys.RETURN)
    assert "No results found." not in main_page.get_page_source()
    main_page.quit()


test_1()
