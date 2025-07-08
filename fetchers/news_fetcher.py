import feedparser

def fetch_news(ticker="AAPL"):
    url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:5]:
        articles.append({"title": entry.title, "summary": entry.summary, "link": entry.link})
    return articles