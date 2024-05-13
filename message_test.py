import unittest
from message_manager import messages


class test_Message(unittest.TestCase):
    def test_Message(self, sender, subject, recipient, message, label, priority=0):
        message = messages(self, sender, subject, recipient, message, label, priority)
        assert int(priority) == self.priority
        print()
        print(f"Tested message {priority} successfully")





    """def test_message(self, sender, subject, recipient, message, label, priority=0):
        self.sender = sender
        self.subject = subject
        self.recipient = recipient
        self.content = message
        self.label = label
        self.priority = priority
        self.unread = False

    def info(self):
        return f"{self.stars():8} {self.sender:25} {self.label:5} {self.subject}"

    def stars(self):
        stars = ""
        for i in range(self.priority):
            stars += "*"
        return stars"""
