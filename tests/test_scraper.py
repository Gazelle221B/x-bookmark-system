import os
import pytest
from dotenv import load_dotenv
from scraper import XBookmarkScraper

# .env読み込みはフィクスチャ定義前に行う
load_dotenv()

@pytest.fixture(scope="session")
def credentials():
    # ここでX_USERNAME, X_PASSWORDが.envから読み込まれる
    return {
        "username": os.environ["X_USERNAME"],
        "password": os.environ["X_PASSWORD"]
    }

def test_scraper_bookmarks(credentials):
    scraper = XBookmarkScraper(credentials["username"], credentials["password"])
    scraper.login()
    scraper.goto_bookmarks()
    tweets = scraper.extract_tweets()

    assert len(tweets) > 0, "No tweets found in bookmarks"
    assert all("text" in t for t in tweets)
    assert all("url" in t for t in tweets)

    scraper.close()
