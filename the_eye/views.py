from django.shortcuts import render
from django.views.generic import ListView, DetailView
from the_eye.models import Session, Category, Time


def handle_not_found(request, exception):
    return render(request,'404.html')


class SessionListView(ListView):
    template_name = "the_eye/session_list.html"
    queryset = Session.objects.all

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryListView(ListView):
    template_name = "the_eye/category_list.html"
    queryset = Category.objects.all

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TimeListView(ListView):
    template_name = "the_eye/time_list.html"
    queryset = Time.objects.all

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


''' Here, the analytics team will be able to access event data
though the related Event model for Session, Category, and Time in the template. '''

class SessionDetailView(DetailView):
    model = Session
    template_name = "the_eye/session_detail.html"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "the_eye/category_detail.html"


class TimeDetailView(DetailView):
    model = Time
    template_name = "the_eye/time_detail.html"
