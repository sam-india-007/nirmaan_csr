from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Contact
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Create your views here.
def index (request):
    return render(request, 'main/index.html')

def test_mail (request):
    message = Mail(
    from_email='f20200021@pilani.bits-pilani.ac.in',
    to_emails='samriddha@gmail.com',
    subject='Campus Reopening',
    html_content='<strong>lmao fr?</strong>')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return HttpResponse("Success")
    except Exception as e:
        print(e)
        return HttpResponse("Fail")
    

def table (request):
    contacts = Contact.objects.all()
    return render(request, 'main/table.html', {'contacts' : contacts})

class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['company', 'person', 'email', 'number', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['company', 'person', 'email', 'number', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False