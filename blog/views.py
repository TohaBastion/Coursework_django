from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm


def blog_home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_home.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all().order_by('-created_at')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect('blog_detail', pk=post.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments, 'form': form})