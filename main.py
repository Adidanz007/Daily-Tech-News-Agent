import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ====== CONFIG (Read from GitHub Secrets / Environment) ======
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")


# ====== FETCH NEWS ======
def get_tech_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "technology",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") != "ok":
            print("Error fetching news:", data)
            return []

        articles = data["articles"]

        news_list = []
        for article in articles:
            news_list.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url")
            })

        return news_list

    except Exception as e:
        print("News API error:", e)
        return []


# ====== FORMAT EMAIL CONTENT ======
def format_news_email(news_list):
    if not news_list:
        return "No news available today."

    content = "Daily Tech Brief\n"
    content += "=" * 40 + "\n\n"

    for i, news in enumerate(news_list, 1):
        content += f"{i}. {news['title']}\n"

        if news["description"]:
            content += f"{news['description']}\n"

        content += f"Read more: {news['url']}\n\n"

    return content


# ====== SEND EMAIL ======
def send_email(content):
    subject = "Daily Tech News"

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(content, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Email error:", e)


# ====== MAIN ======
if __name__ == "__main__":
    print("Fetching tech news...")

    news_list = get_tech_news()
    email_content = format_news_email(news_list)

    print("\nGenerated Email Content:\n")
    print(email_content)

    send_email(email_content)
