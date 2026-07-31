ts for Base class."""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_auto_id(self):
        """Test automatic ID assignment."""

        b1 = Base()
        b2 = Base()

        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Test Base with given ID."""

        b = Base(89)

        self.assertEqual(b.id, 89)

    def test_to_json_none(self):
        """Test None conversion."""

        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        """Test empty list conversion."""

        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_list(self):
        """Test list conversion."""

        result = Base.to_json_string([{"id": 12}])

        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_none(self):
        """Test None JSON."""

        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """Test empty JSON list."""

        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_list(self):
        """Test JSON list."""

        result = Base.from_json_string('[{"id": 89}]')

        self.assertEqual(result, [{"id": 89}])


if __name__ == "__main__":
    unittest.main()
