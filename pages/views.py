from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, TemplateView

from pages import forms
from pages.forms import ContactForm
from pages.models import AboutModel


def home_page_view(request):
    return render(request, 'home.html')


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    # success_url = reverse_lazy('pages:contact')

    def get_success_url(self):
        return reverse_lazy('pages:contact')

    def form_valid(self, form):
        messages.success(self.request, _('Your contact information is sent'))
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors:
            messages.error(self.request, error)
        return super().form_invalid(form)


class AboutPageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['posts'] = AboutModel.objects.all()
        return context

    template_name = 'pages/about-us.html'


def contact_page_view(request):
    if request.method == "POST":

        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message save database')
            return redirect('pages:contact')

        else:
            messages.error(request, 'Error')
            return redirect('pages:contact')

    else:
        return render(request, 'pages/contact.html')