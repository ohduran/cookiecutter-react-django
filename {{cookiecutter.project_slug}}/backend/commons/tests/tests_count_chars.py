import pytest

from django.shortcuts import reverse
from faker import Faker
from rest_framework import status

fake = Faker()

@pytest.mark.django_db
class TestCharCount:

    def test_char_count(self, client, django_assert_num_queries):
        test_word = fake.word()
        with django_assert_num_queries(0):
            res = client.get(f"{reverse('char_count')}?text={test_word}")

        assert status.HTTP_200_OK == res.status_code, res.content
        assert {'count': len(test_word)} == res.json()
