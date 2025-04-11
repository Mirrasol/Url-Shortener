# from django.contrib import messages
# from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, HttpResponseRedirect, redirect, render
from django.urls import reverse_lazy

from .forms import URLForm
from .models import URL


@login_required
def create_short_url(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='links/shortener.html',
            context={'form': URLForm(), 'url': request.user.urls.last()},
        )
    elif request.method == 'POST':
        form = URLForm(data=request.POST)
        if form.is_valid():
            url = URL(
                url=form.cleaned_data['url'],
                user=request.user,
            )
            url.save()

    return redirect(reverse_lazy('shorten_url'))


def redirect_to_shortened(request, hash):
    url = get_object_or_404(URL, hash=hash)
    url.visits_count += 1
    url.save()
    return HttpResponseRedirect(redirect_to=url.url)


@login_required
def get_urls_list(request):
    urls = request.user.urls.all()
    return render(
        request=request,
        template_name='links/urls_list.html',
        context={'urls': urls},
    )

# def register_user(request):
#     if request.user.is_authenticated:
#         return redirect("homepage")
#
#     elif request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request=request, user=user)
#             messages.success(request, 'Registration Successful!')
#             return redirect("homepage")
#         return render(
#             request=request,
#             template_name='links/sign_up.html',
#             context={"form": form},
#             status=403,
#         )
#
#     return render(
#         request=request,
#         template_name='links/sign_up.html',
#         context={'form': UserCreationForm()},
#     )
#
# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect("homepage")
#    
#     elif request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             login(request=request, user=user)
#             return redirect("homepage")
#         return render(
#             request=request,
#             template_name='links/login.html',
#             context={"form": form},
#             status=403,
#         )
#
#     return render(
#         request=request,
#         template_name='links/login.html',
#         context={'form': AuthenticationForm()},
#     )
#
#
# def logout_user(request):
#     logout(request)
#     messages.add_message(request, messages.INFO, "You have been logged out")
#     return redirect("homepage")
#