"""Synthetic selected tests, authored for reading; not executed in a Gapline audit."""

import unittest

from src.registration import register


class RegistrationTests(unittest.TestCase):
    def test_empty_rejected(self) -> None:
        with self.assertRaises(ValueError):
            register("")

    def test_unicode_name_preserved(self) -> None:
        self.assertEqual(register("Åsa"), {"username": "Åsa"})


# Deliberately no whitespace-only case in these selected fixture tests.
