import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI

# ====== CONFIG ======
NEWS_API_KEY = "c80f24235c2747bb8d99c6e574489ddf"

EMAIL = "adhityasoul007@gmail.com"
APP_PASSWORD = "lqwv znok stsf rjth"
TO_EMAIL = "adhityasoul007@gmail.com"

# ====== FETCH NEWS ======
def get_tech_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "technology",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = data["articles"]

    news_list = []

    for article in articles:
        news_list.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        })

    return news_list

# ========Summary========
def format_news_email(news_list):
    content = "Daily Tech Brief\n"
    content += "=" * 40 + "\n\n"

    for i, news in enumerate(news_list, 1):
        content += f"{i}. {news['title']}\n"
        
        if news["description"]:
            content += f"{news['description']}\n"
        
        content += f"Read more: {news['url']}\n\n"

    return content

# ====== EMAIL ======
def send_email(content):
    subject = "Daily AI Tech Summary"

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(content, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()

    print("AI Summary Email Sent!")


# ====== MAIN ======
if __name__ == "__main__":
    news_list = get_tech_news()
    
    email_content = format_news_email(news_list)

    print(email_content)

    send_email(email_content)