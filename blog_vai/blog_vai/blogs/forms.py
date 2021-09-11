from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from blog_vai.blogs.models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'theme', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post
        self.helper.layout = Layout(
            Row(
                Column('title', css_class=' form-group col-md-6 mb-0'),
                Column('theme', css_class='form-group col-md-6 mb-3'),
                css_class='form-row; flex-direction: row; justify-content: center;'
            ),
            Row(
                Column('description')
            ),
            Submit('submit', 'Create Blog', css_class='mt-3')
        )