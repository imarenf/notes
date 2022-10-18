from django.test import TestCase

from .models import Note, Category


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='test_title', description='test_description')

    def test_title_content(self):
        category = Category.objects.get(id=1)
        expected_title = f'{category.title}'
        self.assertEqual(expected_title, 'test_title')

    def test_description_content(self):
        category = Category.objects.get(id=1)
        expected_description = f'{category.description}'
        self.assertEqual(expected_description, 'test_description')


class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='test_title_category', description='test_description')
        Note.objects.create(title='test_title', category=Category.objects.get(id=1))

    def test_title_content(self):
        note = Note.objects.get(id=1)
        expected_title = f'{note.title}'
        self.assertEqual(expected_title, 'test_title')

    def test_category_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.category.title, 'test_title_category')
        self.assertEqual(note.category.description, 'test_description')
