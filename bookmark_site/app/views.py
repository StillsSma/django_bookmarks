from django.shortcuts import render
from app.models import Bookmark
from django.views import View
from app.forms import BookmarkForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class BookmarkView(ListView):
    template_name = "index.html"
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ("full_url", "title", "description")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

def blank_view(request, short_url):
    return render(request, "index.html")
