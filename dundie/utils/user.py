from random import sample
from string import ascii_letters, digits


def generate_simple_password(length=8):
    """Generate a simple password"""
    return "".join(sample(ascii_letters + digits, length))
