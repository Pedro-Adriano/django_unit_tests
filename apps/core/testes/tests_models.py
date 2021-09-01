from django.test import TestCase

from ..models import People


class PeopleTestCase(TestCase):
    def set_up(self):
        People.objects.create(name="Francisco André", years=38)

    def test_return_str(self):
        people = People.objects.get(name="Francisco André")
        self.assertEqual(people.__str__(), "Francisco")
