from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContatoForm
from .models import Image

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

    # def index(request):

    #     if request.method == 'POST':

    #         subject = request.POST.get('subject')
    #         message = request.POST.get('message')
    #         email = request.POST.get('email')
    #         send_mail(subject, message, settings.EMAIL_HOST_USER,
    #                 [email], fail_silently=False)
    #         return render(request, '/templates/contato.html', {'email': email})

    #     return render(request, '/templates/index.html', {})


    # def contato(request):
    #     if str(request.method) == 'POST':
    #         form = ContatoForm(request.POST)
    #         if form.is_valid():
    #             form.send_mail()
    #             messages.success(request, "Email enviado com sucesso.")
    #             form = ContatoForm()
    #         else:
    #             messages.error(request, "Não foi possível enviar o email.")
    #     else:
    #         form = ContatoForm()
    #     context = {
    #         "form": form
    #     }
    #     return redirect("contato.html", context)