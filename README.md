# 🛒 TechStore Support Chatbot

A customer service chatbot for a fictional electronics store, powered by **Groq AI (Llama 3.1)** — completely free to use.

---

## 📸 Preview

A clean chat UI with:
- Purple user bubbles & white bot replies
- Animated typing indicator
- Quick suggestion buttons

---

## 🚀 Quick Start

### 1. Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free, no credit card)
3. Click **API Keys → Create API Key**
4. Copy the key (starts with `gsk_...`)

### 2. Open the Chatbot
Just open `index.html` in your browser. It will prompt you to enter your API key on load. No installation needed.

---

## 📁 Project Structure

```
Gen AI - Chatbot/
│
├── index.html   # Web chatbot UI (HTML + CSS + JS)
└── README.md    # This file
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
| UI | HTML, CSS, JavaScript |
| API | Groq Chat Completions API |

---

## ⚙️ How It Works

1. FAQ data is loaded into the system prompt
2. User messages are sent to the **Groq API** along with conversation history
3. The model replies based on the FAQ, maintaining context across turns
4. If a question isn't in the FAQ, it directs users to `support@techstore.com`

---

## 🔑 API Key Security

- The key is entered via a popup on load — it is never saved or committed
- **Never hardcode your API key** in the source code

---

## 📄 License

MIT — free to use and modify.
