# 📘 SarkariSphere – Your One-Stop Sarkari Naukri Portal

**SarkariSphere** is a powerful and user-friendly Streamlit app that delivers real-time government job updates, admit cards, and results — with **direct download/apply links** and **zero clutter**.

From SSC and UPSC to Railways and State-level recruitment, get all important updates in one place.

---

## 🚀 Features

✅ **Latest Jobs**

- Real-time job listing scraped from [sarkariresult.com](https://www.sarkariresult.com)
- Job titles, deadlines, and direct apply + notification links
- Filter by keyword or active status

📥 **Admit Cards**

- Skip redirections — download admit cards directly from the source

📊 **Results**

- One-click download for Sarkari results

🎯 **Clean UI/UX**

- Responsive layout using Streamlit
- Easy navigation with sidebar and collapsible sections

---

## 🛠️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io) – UI Framework
- [Selenium](https://selenium.dev) – Headless Chrome scraping
- [Lottie](https://lottiefiles.com) – For engaging animation on the homepage

---

## 📦 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/sarkarisphere.git
cd sarkarisphere
pip install -r requirements.txt
streamlit run main.py
```

## 📁 Folder Structure

```bash
sarkarisphere/
├── main.py              # App routing, menu logic
├── home.py              # Homepage layout and animation
├── job_open.py          # Latest job listings
├── datacollect.py       # Scraping logic for results and admit cards
├── job_admit_card.py    # Admit card UI and logic
├── job_result.py        # Result UI and logic
├── lotti/
│   └── lot.py           # Lottie animation JSON
├── requirements.txt     # Required packages
└── README.md            # You're reading it!
```


## 🔮 Future Enhancements

* Job alert via Email or WhatsApp
* Resume builder for job applications
* Smart job recommendations (AI-based)
* Multilingual UI (Hindi, Tamil, Bengali, etc.)
* Bookmark or save job listings
* Pagination and search filters for better UX

## 🧑‍💻 Author

**Sumit Kumar Singh**

Freelancer • Python Developer • Web Automation Enthusiast
