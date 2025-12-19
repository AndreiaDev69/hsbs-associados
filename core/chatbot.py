from associados.models import Associado
from estoque.models import Produto

def chatbot_response(message):
    msg = message.lower()

    if "quantos associados" in msg:
        return f"Existem {Associado.objects.count()} associados cadastrados."

    if "listar associados" in msg:
        associados = Associado.objects.all()[:5]
        nomes = ", ".join(a.nome for a in associados)
        return f"Alguns associados: {nomes}"

    if "quantos produtos" in msg:
        return f"Existem {Produto.objects.count()} produtos no estoque."

    if "estoque baixo" in msg:
        produtos = Produto.objects.filter(quantidade__lte=5)
        if not produtos:
            return "Nenhum produto com estoque baixo."
        nomes = ", ".join(p.nome for p in produtos)
        return f"Produtos com estoque baixo: {nomes}"

    return "Não entendi. Pergunte sobre associados ou estoque."
