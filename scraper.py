# scraper.py
from playwright.sync_api import sync_playwright

class XBookmarkScraper:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.context = None
        self.page = None

    def login(self):
        with sync_playwright() as p:
            # ブラウザ起動
            browser = p.chromium.launch(headless=False)  # 開発中はheadless=Falseで見えるように
            self.context = browser.new_context()
            self.page = self.context.new_page()

            # X（旧Twitter）ログインページへアクセス
            self.page.goto("https://x.com/login")

            # ログインフォーム操作（詳細設計書やHTML構造に基づき適宜修正）
            self.page.fill('input[name="text"]', self.username)
            self.page.press('input[name="text"]', "Enter")
            self.page.fill('input[name="password"]', self.password)
            self.page.press('input[name="password"]', "Enter")

            # 成功するまで待機（適宜待ち条件を追加する）
            self.page.wait_for_load_state("networkidle")

    def goto_bookmarks(self):
        # ブックマークページへのURLへ直接アクセス、あるいはUI操作で遷移
        # URL例: "https://x.com/i/bookmarks"
        self.page.goto("https://x.com/i/bookmarks")
        self.page.wait_for_load_state("networkidle")

    def extract_tweets(self) -> list[dict]:
        # ツイート要素をセレクタで特定
        # セレクタは実際のDOM構造に合わせて修正
        tweet_elements = self.page.query_selector_all('article[data-testid="tweet"]')

        tweets = []
        for el in tweet_elements:
            text_el = el.query_selector('div[data-testid="tweetText"]')
            user_el = el.query_selector('div[role="link"] > span')
            tweet_text = text_el.inner_text() if text_el else ""
            user_name = user_el.inner_text() if user_el else "Unknown"
            link_el = el.query_selector('a[href*="/status/"]')
            tweet_url = link_el.get_attribute("href") if link_el else ""

            tweets.append({
                "text": tweet_text,
                "user": user_name,
                "url": "https://x.com" + tweet_url
            })
        return tweets

    def close(self):
        if self.context:
            self.context.close()
