import gradio as gr
from fetchers.news_fetcher import fetch_news
from agents.llm_analyzer import summarize_and_analyze

def analyze_ticker(ticker):
    news_list = fetch_news(ticker)
    results = []
    for article in news_list:
        result = summarize_and_analyze(article["summary"])
        results.append(f"标题：{article['title']}\n链接：{article['link']}\n分析：\n{result}\n")
    return "\n\n".join(results)

demo = gr.Interface(fn=analyze_ticker, inputs="text", outputs="text", title="美股智能分析助手", description="输入股票代码（如 AAPL、TSLA），获取最近新闻分析")

if __name__ == "__main__":
    demo.launch()