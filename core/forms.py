from django import forms
from django.core.mail.message import EmailMessage
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

<<<<<<< HEAD
        conteudo = f'Nome: {nome}\nE-mail: {email}\nTelefone: {assunto}\nMensagem: {mensagem}'
=======
        conteudo = f'Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}'
>>>>>>> 1a31cf2b8d53f8aa4edf170a65a09b4b6e233f1d

        mail = EmailMessage(
            subject=nome,
            body=conteudo,
            from_email=email,
            to=['aquinoreginaldo@hotmail.com',],
            headers={'Reply-To': email}
        )
        mail.send()

