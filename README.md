# 🛒 TechStore Support Chatbot

A customer service chatbot for a fictional electronics store, powered by **Groq AI (Llama 3.1)** — completely free to use.

---

## 📸 Preview

A clean chat UI with:
- Purple user bubbles & white bot replies
- Animated typing indicator
- Quick suggestion buttons
- Sidebar with store contact info

---

## 🚀 Quick Start

### 1. Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free, no credit card)
3. Click **API Keys → Create API Key**
4. Copy the key (starts with `gsk_...`)

### 2. Open the Chatbot

#### Option A — Web UI (Recommended)
Just open `index.html` in your browser. No installation needed.

#### Option B — Terminal Chatbot
```bash
pip install groq
export GROQ_API_KEY="gsk_your_key_here"
python3 chatbot.py
```

#### Option C — Streamlit UI
```bash
pip install streamlit groq
export GROQ_API_KEY="gsk_your_key_here"
streamlit run app.py
```

---

## 📁 Project Structure

```
Gen AI - Chatbot/
│
├── index.html        # Web chatbot UI (HTML + CSS + JS)
├── chatbot.py        # Terminal chatbot (Python)
├── app.py            # Streamlit web app (Python)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 💬 FAQ Topics Covered

| Category | Topics |
|---|---|
| Products & Pricing | Product range, student discounts, price match |
| Shipping | Delivery times, express shipping, free shipping, international |
| Returns & Refunds | Return policy, how to return, refund timeline |
| Account & Orders | Order tracking, cancellations, password reset |
| Support | Contact info, tech support, warranty |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI Model | Llama 3.1 8B Instant (via Groq) |
| Web UI | HTML, CSS, JavaScript |
| Terminal UI | Python |
| Streamlit UI | Python + Streamlit |
| API | Groq Chat Completions API |

---

## ⚙️ How It Works

1. A **system prompt** loads all FAQ data into the model's context
2. User messages are sent to the **Groq API** along with conversation history
3. The model replies based on the FAQ, maintaining context across turns
4. If a question isn't in the FAQ, it directs users to `support@techstore.com`

---

## 📦 Dependencies

```
groq>=0.9.0
streamlit>=1.28.0   # only needed for app.py
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Security

- **Never commit your API key** to version control
- Store it as an environment variable: `export GROQ_API_KEY="gsk_..."`
- Add a `.env` file to `.gitignore` if using one

---

## 📄 License

MIT — free to use and modify.
