# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.views.generic.base import View
from .forms import LoginForm


# def login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username","")
#         print(user_name)
#     elif request.method == "GET":
#         return render(request, "login.html",{})


class loginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg":"用户未激活"})

# class LoginView(request):
#     def get(self, request):
#         print(request)
#         pass
#         return render(request, "login.html", {})
    # def post(self, request):
    #     login_form = LoginForm(request.POST)
    #     if login_form.is_valid():
    #         user_name = request.POST.get("username", "")
    #         pass_word = request.POST.get("password", "")
    #         user = authenticate(username=user_name, password=pass_word)
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect(reverse("index"))
    #             else:
    #                 return render(request, "login.html", {"msg":"用户未激活！"})
    #         else:
    #             return render(request, "login.html", {"msg":"用户名或密码错误！"})
    #     else:
    #         return render(request, "login.html", {"login_form":login_form})
