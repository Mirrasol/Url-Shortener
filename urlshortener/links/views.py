from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register_user(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect("main:home")
        return render(
            request=request,
            template_name='links/sign_up.html',
            context={"form": form},
            status=403,
        )

    return render(
        request=request,
        template_name='links/sign_up.html',
        context={'form': UserCreationForm()},
    )