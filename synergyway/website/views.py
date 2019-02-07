from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import User, Group
from .forms import NewUserForm, NewGroupForm
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


class CreateUserView(CreateView):
    model = User
    template_name = 'add_user.html'
    form_class = NewUserForm

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

    def get_success_url(self):
        return reverse('users')


class DeleteUserView(DeleteView):
    model = User
    template_name = 'delete_user.html'

    def get_success_url(self):
        return reverse('users')


class EditUserView(UpdateView):
    model = User
    template_name = 'edit_user.html'
    form_class = NewUserForm

    def get_success_url(self):
        return reverse('users')


class ListGroupsView(ListView):
    model = Group
    template_name = 'groups.html'

    def get_context_data(self, **kwargs):
        context = super(ListGroupsView, self).get_context_data(**kwargs)
        context['list_groups'] = Group.objects.all()
        return context


class CreateGroupView(CreateView):
    model = Group
    template_name = 'add_group.html'
    form_class = NewGroupForm

    def get_context_data(self, **kwargs):
        context = super(CreateGroupView, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

    def get_success_url(self):
        return reverse('groups')


class DeleteGroupView(DeleteView):
    model = Group
    template_name = 'delete_group.html'

    def get_success_url(self):
        return reverse('groups')


class EditGroupView(UpdateView):
    model = Group
    template_name = 'edit_group.html'
    form_class = NewGroupForm

    def get_success_url(self):
        return reverse('groups')
