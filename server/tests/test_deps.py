import unittest
import importlib

class TestDependencies(unittest.TestCase):
    def test_livekit_agents_installed(self):
        try:
            importlib.import_module('livekit.agents')
            installed = True
        except ImportError:
            installed = False
        self.assertTrue(installed, "livekit-agents is not installed")

    def test_deepgram_installed(self):
        try:
            importlib.import_module('livekit.plugins.deepgram')
            installed = True
        except ImportError:
            installed = False
        self.assertTrue(installed, "livekit-plugins-deepgram is not installed")

    def test_google_installed(self):
        try:
            importlib.import_module('livekit.plugins.google')
            installed = True
        except ImportError:
            installed = False
        self.assertTrue(installed, "livekit-plugins-google is not installed")

if __name__ == '__main__':
    unittest.main()
