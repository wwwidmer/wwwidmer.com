from django.test import TestCase
from django.utils import timezone
from wwwidmer.models import *
from datetime import datetime
import time


class PageTestCase(TestCase):
    def setUp(self):
        page.objects.create(title="Test1",descript="A test",content="Some content",onMenu=False)
        page.objects.create(title="Test2",descript="A test2",content="Some content again",onMenu=True)
    def test_is_menu(self):
        onMenu = page.objects.filter(onMenu=True)
        offMenu = page.objects.filter(onMenu=False)
        test1 = page.objects.get(title="Test1")
        test2 = page.objects.get(title="Test2")
        self.assertNotEqual(onMenu,offMenu)
        self.assertEqual(test1.onMenu,False)
        self.assertEqual(test2.onMenu,True)
    def test_content_title_description(self):
        test1 = page.objects.get(title="Test1")
        self.assertEqual(test1.title,"Test1")
        self.assertEqual(test1.descript,"A test")
        self.assertEqual(test1.content,"Some content")
class BlogTestCase(TestCase):
    def setUp(self):
        blog1 = blog.objects.create(title="Blog1",descript="Blog1",content="Blog1",pub_date=timezone.now())
        time.sleep(2)
        blog2 = blog.objects.create(title="Blog2",descript="Blog2",content="Blog2",pub_date=timezone.now())
    def test_pub_date(self):
        allBlogs = blog.objects.all()
        for blogs in allBlogs:
            for b in allBlogs:
                if blogs is b:
                    self.assertEqual(blogs.pub_date,b.pub_date)
                if blogs is not b:
                    self.assertNotEqual(blogs.pub_date,b.pub_date)
