import pytest
import unittest

from pages.article_page import ArticlePage

class TestArticlePage():

    def test_article_page(self):
        article = ArticlePage()
        TEST_SEARCH = "meteorito"

        title = article.verify_article()
        assert TEST_SEARCH in title.lower()

        suggestions_article = article.search_from_article()

        for suggestion in suggestions_article:
            assert TEST_SEARCH in suggestion.lower()

        article.quit_driver()

# @pytest.mark.usefixtures("oneTimeSetUp")
# class TestArticlePage(unittest.TestCase):

    # @pytest.fixture(autouse=True)
    # def setUp(self, oneTimeSetUp):
    #     self.article = ArticlePage(self.driver)
    #     self.TEST_SEARCH = "meteorito"

    # def test_article(self):
    #     title = self.article.verify_article()
    #
    #     assert self.TEST_SEARCH in title.lower()
    #
    # def test_search(self):
    #     suggestions_article = self.article.search()
    #
    #     for suggestion in suggestions_article:
    #         assert self.TEST_SEARCH in suggestion.lower()

