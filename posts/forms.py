from django import forms

from FurryFunnies.mixins import ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

        help_texts = {
            'image_url': 'Share your funniest furry photo URL!'

        }
        error_messages = {
            'title':{
                'unique':'Oops! That title is already taken. How about something fresh and fun?',
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...'
            })
        }
        labels = {
            'title': 'Title:',
            'content': 'Content:',
        }

class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    pass

class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title','image_url', 'content']