import csv
from django.core.management.base import BaseCommand
from associados.models import Associado


class Command(BaseCommand):
    help = 'Exporta clientes para Power BI'

    def handle(self, *args, **kwargs):
        with open('clientes_powerbi.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nome', 'cpf', 'email', 'telefone'])

            for c in Associado.objects.all():
                writer.writerow([
                    c.id,
                    c.nome,
                    c.cpf,
                    c.email,
                    c.telefone
                ])

        self.stdout.write(self.style.SUCCESS('Arquivo clientes_powerbi.csv gerado com sucesso!'))
