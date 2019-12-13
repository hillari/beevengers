from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import generic
from .models import Subscription
from .forms import SubscriptionForm


def redirect_view(request):
    return redirect('home/')


class Homepage(generic.TemplateView):
    model = Subscription
    template_name = 'pages/homepage/index.html'

    def get(self, request):
        form = SubscriptionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            subscriber = form.save(commit=False)
            new_email = form.cleaned_data['email']
            if new_email == "":
                # throw error
                form.add_error('email', 'Please enter an email to subscribe.')
            subscriber.email = new_email
            subscriber.save()

            form = SubscriptionForm()
            return render(request, 'pages/homepage/success.html')

        args = {'form': form}
        return render(request, self.template_name, args)














def calendar(request):
    return render(request, 'pages/calendar/calendar.html')


def education(request):
    return render(request, 'pages/education/education.html')

