import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestAgent(unittest.TestCase):
    def test_agent_module_has_main(self):
        try:
            import agent
            self.assertTrue(hasattr(agent, 'entrypoint'))
            self.assertTrue(hasattr(agent, 'prewarm'))
        except ImportError as e:
            self.fail(f"Failed to import agent module: {e}")

if __name__ == '__main__':
    unittest.main()
