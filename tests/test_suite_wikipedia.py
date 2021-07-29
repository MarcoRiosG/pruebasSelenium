#******USELESS AT THE MOMENT*******
import unittest
from tests.test_main_wikipedia import TestMainPage
from tests.test_special_suggestions import TestSpecialPage
from tests.test_article import TestArticlePage

testmain = unittest.TestLoader().loadTestsFromTestCase(TestMainPage)
testarticle = unittest.TestLoader().loadTestsFromTestCase(TestArticlePage)
testspecial = unittest.TestLoader().loadTestsFromTestCase(TestSpecialPage)

test_suite = unittest.TestSuite([testmain, testarticle, testspecial])

unittest.TextTestRunner(verbosity=2).run(test_suite)