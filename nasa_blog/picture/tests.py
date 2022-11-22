import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from picture.models import Picture


class PictureTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Picture.objects.create(title_name="Foto", taken_by="Persona", owner=self.test_user)
        Picture.objects.create(title_name="Imagen2", taken_by="Instrumento", owner=self.test_user)

        picture_test_num = 20
        self.mock_title_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(picture_test_num)
        ]
        self.mock_taken_bys = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(picture_test_num)
        ]

        for mock_title_names, mock_taken_bys in zip(self.mock_title_names, self.mock_taken_bys):
            Picture.objects.create(title_name=mock_title_names, taken_by=mock_taken_bys, owner=self.test_user)

    def test_picture_model(self):
        """Pictures creation are correctly identified"""
        foto_picture = Picture.objects.get(title_name="Foto")
        imagen2_picture = Picture.objects.get(title_name="Imagen2")
        self.assertEqual(foto_picture.owner.username, "testuser")
        self.assertEqual(imagen2_picture.owner.username, "testuser")
        self.assertEqual(foto_picture.taken_by, "Persona")
        self.assertEqual(imagen2_picture.taken_by, "Instrumento")

    