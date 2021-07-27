from django.views.generic import View
from django.shortcuts import render

from .forms import ContactDetailsForm


class ContactView(View):
    http_method_names = ['get', 'post']
    template_name = 'contact.html'

    def get(self, request):
        c_form = ContactDetailsForm()

        context = {'form': c_form}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = ContactDetailsForm(request.POST)

        if form.is_valid():
            u_email = form.cleaned_data['email_id']
            form.save()
            context = {'email': u_email}
            return render(request, 'success.html', context)
        else:
            return render(request, 'failure.html')