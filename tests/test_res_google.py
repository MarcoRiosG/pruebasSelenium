from tasks.google_search import GoogleSearch

def test_search_5():

    _word_search = "github"
    test = GoogleSearch()
    results = test.search()

    for result in results:
        assert _word_search in result.lower()

test_search_5()
