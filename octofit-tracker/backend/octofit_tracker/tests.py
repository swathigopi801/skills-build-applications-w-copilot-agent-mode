from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)
        self.workout = Workout.objects.create(name='Pushups', difficulty='Easy')

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)
