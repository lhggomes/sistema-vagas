import datetime
from django.db.models import Model, CharField, FloatField, TextField, ForeignKey, EmailField, DateField, PROTECT


class PCEmpresa(Model):
    razao_social = CharField(max_length=255, verbose_name="razão social")
    cnpj = CharField(max_length=14)

    def __str__(self):
        return f'{self.razao_social} - {self.cnpj}'


class PCEscolaridade(Model):
    descricao = CharField(max_length=80)

    def __str__(self):
        return f'{self.descricao}'


class PCVaga(Model):
    descricao = CharField(max_length=100, verbose_name="descrição")
    salario = FloatField()
    requisitos = TextField()
    data_criacao = DateField(default=datetime.date.today)

    escolaridade = ForeignKey(PCEscolaridade, on_delete=PROTECT)
    empresa = ForeignKey(PCEmpresa, on_delete=PROTECT)


    def __str__(self):
        return f'{self.descricao} - {self.empresa.razao_social}'


class PCCandidato(Model):
    nome = CharField(max_length=100)
    email = EmailField()

    data_criacao = DateField(default=datetime.date.today)
    def __str__(self):
        return f'{self.nome} - {self.email}'


class PCFaixaSalarial(Model):
    descricao = CharField(max_length=100, verbose_name="descrição")

    def __str__(self):
        return f'{self.descricao}'


class PCCandidatura(Model):
    experiencia = CharField(max_length=255, verbose_name="experiência")
    data_criacao = DateField(default=datetime.date.today)

    pretensao_salarial = ForeignKey(PCFaixaSalarial, on_delete=PROTECT)
    ultima_escolaridade = ForeignKey(PCEscolaridade, on_delete=PROTECT)
    candidato = ForeignKey(PCCandidato, on_delete=PROTECT)
    vaga = ForeignKey(PCVaga, on_delete=PROTECT)

    def __str__(self):
        return f'{self.candidato.nome} - {self.vaga.descricao}'
