from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms

from blog_vai.blogs.models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_image', 'title', 'category', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post
        self.helper.layout = Layout(
            Row(
                Column('blog_image', css_class='form-control mb-4'),
            ),
            Row(
                Column('title', css_class=' form-group col-md-6 mb-0'),
                Column('category', css_class='form-group col-md-6 mb-3'),
                css_class='form-row; flex-direction: row; justify-content: center;'
            ),

            Row(
                Column('description')
            ),

            Submit('submit', 'Create Blog', css_class='mt-3'),
        )


class BlogEditForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_image', 'title', 'category', 'description')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('blog_image', css_class='form-control mb-4')
            ),
            Row(
                Column('title', css_class='form-group col-md-6 mb-2'),
                Column('category', css_class='form-group col-md-6 mb-0'),

                # css_class='form-row'
            ),

            Row(
                'description', css_class='form-group row-md-6 mb-2 ',
            ),

            Row(
                Submit('submit', 'Update', css_class='mt-3 mb-2'),
                HTML('<a class="btn btn-danger" href="javascript:history.back()">Cancel</a>')
            )
        )
