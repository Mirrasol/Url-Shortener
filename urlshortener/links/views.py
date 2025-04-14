from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import URLForm
from .models import URL


@login_required
def create_short_url(request):
    """
    Create a short URL using hash.
    """
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


@login_required
def redirect_to_shortened(request, hash):
    """
    Redirect to a URL using short version,
    update visits counter for that short link.
    """
    url = get_object_or_404(URL, hash=hash)
    url.visits_count += 1
    url.save()
    return HttpResponseRedirect(redirect_to=url.url)


@login_required
def get_urls_list(request):
    """
    Get a list of all shortened URLs saved by the current user.
    """
    urls = request.user.urls.all()
    return render(
        request=request,
        template_name='links/urls_list.html',
        context={'urls': urls},
    )
