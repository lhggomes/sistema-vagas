from django.db.models import Model, CharField, FloatField, TextField, ForeignKey


class Vaga(Model):
    """
    Vaga Model Class
    """
    descricao = CharField(max_length=100, verbose_name="descrição")
    salario = FloatField()
    requisitos = TextField()
    escolaridade = CharField()

    def __str__(self):
        return "{} ({})".format(self.descricao, self.salario)


class Empresa(Model):
    razao_social = CharField(max_length=255, verbose_name="razão social")
    cnpj = CharField(max_length=14)

    def __str__(self):
        return "{} - {}".format(self.razao_social, self.cnpj)


class Candidato(Model):
    nome = CharField(max_length=100)
    email = CharField(max_length=200)


class Candidatura(Model):
    candidato = CharField(max_length=100)
    vaga = CharField(max_length=50)
    experiencia = CharField(max_length=255, verbose_name="experiência")
    ultima_escolaridade = CharField(max_length=60)
    pretensao_salarial = FloatField(verbose_name="pretensão salarial")

    def __str__(self):
        return "{} - {}  - {}".format(self.candidato, self.pretensao_salarial, self.ultima_escolaridade)