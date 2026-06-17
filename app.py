import os
import streamlit as st
from groq import Groq

FAQ_DATA = """
# TechStore FAQ

## Products & Pricing
Q: What products do you sell?
A: We sell laptops, smartphones, tablets, headphones, smart home devices, and accessories.

Q: Do you offer student discounts?
A: Yes! Students get 10% off with a valid .edu email address. Apply at checkout.

Q: What is your price match policy?
A: We match prices from major retailers within 14 days of purchase. Contact support with proof.

## Shipping & Delivery
Q: How long does shipping take?
A: Standard shipping takes 3-5 business days. Express shipping (1-2 days) is available for $15.

Q: Do you ship internationally?
A: We currently ship to the US, Canada, UK, and Australia.

Q: Is free shipping available?
A: Yes, orders over $50 qualify for free standard shipping.

## Returns & Refunds
Q: What is your return policy?
A: Items can be returned within 30 days of purchase for a full refund, provided they are in original condition.

Q: How do I start a return?
A: Log into your account, go to Order History, select the item, and click Start Return. We will email you a prepaid label.

Q: When will I receive my refund?
A: Refunds are processed within 3-5 business days after we receive the returned item.

## Account & Orders
Q: How do I track my order?
A: You will receive a tracking number by email once your order ships. You can also track it under Order History in your account.

Q: Can I change or cancel my order?
A: Orders can be modified or cancelled within 1 hour of placement. After that, contact support immediately.

Q: I forgot my password. How do I reset it?
A: Click Forgot Password on the login page and follow the email instructions.

## Support
Q: How do I contact customer support?
A: Email support@techstore.com, call 1-800-TECHSTORE (Mon-Fri 9am-6pm EST), or use live chat on our website.

Q: Do you offer technical support for products?
A: Yes, our tech team is available Mon-Sat 10am-8pm EST. Premium support plans are also available for $9.99/month.

Q: What warranty do products come with?
A: Most products include a 1-year manufacturer warranty. Extended warranties (2 or 3 years) are available at checkout.
"""

SYSTEM_PROMPT = f"""You are a helpful customer service chatbot for TechStore, an electronics retailer.

Use the FAQ data below to answer customer questions accurately and helpfully.

{FAQ_DATA}

Guidelines:
- Be friendly, concise, and professional
- Answer based on the FAQ when possible
- If a question is not covered, acknowledge it and suggest contacting support@techstore.com
- Be empathetic if a customer seems frustrated"""

st.set_page_config(
    page_title="TechStore Support",
    page_icon="🛒",
    layout="centered",
)

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }

    .chat-header {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
        padding: 20px 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .chat-header h1 { margin: 0; font-size: 22px; font-weight: 700; }
    .chat-header p  { margin: 4px 0 0; font-size: 13px; color: #a0aec0; }

    .online-dot {
        width: 10px; height: 10px;
        background: #48bb78;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
    }

    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }

    .suggestion-btn button {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 6px 14px;
        font-size: 13px;
        color: #4a5568;
        cursor: pointer;
        transition: all 0.2s;
    }
    .suggestion-btn button:hover {
        background: #ebf8ff;
        border-color: #90cdf4;
        color: #2b6cb0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chat-header">
    <div style="font-size:36px">🛒</div>
    <div>
        <h1>TechStore Support</h1>
        <p><span class="online-dot"></span>Online · Typically replies instantly</p>
    </div>
</div>
""", unsafe_allow_html=True)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.history = [{"role": "system", "content": SYSTEM_PROMPT}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])

if not st.session_state.messages:
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown("👋 Hi! Welcome to **TechStore** support. How can I help you today?")

    st.markdown("**Quick questions:**")
    cols = st.columns(2)
    suggestions = [
        "What is your return policy?",
        "Do you offer free shipping?",
        "How do I track my order?",
        "Do you have student discounts?",
    ]
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                st.session_state.pending_input = suggestion
                st.rerun()

if "pending_input" in st.session_state:
    user_input = st.session_state.pop("pending_input")

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.history.append({"role": "user", "content": user_input})

    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.history,
        max_tokens=1024,
    )
    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.history.append({"role": "assistant", "content": reply})
    st.rerun()

if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.history.append({"role": "user", "content": user_input})

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Typing..."):
            client = Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.history,
                max_tokens=1024,
            )
            reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.history.append({"role": "assistant", "content": reply})

with st.sidebar:
    st.markdown("### 🛒 TechStore")
    st.markdown("---")
    st.markdown("**📞 Contact Us**")
    st.markdown("📧 support@techstore.com")
    st.markdown("📱 1-800-TECHSTORE")
    st.markdown("🕒 Mon-Fri, 9am–6pm EST")
    st.markdown("---")
    st.markdown("**⚡ Quick Links**")
    st.markdown("• [Track Order](#)")
    st.markdown("• [Start a Return](#)")
    st.markdown("• [My Account](#)")
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.history = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.rerun()
