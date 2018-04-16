from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=60, null=True)


    def __str__(self):
        return (self.nome)

class Evento (models.Model):
    nome = models.CharField(max_length=150, null=True)
    eventoPrincipal = models.CharField(max_length=30,null=True)
    sigla = models.CharField(max_length=10,null=True)
    dataEHoraDeInicio = models.DateTimeField(blank=False, null=True)
    logoTipo = models.CharField(max_length=200,null=True)
    realisador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    cidade = models.CharField(max_length=30,null=True)
    uf= models.CharField(max_length=2,null=True)
    cep = models.CharField(max_length=8,null=True)

    def __str__(self):
        return (self.nome)
        

class EventoCientifico(Evento):
    issn=models.CharField(max_length=30, null=True )

    def __str__(self):
        return ( self.issn)

class Autor (Pessoa):
    curriculo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return (self.curriculo)


class PessoasJuridica(Pessoa):
    cnpj = models.CharField(max_length=12, null=True)
    razaoSocial = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return (self.razaoSocial)

class PessoaFisica(Pessoa):
    cpf= models.CharField(max_length=11,null=True)

    def __str__(self):
        return (self.cpf )

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=30, null=True)
    autores = models.ManyToManyField(Autor, null=True)
    evento = models.ForeignKey(EventoCientifico, on_delete=models.CASCADE, related_name='eventoCientifico', null=True)

    def __str__(self):
        return (self.titulo)


class Avaliador (PessoaFisica):
    formacao=models.CharField('formacao', max_length=50,null=True)

    def __str__(self):
        return (self.formacao)

class Avaliacao (models.Model):
    qualitecnica=models.IntegerField()
    inovacao=models.IntegerField()
    resultados=models.IntegerField()
    metodologia=models.IntegerField()
    adequacaoTematica=models.IntegerField()
    avaliador=models.ForeignKey(Avaliador, null = True,blank = False,on_delete = models.CASCADE )
    artigoAvaliacao = models.ManyToManyField(ArtigoCientifico)
    media=models.CharField(max_length=30,null=True)

    def __str__(self):
        return (self.media)

