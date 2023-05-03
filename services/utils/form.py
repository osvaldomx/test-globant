"""
Test Globant >
"""

from wtforms import Form
from wtforms import HiddenField
from wtforms import StringField
from wtforms import validators

class BasicForm(Form):
    method = 'post'
    _method = HiddenField("", default=method)

    country_code = StringField("Country code", [
        validators.DataRequired(message="Country code is required."),
        validators.Length(min=2, max=2)
    ])

    city = StringField("City", [
        validators.DataRequired(message="City is required.")
    ])