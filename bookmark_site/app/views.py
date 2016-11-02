from django.shortcuts import render
from app.models import Bookmark, Click
from django.views import View
from app.forms import BookmarkForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from hashids import Hashids


# Create your views here.
class BookmarkView(ListView):
    template_name = "index.html"
    model = Bookmark

    def get_queryset(self):
        return Bookmark.objects.filter(is_private=False)

class ProfileView(ListView):
    template_name = "profile.html"
    model = Bookmark

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)




class BookmarkCreateView(CreateView):
    model = Bookmark
    success_url = reverse_lazy("profile_view")
    fields = ("full_url", "title", "description", "is_private")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ("full_url", "title", "description", "is_private")
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("profile_view")

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy("profile_view")

def redirect_view(request, short_url):
    number = Hashids().decode(short_url)
    var = Bookmark.objects.get(pk=number[0] - 1000000)
    user = request.user
    #bookmark = Bookmark.objects.get(id=7)
    if request.method == 'GET':
        c = Click(user=user ,bookmark=var ,value=True)
        c.save()

        return redirect(var.full_url)

class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy("bookmark_view")
    form_class = UserCreationForm
