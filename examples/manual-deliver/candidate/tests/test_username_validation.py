"""Selected commands can check only the properties they actually exercise."""

import unittest

from username_validation import register_username


class UsernameValidationTests(unittest.TestCase):
    def test_rejects_blank(self):
        # Intended selected Proofline command for illustrative R1 only.
        for username in ("", " ", "\t", "\n", "  \t \n"):
            with self.subTest(username=repr(username)):
                with self.assertRaises(ValueError):
                    register_username(username)

    def test_preserves_valid(self):
        # Separate R2 assertion, not part of the illustrated selected command.
        for username in ("alice", "Zoë", "  山田  ", "a b"):
            with self.subTest(username=username):
                self.assertEqual(register_username(username), username)


if __name__ == "__main__":
    unittest.main()
