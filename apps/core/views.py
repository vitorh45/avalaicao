#coding: utf-8
from django.shortcuts import render
from django.contrib import messages
from apps.core.forms import UsuarioAvaliacaoForm


def index(request):
    form = UsuarioAvaliacaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message_type = messages.SUCCESS
            message_text = u'Dados enviados com sucesso! Em breve você receberá um email de confirmação.'
        else:
            message_type = messages.ERROR
            message_text = u'Ocorreu um erro ao enviar os dados. Por favor verifique!'

        messages.add_message(request, message_type, message_text)
        form = UsuarioAvaliacaoForm()
    return render(request, 'index.html', {'form': form})
