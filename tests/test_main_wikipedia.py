import pytest
import unittest
from selenium import webdriver
from pages.main_page import MainPage

class TestMainPage():

    def test_main_page(self):
        main = MainPage()
        TEST_SEARCH = "meteorito"
        suggestions = main.search()

        for suggestion in suggestions:
            assert TEST_SEARCH in suggestion.lower()

        main.quit_driver()

#@pytest.mark.usefixtures("oneTimeSetUp")
# class TestMainPage(unittest.TestCase):

    #@pytest.fixture(autouse=True)
    # def setUp(self, oneTimeSetUp):
    #     self.main = MainPage(self.driver)

#     def __init__(self):
#         self.main = MainPage()
#
#     def test_suggestions(self):
#
#         TEST_SEARCH = "meteorito"
#         suggestions = self.main.search()
#
#         for suggestion in suggestions:
#             assert TEST_SEARCH in suggestion.lower()
#
#     def quit_driver(self):
#         self.main.quit_driver()
#
# mt = TestMainPage()
# mt.test_suggestions()
# mt.quit_driver()

