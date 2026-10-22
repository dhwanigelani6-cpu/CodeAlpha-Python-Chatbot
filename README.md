
# CodeAlpha Python Flask Chatbot

A web-based customer support chatbot built using Python, Flask, HTML, CSS, and JavaScript.

## Features

- Interactive chat interface
- Instant responses to supported FAQ questions
- Predefined response patterns
- Flask REST endpoint for chat messages
- Input validation and error handling
- Automated tests using Python unittest
- Deployment configuration for Render

## Technologies

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- Gunicorn
- unittest

## Project Structure

```text
CodeAlpha-Python-Chatbot/
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
├── .gitignore
├── render.yaml
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha-Python-Chatbot.git
cd CodeAlpha-Python-Chatbot
```

Replace YOUR_USERNAME with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Run Tests

```bash
python -m unittest test_app.py -v
```

## Chat API

Endpoint: `POST /chat`

Example JSON request:

```json
{
  "message": "How can I get a refund?"
}
```

Example JSON response:

```json
{
  "response": "For a refund, please share your order details with our support team."
}
```

## Deployment

This project includes a `render.yaml` configuration and can be deployed to a compatible Python hosting service.

For a Gunicorn-based deployment, use:

```bash
gunicorn app:app
```

## Limitations

This version uses predefined FAQ patterns and rule-based matching. It does not currently use a trained machine learning model or generative AI API.

The example support information should be customized before using this project for a real business.

## Future Improvements

- Semantic search over a larger FAQ knowledge base
- Optional generative AI integration
- More comprehensive testing
- Persistent chat history
- Improved accessibility and multilingual support

## Author

Add your name here.

## Internship

CodeAlpha - Cloud Computing Internship
