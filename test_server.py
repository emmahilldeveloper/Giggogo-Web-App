import unittest
import server

class app_function_test(unittest.TestCase):
    """Testing my Giggogo Flask server."""

    def test_homepage(self):
        client = server.app.test_client()
        result = client.get("/")
        print(result.data)
        self.assertIn(b'<head class="theme-style">', result.data) #checks that my template inheritance worked on my homepage