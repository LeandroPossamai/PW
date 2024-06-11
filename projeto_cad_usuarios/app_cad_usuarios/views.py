from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvando os dados da tela para o bd
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibindo todos users cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornando os dados para a pagina de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)
