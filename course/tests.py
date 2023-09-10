from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from course.models import *
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="test@example.com", password="TestPassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_lesson(self):
        '''  Тестирование создания урока  '''

        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'joplesson',
            'description': 'youtube.com'
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_course(self):
        '''  Тестирование создания урока  '''

        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'jopcourse',
            'description': 'youtube.com'
        }

        response = self.client.post(
            '/courses/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_subscription(self):
        """ Тестирование создания подписки"""
        self.client.force_authenticate(user=self.user)
        sub = Course.objects.create(
            title="JAVA-developer",
            description="Курс для BACKEND разработчиков на JAVA",
            preview='',

        )
        data = {
            "course": sub.pk
        }
        response = self.client.post(
            '/subscription/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )