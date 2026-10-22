
import unittest
from app import app


class ChatbotTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CodeAlpha Assistant", response.data)

    def test_greeting(self):
        response = self.client.post(
            "/chat",
            json={"message": "hello"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello", response.get_json()["response"])

    def test_refund_question(self):
        response = self.client.post(
            "/chat",
            json={"message": "How can I get a refund?"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "refund",
            response.get_json()["response"].lower()
        )

    def test_empty_message(self):
        response = self.client.post(
            "/chat",
            json={"message": ""}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Please type a question",
            response.get_json()["response"]
        )

    def test_long_message_rejected(self):
        response = self.client.post(
            "/chat",
            json={"message": "a" * 1001}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_json_body(self):
        response = self.client.post(
            "/chat",
            data="invalid",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_non_text_message_rejected(self):
        response = self.client.post(
            "/chat",
            json={"message": 123}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
