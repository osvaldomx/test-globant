from services.utils.form import BasicForm

import pytest

class TestBasicForm:
    # Tests that the BasicForm class has a default method of 'post'. 
    def test_basic_form_default_method_is_post(self):
        form = BasicForm()
        assert form.method == 'post'

    # Tests submitting a form with valid country code and city. 
    def test_basic_form_valid_country_code_and_city(self):
        form_data = {'country_code': 'US', 'city': 'New York'}
        form = BasicForm(data=form_data)
        assert form.validate() is True

    # Tests submitting a form with empty country code. 
    def test_basic_form_empty_country_code(self):
        form_data = {'country_code': '', 'city': 'New York'}
        form = BasicForm(data=form_data)
        assert form.validate() is False

    # Tests submitting a form with invalid country code. 
    def test_basic_form_invalid_country_code(self):
        form_data = {'country_code': 'USA', 'city': 'New York'}
        form = BasicForm(data=form_data)
        assert form.validate() is False

    # Tests that the BasicForm class has a hidden field for the HTTP method. 
    def test_basic_form_has_hidden_method_field(self):
        form = BasicForm()
        assert '_method' in form._fields

    # Tests submitting a form with empty city. 
    def test_basic_form_empty_city(self):
        form_data = {'country_code': 'US', 'city': ''}
        form = BasicForm(data=form_data)
        assert form.validate() is False