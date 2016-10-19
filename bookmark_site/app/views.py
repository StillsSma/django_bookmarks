from django.shortcuts import render
from app.models import Bookmark, Click
from django.views import View
from app.forms import BookmarkForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from hashids import Hashids


# Create your views here.
class BookmarkView(ListView):
    template_name = "index.html"
    model = Bookmark

    def get_queryset(self):
        try:
            return Bookmark.objects.filter(user=self.request.user)
        except TypeError:
            return Bookmark.objects.all()



class BookmarkCreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ("full_url", "title", "description")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ("full_url", "title", "description")
    template_name_suffix = '_update_form'
    success_url = "/"

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = "/"

def redirect_view(request, short_url):
    number = Hashids().decode(short_url)
    var = Bookmark.objects.get(pk=number[0] - 1000000)
    user = request.user
    bookmark = Bookmark.objects.get(id=7)
    if request.method == 'GET':
        c = Click(user=user ,bookmark=var ,value=True)
        c.save()

        return redirect(var.full_url)

class UserCreateView(CreateView):
    model = User
    success_url = "/"
    form_class = UserCreationForm
