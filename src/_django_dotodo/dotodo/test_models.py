from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Task, Category


class TaskTests(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1')

    def test_task_categories(self):
        """
        test create and cascade delete
        """
        u = User.objects.create(username='user2')
        cat = Category.objects.create(cat_name="cat", user=u)
        t = Task.objects.create(title="title", description="...", user=u, category=cat)
        # test1 = Task.objects.filter(user=self.u1).first() - returns None
        # test adding one category and task on user 'u'
        self.assertIs(Task.objects.filter(user=self.u1.pk).exists(), False)
        self.assertIs(Task.objects.filter(user=u.pk).exists(), True)
        self.assertIs(Task.objects.filter(category=cat).exists(), True)

        # adding to user 'u1', deleting 'u'
        cat1 = Category.objects.create(cat_name="cat", user=self.u1)
        Task.objects.create(title="t1", description="...", user=self.u1, category=cat1)
        u.delete()
        self.assertIs(Task.objects.filter(user=self.u1.pk).exists(), True)
        self.assertIs(Task.objects.filter(title=t.title).exists(), False)
        self.assertIs(Category.objects.filter(user=u.pk).exists(), False)
        self.assertIs(Category.objects.filter(user=self.u1.pk).exists(), True)

    def tearDown(self):
        self.u1.delete()
