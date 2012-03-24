from django.test import TestCase
from burn.forms import BurnTextForm, BurnTextModelForm


class BurnModelFormTest(TestCase):
    def test_form_is_validate_char_255(self):
        data = { 'char_50': '1234567890000', 'char_255': 'test' }
        form = BurnTextModelForm(data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors,{'char_255': [u'This Field must have more than 10 char']})

    def test_form_is_validate_char_50(self):
        data = { 'char_50': 'test', 'char_255': '1234567890000' }
        form = BurnTextModelForm(data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors,{'char_50': [u'This Field must have more than 10 char']})

    def test_form_is_valid(self):
        data = { 'char_50': '123456789000', 'char_255': '123456789000' }
        form = BurnTextModelForm(data)
        self.assertTrue(form.is_valid())

class BurnFormTest(TestCase):
    def test_form_is_validate_char_255(self):
        data = { 'char_50': '1234567890000'}
        form = BurnTextForm(data)
        self.assertTrue(form.is_valid())

    def test_form_is_validate_char_null(self):
        data = { 'char_50': '1234567890000', 'char_null': 12334}
        form = BurnTextForm(data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors,
                {'char_null': [u'This Field must be null']})


