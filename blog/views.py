from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic
from .models import Post
from .forms import CommentForm, LoginForm, UserRegistration
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


@login_required
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():


            new_comment = comment_form.save(commit=False)

            new_comment.post = post

            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("You are authenticated")

            else:
                return HttpResponse("Invalid Login")

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():

            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})

    else:
        user_form = UserRegistration()

    return render(request, 'account/register.html', {'user_form': user_form})
