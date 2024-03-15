import pytest
from django.db import IntegrityError

from core.models import Artist

pytestmark = pytest.mark.django_db


def test_name_is_unique():
    Artist.objects.create(name="test")

    with pytest.raises(IntegrityError):
        Artist.objects.create(name="test")
        assert Artist.objects.count() == 1


def test_name_is_unique_upper_case():
    Artist.objects.create(name="test")

    with pytest.raises(IntegrityError):
        Artist.objects.create(name="TEST")
        assert Artist.objects.count() == 1
