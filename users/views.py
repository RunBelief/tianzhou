# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.views import View
from users.forms import LoginForm
# Create your views here.
#首页
class IndexView(View):
    def get(self, request):
        return render(request,"index.htm", {})

#登入页面
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST) #获取到登录的DATA
        if login_form.is_valid(): #验证
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word) #验证user
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {'msg': '用户不存在'})
            else:
                return render(request, "login.html", {'meg': '密码错误'})
        return render(request, "login.html", {'login_form': login_form})











