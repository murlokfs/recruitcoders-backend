from datetime import datetime

from celery import shared_task

from .models import Vaga


@shared_task
def atualizar_vagas_expiradas():
    hoje = datetime.now().date()

    vagas_expiradas = Vaga.objects.filter(valido_ate__lte=hoje, is_ativo=True)
    total_vagas_expiradas = vagas_expiradas.count()

    # para cada vaga que excedeu o tempo de validade, é definido o campo is_ativo como false
    for vaga in vagas_expiradas:
        vaga.is_ativo = False
        vaga.save()

    total_vagas_analisadas = Vaga.objects.filter(valido_ate__lte=hoje).count()

    return f"Vagas fechadas: {total_vagas_expiradas} \n Vagas analisadas: {total_vagas_analisadas}"


@shared_task
def teste_task():
    print("Tarefa teste executada")
    return "Sucesso"
