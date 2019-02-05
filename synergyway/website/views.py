from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import User, Group
from django.urls import reverse

# from .forms import NewStudentForm

# Create your views here.


class ListUsersView(ListView):
    model = User
    template_name = 'users.html'

    def get_context_data(self, **kwargs):
        context = super(ListUsersView, self).get_context_data(**kwargs)
        context['list_users'] = User.objects.all()
        return context



class ListGroupsView(ListView):
    model = Group
    template_name = 'groups.html'

    def get_context_data(self, **kwargs):
        context = super(ListGroupsView, self).get_context_data(**kwargs)
        context['list_groups'] = Group.objects.all()
        return context


