from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# put it in setUp
self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                               desired_capabilities={'app': 'C:\MasterM\master.exe',
                                                     'args': '-port 345'})
# put it in test method body
win = self.driver.find_element_by_id('WpfTestApplicationMainWindow')
win.find_element_by_id('SetTextButton').click()
assert 'CARAMBA' == self.driver.find_element_by_id('MyTextBox').text