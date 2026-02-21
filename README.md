# 📰 Daily Tech News Agent

An automated cloud-based Python agent that fetches the latest technology news and delivers a well-formatted summary via email every day at **10:00 AM IST**.

This project runs automatically using **GitHub Actions**, so it works even when your laptop is turned off.

---

## 🚀 Features

* Fetches latest **Technology News** in real time using NewsAPI
* Extracts:

  * Title
  * Short description
  * Source link
* Formats news into a clean **Daily Tech Brief**
* Sends email using Gmail SMTP
* Runs automatically every day via GitHub Actions
* Fully cloud-based automation (no local system required)

---

## 🛠️ Tech Stack

* Python
* Requests (API integration)
* NewsAPI
* Gmail SMTP
* GitHub Actions (Cloud Scheduler)

---

## 📂 Project Workflow

```
NewsAPI → Fetch Articles → Format Summary → Send Email → GitHub Actions Scheduler
```

---

## 📁 Project Structure

```
tech-news-agent/
│
├── main.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── news.yml
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/tech-news-agent.git
cd tech-news-agent
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Get Required Credentials

#### NewsAPI Key

1. Go to: https://newsapi.org
2. Create a free account
3. Copy your API key

---

#### Gmail App Password

1. Enable **2-Step Verification** in your Google account
2. Go to **App Passwords**
3. Generate a password for:

   * App: Mail
   * Device: Other (Python)
4. Copy the 16-character password (without spaces)

---

## 🔐 Add Secrets in GitHub

Go to:

**Repository → Settings → Secrets and variables → Actions**

Add the following secrets:

| Name         | Description                     |
| ------------ | ------------------------------- |
| NEWS_API_KEY | Your NewsAPI key                |
| EMAIL        | Your Gmail address              |
| APP_PASSWORD | Gmail App Password              |
| TO_EMAIL     | Email where news should be sent |

---

## ⏰ Automation Schedule

The workflow runs daily at:

**10:00 AM IST**

Cron configuration (UTC):

```
30 4 * * *
```

You can also trigger it manually from the **Actions** tab.

---

## 📧 Sample Email Output

```
Daily Tech Brief
========================================

1. Samsung Galaxy S26 Ultra Launch
Samsung introduces its latest flagship smartphone with improved performance and camera.
Read more: https://...

2. Google AI Update
Google expands its AI capabilities with new tools for developers.
Read more: https://...
```

---

## 🎯 Use Case

This project demonstrates:

* API Integration
* Cloud Automation
* Secure Environment Variables
* Email Notification Systems
* Real-world Python automation

Suitable for:

* Portfolio / Resume
* Automation learning
* Beginner DevOps projects

---

## 🔮 Future Improvements

* HTML email newsletter design
* AI-based news filtering (AI/ML only)
* WhatsApp notifications
* Cloud deployment with database history

---

## 📜 License

This project is for educational and personal use.
