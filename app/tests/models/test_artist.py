from django.db import IntegrityError
from django.test import TestCase

from core.models import Artist


class ArtistTestCase(TestCase):

    def test_name_is_unique(self):
        Artist.objects.create(name="test")

        with self.assertRaises(IntegrityError):
            Artist.objects.create(name="test")
            self.assertEqual(Artist.objects.count(), 1)

    def test_name_is_unique_upper_case(self):
        Artist.objects.create(name="test")

        with self.assertRaises(IntegrityError):
            Artist.objects.create(name="TEST")
            self.assertEqual(Artist.objects.count(), 1)
