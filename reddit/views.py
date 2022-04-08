from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.utils.text import slugify

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render (
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comments = post.comments.order_by('created_on')
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True

            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                comment_form = CommentForm()

            return render (
                request,
                "post_detail.html",
                {
                    "post": post,
                    "comments": comments,
                    "liked": liked,
                    "comment_form": comment_form
                },
            )

class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PostCreate(View):
    
    def get(self, request):

        return render(request, "create_post.html",
        {
        "post_form": PostForm()
        },
        )      

    def post(self, request, *args, **kwargs):

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.instance.email = request.user.email
            post_form.instance.name = request.user.username
            post.author = request.user
            post_form.instance.slug = slugify(post.title)
            post.save()
            return redirect('home')
        else:
            post_form = PostForm()

        return render(request, "create_post.html",
        {
        "post_form": PostForm()
        })


class UpdatePost(View):
    
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        return render (
            request,
            "update_post.html",
            {
                "post_form": PostForm(instance=post)
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post_form = PostForm(data=request.POST, instance=post)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.instance.email = request.user.email
            post_form.instance.name = request.user.username
            post.author = request.user
            post_form.instance.slug = slugify(post.title)
            post.save()
            return redirect('home')
        else:
            post_form = PostForm(instance=post)

class DeletePost(View):

    def get(self, request, slug, *args, **kwargs):
        return render(request, "delete.html")

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')

class ProfilePostList(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        user_posts = Post.objects.filter(author=request.user).order_by('-updated_on')
        return render(request, "user_profile.html", {
            "user_posts": user_posts,
            "user": user,
        })


    