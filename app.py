
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

FAQS = {
    "hello": "Hello! Welcome to our support chatbot. How can I help you?",
    "hi": "Hi there! What would you like to know?",
    "hours": "Our customer support is available Monday to Friday, 9 AM to 6 PM.",
    "price": "Please tell me which product or service you are interested in.",
    "payment": "We accept common online payment methods. Contact support for payment assistance.",
    "refund": "For a refund, please share your order details with our support team.",
    "contact": "You can contact our support team at support@example.com.",
    "services": "We provide customer support, product information, and order assistance.",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "bye": "Goodbye! Have a great day."
}


def get_response(message):
    message = message.lower().strip()

    if not message:
        return "Please type a question so I can help you."

    # Check longer phrases before shorter keywords.
    if "support hours" in message or "opening hours" in message:
        return FAQS["hours"]

    if "how can i get a refund" in message or "refund" in message:
        return FAQS["refund"]

    if "payment" in message or "pay" in message:
        return FAQS["payment"]

    if "price" in message or "cost" in message:
        return FAQS["price"]

    if "contact" in message or "email" in message:
        return FAQS["contact"]

    if "service" in message:
        return FAQS["services"]

    # Match standalone greetings and common phrases.
    words = set(message.replace("!", " ").replace("?", " ").replace(".", " ").split())

    if words.intersection({"hello", "hi", "hey"}):
        return FAQS["hello"]

    if "thanks" in words or "thank" in words:
        return FAQS["thanks"]

    if "bye" in words or "goodbye" in words:
        return FAQS["bye"]

    return (
        "Sorry, I don't have an answer for that yet. "
        "Try asking about services, prices, payments, refunds, "
        "support hours, or contact details."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Please send a valid JSON object."}), 400

    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({"error": "Message must be text."}), 400

    if len(message) > 1000:
        return jsonify({"error": "Message is too long. Maximum is 1000 characters."}), 400

    response = get_response(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
