from unittest import TestCase

from app.controllers.morse import MorseController


class MorseControllerTest(TestCase):
    def setUp(self):
        self.morse_controller = MorseController()

        self.default_message = '--- .-.. .-'
        self.defatul_translated_message = 'OLA'
    
    def test_when_I_call_translate_should_be_success(self):
        translated = self.morse_controller.translate_word(self.default_message)
        self.assertEqual(self.defatul_translated_message, translated)