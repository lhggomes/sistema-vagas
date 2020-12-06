from django.db.models import Model, CharField, FloatField, TextField, ForeignKey, EmailField, PROTECT


class PCEmpresa(Model):
    razao_social = CharField(max_length=255, verbose_name="razão social")
    cnpj = CharField(max_length=14)

    def __str__(self):
        return "{} - {}".format(self.razao_social, self.cnpj)


class PCVaga(Model):
    """
    Vaga Model Class
    """
    descricao = CharField(max_length=100, verbose_name="descrição")
    salario = FloatField()
    requisitos = TextField()
    escolaridade = CharField(max_length=100)
    empresa = ForeignKey(PCEmpresa, on_delete=PROTECT)

    def __str__(self):
        return "{} ({})".format(self.descricao, self.salario)


class PCCandidato(Model):
    nome = CharField(max_length=100)
    email = EmailField()


class PCCandidatura(Model):
    experiencia = CharField(max_length=255, verbose_name="experiência")
    ultima_escolaridade = CharField(max_length=60)
    pretensao_salarial = FloatField(verbose_name="pretensão salarial")

    candidato = ForeignKey(PCCandidato, on_delete=PROTECT)
    vaga = ForeignKey(PCVaga, on_delete=PROTECT)

    def __str__(self):
        return "{}  - {}".format(self.pretensao_salarial, self.ultima_escolaridade)