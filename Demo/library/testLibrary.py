# coding=utf-8
from appium.webdriver.common.touch_action import TouchAction
from robot.libraries.BuiltIn import BuiltIn






class testLibrary:

    def draw_Lock_Pattern(self, x1, y1, x2, y2, x3, y3):
        driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
        action = TouchAction(driver)
        action.press(x=x1, y=y1).move_to(x=x2, y=y2).move_to(
            x=x3, y=y3).release().perform()

    def get_bugreport(self):
    	driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
    	logtypes = driver.log_types
    	driver.get_log('bugreport')


    def change_language(self):
    	driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
    	element1 = driver.find_element_by_xpath("//android.widget.TextView[@text='Languages']")
    	element2 = driver.find_element_by_xpath("//android.widget.TextView[@text='2']")
    	action = TouchAction(driver)
    	action.long_press(element2).move_to(element1).release().perform()

    def double_click(self, locator):
        driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
        element = driver.find_element_by_xpath(locator)
        action = TouchAction(driver)
        action.tap(element, count=2).perform()
    
    def unlock_by_screenLock_pattern(self):
        driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
        driver.unlock()


