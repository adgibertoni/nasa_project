import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from new.models import New


class NewTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        New.objects.create(title="Titulo1", header="prueba para el 1", owner=self.test_user)
        New.objects.create(title="Titulo 2", header="funcionará el 2?", owner=self.test_user)

        new_test_num = 20
        self.mock_title = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(new_test_num)
        ]
        self.mock_header = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(new_test_num)
        ]

        for mock_title, mock_header in zip(self.mock_title, self.mock_header):
            New.objects.create(title=mock_title, header=mock_header, owner=self.test_user)

    def test_new_model(self):
        """News creation are correctly identified"""
        titulo1_new = New.objects.get(title="Titulo1")
        titulo2_new = New.objects.get(title="Titulo 2")
        self.assertEqual(titulo1_new.owner.username, "testuser")
        self.assertEqual(titulo2_new.owner.username, "testuser")
        self.assertEqual(titulo1_new.header, "prueba para el 1")
        self.assertEqual(titulo2_new.header, "funcionará el 2?")
