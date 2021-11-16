from .forms import UserForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
#from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime



class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:users')


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'base/user_list.html'


"""           
  // diese Methode ist dafür da das der admin2 nicht alle Details sieht die admin enthält
"""


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    context_object_firstname = 'user'
    context_object_lastname = 'user'
    template_name = 'base/user.html'


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm  # für bootstrap eingebunden das forms.py
    #fields = ['firstname', 'lastname', 'companyname', 'email']    # alternative ['name','companyname'] / __all__ zeigt alle Felder
    success_url = reverse_lazy('base:users')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserCreate, self).form_valid(form)


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['firstname', 'lastname', 'companyname', 'email']
    success_url = reverse_lazy('base:users')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = User
    context_object_firstname = 'user'
    context_object_lastname = 'user'
    success_url = reverse_lazy('base:users')


class UserLeave(LoginRequiredMixin, ListView):
    model = User
    template_name = 'base/user_leave.html'
    fields = ['lastname', 'companyname']  # alternative ['name','companyname'] / __all__ zeigt alle Felder
    success_url = reverse_lazy('base:users')
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['users'].filter(leave=None).count()
        context['users'] = context['users'].filter(user=self.request.user, leave=None)
        search_input = self.request.GET.get('Suchfeld') or ''
        if search_input:
            context['users'] = context['users'].filter(
                firstname__startswith=search_input)

        context['search_input'] = search_input

        return context


class UserLogout(LoginRequiredMixin, DetailView):
    model = User

    def logout(self, pk):
        queryset = User.objects.filter(id=pk)

        for user in queryset:
            user.leave = datetime.now()
            user.save()

        return redirect('base:user-leave')

"""
 



    def logout(request):
        context = {}
        
        user = request.user
        if request.POST:
            
        
        
     logout = User.objects.filter(firstname=request.user)
        context['logout']









    def get_#
    context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['users'].filter(leave=None).count()
        context['users'] = context['users'].filter(user=self.request.user)
        search_input = self.request.GET.get('Suchfeld') or ''
        if search_input:
            context['users'] = context['users'].filter(
                firstname__startswith=search_input)

        context['search_input'] = search_input

        return context
"""


"""
class UserLogout(DetailView):
    # HTML Datei / Form für die Variablen / URL
    # Wie kommen die Variablen aus dem Form hier her?
    name_template = 'Muster'
    companyname_template = 'Muster'

    # Variablen benutzen um SQL zu filtern
    queryset = User.objects.filter(
        name=name_template,
        companyname=companyname_template,
        leave=None
    )
    # für jeden Besucher im Queryset willst die "leave" sinnvoll füllen

user_list = [user1, user2, user3]

for visitor in user_list:
    leave zeit einfügen
"""