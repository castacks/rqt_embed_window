#!/usr/bin/env python3

import unittest
import importlib

class TestImports(unittest.TestCase):
    def test_import_package(self):
        """Test that the package can be imported."""
        try:
            import rqt_embed_window
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import rqt_embed_window")
    
    def test_import_main_module(self):
        """Test that the main module can be imported."""
        try:
            from rqt_embed_window import RqtEmbedWindow
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import RqtEmbedWindow")
    
    def test_import_shell_cmd(self):
        """Test that the shell_cmd module can be imported."""
        try:
            from rqt_embed_window import shell_cmd
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import shell_cmd")

if __name__ == '__main__':
    unittest.main()