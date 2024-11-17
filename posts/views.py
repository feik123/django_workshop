from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from FurryFunnies.utils import get_user_obj
from posts.forms import PostCreateForm
from posts.models import Post


class CreatePost(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('dash')
    template_name = 'posts/create-post.html'

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostDetails(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'
