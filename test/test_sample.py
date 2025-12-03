import sys
import os

# Add project root folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add

def test_add():
    assert add(2, 3) == 5

