from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('service-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    categories = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categories_menu"] = categories_menu
        return context

def category_list_view(request):
    categories_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'categories_menu_list':categories_menu_list})


def category_view(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'categories.html', {'categories':categories.title().replace('-', ' '), 'category_posts': category_posts})

class ServiceDetailView(DetailView):
    model = Post
    template_name = 'service_details.html'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(ServiceDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["categories_menu"] = categories_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
