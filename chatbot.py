import os
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
A: Log into your account, go to Order History, select the item, and click "Start Return." We will email you a prepaid label.

Q: When will I receive my refund?
A: Refunds are processed within 3-5 business days after we receive the returned item.

## Account & Orders
Q: How do I track my order?
A: You will receive a tracking number by email once your order ships. You can also track it under "Order History" in your account.

Q: Can I change or cancel my order?
A: Orders can be modified or cancelled within 1 hour of placement. After that, contact support immediately.

Q: I forgot my password. How do I reset it?
A: Click "Forgot Password" on the login page and follow the email instructions.

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


def main():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY environment variable not set.")
        print("Get a free key at: https://console.groq.com")
        return

    client = Groq(api_key=api_key)
    history = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("=" * 50)
    print("  TechStore Customer Support Chatbot")
    print("  Powered by Groq (Free)")
    print("=" * 50)
    print("Hi! I am TechStore's support assistant.")
    print("How can I help you today? (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "bye"):
            print("\nAssistant: Thanks for visiting TechStore! Have a great day!")
            break

        history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=history,
            max_tokens=1024,
        )

        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})

        print(f"\nAssistant: {reply}\n")


if __name__ == "__main__":
    main()
