from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import postForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#views for categories
def category_list(request):
    categories = get_object_or_404(Category)
    return render(request, 'blog/cat_list.html', {'categories': categories})

'''
  save the form with form.save and we add an author 
 (since there was no author field, and 
 this field is required). 
 commit=False means that we don't want to save the Post model yet – we want to add the author first. 
 Most of the time you will use form.save() without commit=False, 
 but this case, we need to supply it. 
 post.save() will preserve changes (adding the author) 
 and a new blog post is created!
'''

def new_post(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = postForm()
    return render(request, 'blog/edit_post.html', {'form': form})

# view to edit post
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = postForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})