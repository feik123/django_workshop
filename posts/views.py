from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.utils import get_user_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
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


class PostEdit(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')


class PostDelete(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

