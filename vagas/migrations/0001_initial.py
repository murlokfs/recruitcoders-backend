# Generated by Django 5.0.8 on 2024-08-21 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(blank=True, max_length=50)),
                ('sobre_mim', models.TextField(blank=True)),
                ('formacao', models.CharField(blank=True, choices=[('ensino_fi', 'Ensino Fundamental Incompleto'), ('ensino_fc', 'Ensino Fundamental Completo'), ('ensino_mi', 'Ensino Médio Incompleto'), ('ensino_mc', 'Ensino Médio Completo'), ('ensino_mti', 'Ensino Médio Técnico Incompleto'), ('ensino_mtc', 'Ensino Médio Técnico Completo'), ('ensino_si', 'Ensino Superior Incompleto'), ('ensino_sc', 'Ensino Superior Completo')], max_length=22)),
                ('habilidades', models.TextField(blank=True)),
                ('atualizado_em', models.DateTimeField(null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('imagem', models.ImageField(blank=True, upload_to='empresas')),
                ('email', models.EmailField(max_length=254)),
                ('tipo', models.CharField(choices=[('startup', 'StartUp'), ('pequenamedia', 'Pequena/Média Empresa'), ('grande', 'Grande Empresa')], default=(), max_length=20)),
                ('colaboradores', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField()),
                ('experiencia', models.CharField(choices=[('junior', 'Júnior'), ('pleno', 'Pleno'), ('senior', 'Sênior')], default=(), max_length=6)),
                ('stack', models.CharField(choices=[('python', 'Python'), ('javascript', 'JavaScript'), ('java', 'Java'), ('csharp', 'C#'), ('cplus', 'C++')], default=(), max_length=10)),
                ('contrato', models.CharField(choices=[('clt', 'CLT'), ('pj', 'PJ'), ('estagio', 'Estágio')], default=(), max_length=7)),
                ('valido_ate', models.DateTimeField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateField(auto_now=True)),
                ('qntd_etapas', models.IntegerField()),
                ('is_ativo', models.BooleanField(default=True)),
                ('qntd_candidaturas', models.IntegerField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vagas.empresa')),
                ('local', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vagas.local')),
            ],
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etapa', models.IntegerField()),
                ('is_ativa', models.BooleanField()),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vagas.vaga')),
            ],
        ),
    ]
