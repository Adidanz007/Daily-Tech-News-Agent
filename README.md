# 📰 Daily Tech News Agent

An automated Python-based agent that fetches the latest technology news and sends a well-formatted summary to your email every day.

This project uses NewsAPI to collect real-time tech news, formats it into a readable newsletter-style report, and delivers it automatically via Gmail.

---

## 🚀 Features

* Fetches latest **Technology News** in real-time
* Extracts:

  * News title
  * Short description
  * Source link
* Formats content into a clean **Daily Tech Brief**
* Sends email automatically using Gmail SMTP
* Supports daily automation using Task Scheduler
* Fully automated workflow

---

## 🛠️ Tech Stack

* Python
* Requests (API integration)
* NewsAPI
* Gmail SMTP
* Windows Task Scheduler

---

## 📂 Project Workflow

```
NewsAPI → Fetch Articles → Format News → Send Email → Daily Automation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/tech-news-agent.git
cd tech-news-agent
```

---

### 2. Install Dependencies

```
pip install requests
```

---

### 3. Get NewsAPI Key

1. Go to: https://newsapi.org
2. Create a free account
3. Copy your API key

Update in `main.py`:

```
NEWS_API_KEY = "your_newsapi_key"
```

---

### 4. Configure Gmail

1. Enable **2-Step Verification** in your Google account
2. Generate an **App Password**
3. Update in `main.py`:

```
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
TO_EMAIL = "receiver_email@gmail.com"
```

---

## 📧 Sample Email Output

```
Daily Tech Brief
----------------------------------------

1. Samsung Galaxy S26 Ultra Launch
Samsung introduces its latest flagship smartphone with upgraded performance and camera features.
Read more: https://...

2. Google AI Update
Google expands its AI capabilities with new tools and features for developers.
Read more: https://...
```

---

## ⏰ Automation

To run automatically every day:

* Use **Windows Task Scheduler**
* Schedule `main.py` to run at your preferred time

---

## 📁 Project Structure

```
tech-news-agent/
│
├── main.py
├── README.md
```

---

## 🎯 Use Case

This project demonstrates:

* API Integration
* Python Automation
* Email Notification System
* Real-world data processing

Suitable for:

* Beginner Python projects
* Automation learning
* Portfolio / Resume

---

## 🔮 Future Improvements

* WhatsApp notification support
* AI-based news summarization
* Topic filtering (AI, Cloud, Programming)
* Cloud deployment (run 24/7)

---

## 📜 License

This project is for educational and personal use.
