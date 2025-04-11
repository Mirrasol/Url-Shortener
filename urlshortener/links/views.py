# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import redirect, render


# def register_user(request):
#     if request.user.is_authenticated:
#         return redirect("homepage")
    
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

#     return render(
#         request=request,
#         template_name='links/sign_up.html',
#         context={'form': UserCreationForm()},
#     )

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