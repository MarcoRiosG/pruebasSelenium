import pytest
import unittest
from selenium import webdriver

from pages.special_suggestion import SpecialSuggestions

class TestSpecialPage():

    def test_special_suggestions_page(self):

        special_suggestions = SpecialSuggestions()
        TEST_SEARCH = "meteorito"
        suggestion_titles_lower = []
        suggestions_text_lower = []
        suggestions_titles, suggestions_texts = special_suggestions.presented_suggestions()
        for suggestion in suggestions_titles:
            suggestion_titles_lower.append(suggestion.lower())
        for suggestion_text in suggestions_texts:
            suggestions_text_lower.append(suggestion_text.lower())
        assert TEST_SEARCH in suggestions_text_lower or TEST_SEARCH in suggestion_titles_lower

        special_suggestions.big_search_bar()
        new_suggestions_titles_lower = []
        new_suggestions_text_lower = []
        new_suggestions_titles, new_suggestions_texts = special_suggestions.presented_suggestions()
        for suggestion in new_suggestions_titles:
            new_suggestions_titles_lower.append(suggestion.lower())
        for suggestion_text in new_suggestions_texts:
            new_suggestions_text_lower.append(suggestion_text.lower())
        assert TEST_SEARCH in new_suggestions_titles_lower and TEST_SEARCH in new_suggestions_text_lower

        special_suggestions.quit_driver()

#@pytest.mark.usefixtures("oneTimeSetUp")
# class TestSpecialPage(unittest.TestCase):

    #@pytest.fixture(autouse=True)
    # def setUp(self, oneTimeSetUp):
    #     self.special_suggestions = SpecialSuggestions(self.driver)
    #     self.TEST_SEARCH = "meteorito"
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    # def test_suggestions(self):
    #
    #     suggestions_titles, suggestions_texts = self.special_suggestions.presented_suggestions()
    #
    #     assert self.TEST_SEARCH in suggestions_texts or self.TEST_SEARCH in suggestions_texts
    #
    #     self.special_suggestions.big_search_bar()
    #
    #     new_suggestions_titles, new_suggestions_texts = self.special_suggestions.presented_suggestions()
    #
    #     assert suggestions_titles == new_suggestions_titles and suggestions_texts == new_suggestions_texts
