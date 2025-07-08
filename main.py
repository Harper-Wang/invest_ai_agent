from fetchers.news_fetcher import fetch_news
from agents.llm_analyzer import summarize_and_analyze
from notifiers.email_sender import send_email

if __name__ == "__main__":
    ticker = "AAPL"
    articles = fetch_news(ticker)
    body = ""
    for article in articles:
        analysis = summarize_and_analyze(article["summary"])
        body += f"标题：{article['title']}\n链接：{article['link']}\n{analysis}\n\n"

    send_email(
        subject=f"{ticker} 最新分析摘要",
        content=body,
        to_email="RECEIVER_EMAIL@example.com",
        from_email="YOUR_EMAIL@example.com",
        smtp_server="smtp.gmail.com",
        smtp_port=465,
        username="YOUR_EMAIL@example.com",
        password="YOUR_APP_PASSWORD"
    )
