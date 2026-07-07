from django.http import HttpResponse

def test_view(request):
    return HttpResponse("<h1>Olá, mundo! Esta é uma view de teste.</h1>")

def index_view(request):
    return HttpResponse("<h1>Bem-vindo à página inicial!</h1><p>Agora meu sistema está em desenvolvimento.</p>")
def administracao_view(request):
    return HttpResponse("<h1>Bem-vindo à página de administração!</h1><p>Esta é a área de administração do sistema.</p>")