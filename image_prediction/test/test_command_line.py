from unittest import TestCase

from image_prediction.command_line import main


class TestCmd(TestCase):
    def test_basic(self):
        main()