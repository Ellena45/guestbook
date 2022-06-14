from .forms import UserForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import User
from django.views.generic.edit import CreateView, UpdateView, \
    DeleteView  # python genercis sind python eigen /Klassenbasierte Ansichten richten automatisch alles von A bis Z ein.
# Es muss nur angeben werden, für welches Modell DetailView erstellt werden soll, dann versucht dasklassenbasierte DetailView automatisch diese zuerstellen
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import csv
from django.http import HttpResponse




class CustomLoginView(LoginView):  # Admin Login welches auf die html Vorlage login zugeordnet wird
    template_name = 'guests/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):  #
        return reverse_lazy('guests:users')


class UserList(LoginRequiredMixin, ListView):  # lstet die User liste aus meiner DB auf
    model = User
    template_name = 'guests/start_page.html'


"""           
  // diese Methode ist dafür da das der admin2 nicht alle Details sieht die admin enthält
"""


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    context_object_firstname = 'user'
    context_object_lastname = 'user'
    template_name = 'guests/user.html'


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm  # für bootstrap eingebunden das forms.py
    # fields = ['firstname', 'lastname', 'companyname', 'email']    # alternative ['name','companyname'] / __all__ zeigt alle Felder
    success_url = reverse_lazy('guests:users')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserCreate, self).form_valid(form)


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['firstname', 'lastname', 'companyname', 'email']
    success_url = reverse_lazy('guests:users')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = User
    context_object_firstname = 'user'
    context_object_lastname = 'user'
    success_url = reverse_lazy('guests:users')


class UserLeave(LoginRequiredMixin, ListView):
    model = User
    template_name = 'guests/user_details.html'
    fields = ['lastname', 'companyname']  # alternative ['name','companyname'] / __all__ zeigt alle Felder
    success_url = reverse_lazy('guests:users')
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

        return redirect('guests:user-leave')


class Impressum(LoginRequiredMixin, ListView):
    model = User
    template_name = 'guests/user_impressum.html'



def csv_database_write(request):

    # entnimmt alle Daten aus dem Model User
    users = User.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name'])

    for user in users:
        writer.writerow([user.first_name, user.last_name])

    return response



"""
 class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model.meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Select"


response = HttpResponse(content_type='text/csv')
    
        writer = csv.writer(response)
        writer.writerow(['firstname', 'lastname'])
        for user in User.objects.all().values_list('firstname','lastname'):
            writer.writerow(user)
        response['Content-Disposition'] = 'attachment; filename="user.csv.format"'
    
        return response
        
        

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
