from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Especie(models.Model):
    descricao = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Espécies'

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Especie, self).save()
            self.slug = '%s-%i' % (slugify(self.descricao), self.id)
        super(Especie, self).save(*args, **kwargs)


class Raca(models.Model):
    especie = models.ForeignKey(Especie)
    descricao = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Raças'

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Raca, self).save()
            self.slug = '%s-%i' % (slugify(self.descricao), self.id)
        super(Raca, self).save(*args, **kwargs)


class Pet(models.Model):
    user = models.ForeignKey(User)
    nome = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    especie = models.ForeignKey(Especie)
    raca = models.ForeignKey(Raca)
    foto = models.ImageField(upload_to='img_pets', blank=True)
    STATUS_CHOICES = (
        ('Disponível', 'Disponível'),
        ('Adotado', 'Adotado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Disponível")
    IDADE_CHOICES = (
        ('1 a 3 meses', '1 a 3 meses'),
        ('3 a 6 meses', '3 a 6 meses'),
        ('6 a 9 meses', '6 a 9 meses'),
        ('9 a 12 meses', '9 a 12 meses'),
        ('1 a 3 anos', '1 a 3 anos'),
        ('Acima de 3 anos', 'Acima de 3 anos'),
    )
    idade = models.CharField(max_length=20, choices=IDADE_CHOICES, default="1 a 3 meses")
    GENERO_CHOICES = (
        ('Fêmea', 'Fêmea'),
        ('Macho', 'Macho'),
    )
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, default="Feminino")
    descricao = models.TextField(blank=True, null=True)
    uf_escolhas = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )
    uf = models.CharField(max_length=20, choices=uf_escolhas, default='RO')
    cidade = models.CharField(max_length=150)
    contato = models.CharField(max_length=255, blank=True, null=True)

    @property
    def question_no_answer(self):
        return self.petquestion_set.filter(petanswer__isnull=True)

    @property
    def question_answer(self):
        return self.petquestion_set.filter(petanswer__isnull=False)

    class Meta:
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Pet, self).save()
            self.slug = '%s-%i' % (slugify(self.nome), self.id)
        super(Pet, self).save(*args, **kwargs)


class PetQuestion(models.Model):
    user = models.ForeignKey(User)
    pet = models.ForeignKey('Pet')
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Perguntas'

    @property
    def get_answers(self):
        return self.petanswer_set.all()

    def __str__(self):
        return self.question


class PetAnswer(models.Model):
    user = models.ForeignKey(User)
    pet_question = models.ForeignKey(PetQuestion)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return self.answer


class UserProfile(models.Model):
    usuario = models.OneToOneField(User, unique=True)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    foto = models.ImageField(upload_to='img_user', blank=True, default='static/img/user.png')
    uf_escolhas = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )
    estado = models.CharField(max_length=20, choices=uf_escolhas, default='RO')


class Contato(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comentario = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
