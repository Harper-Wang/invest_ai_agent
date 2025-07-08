import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

def summarize_and_analyze(article_text):
    prompt = f"""
    你是一位美股投资顾问，请阅读以下财经新闻，并总结核心内容和对股票的影响（利好/利空/中性），并给出建议：
    
    新闻内容：{article_text}
    
    输出格式：
    - 摘要：...
    - 情绪判断：利好/利空/中性
    - 建议：买入/卖出/观望，并说明理由
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]