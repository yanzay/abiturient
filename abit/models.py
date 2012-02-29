# coding=utf-8
from django.db.models import Model
from django.db.models.fields import CharField, DateField, FloatField, DecimalField, BooleanField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

#pre_save.connect(calc_sr_bal)

#def calc_sr_bal(sender,instance):
#    pass

class AbitRequest(Model):
    #Личные данные
    SEX_CHOICES = ((u'М',u'Мужской'),(u'Ж',u'Женский'))
    surname = CharField(u'Фамилия', max_length=50)
    name = CharField(u'Имя', max_length=50)
    father = CharField(u'Отчество', max_length=50)
    sex = CharField(u'Пол', max_length=1, choices=SEX_CHOICES)
    birth_date = DateField(u'Дата рождения')
    passport_ser = CharField(u'Серия паспорта', max_length=5)
    passport_num = CharField(u'Номер паспорта', max_length=10)
    passport_date = DateField(u'Дата выдачи')
    passport_org = CharField(u'Кем выдан', max_length=150)
    id_number = CharField(u'Идентификационный код', max_length=15)
    city = CharField(u'Город', max_length=20)
    address = CharField(u'Адрес', max_length=100)
    phone = CharField(u'Телефон', max_length=15)
    att_school = CharField(u'Учебное заведение', max_length=25)
    att_date = DateField(u'Дата выдачи аттестата')
    att_srbal = DecimalField(u'Средний балл аттестата', max_digits=4, decimal_places=1)

    #Льготы
    privilege = BooleanField(u'Льготы',default=False)
    privilege_category = CharField(u'Льготная категория',max_length=100)

    #Данные заявки
    code = CharField(u'Шифр заявки', max_length=7)
    speciality = ForeignKey('Speciality', verbose_name=u'Специальность')
    edform = ForeignKey('EducationalForm',verbose_name=u'Форма обучения')

    test1_subject = ForeignKey('TestSubject',related_name="+",verbose_name=u'Первый предмет')
    test1_cert_num = CharField(u'Номер сертификата', max_length=15)
    test1_cert_pin = CharField(u'Пин-код сертификата', max_length=4)
    test1_cert_year = CharField(u'Год получения сертификата', max_length=4)
    test1_value = DecimalField(u'Балл', max_digits=4, decimal_places=1)

    test2_subject = ForeignKey('TestSubject',related_name="+",verbose_name=u'Второй предмет')
    test2_cert_num = CharField(u'Номер сертификата', max_length=15)
    test2_cert_pin = CharField(u'Пин-код сертификата', max_length=4)
    test2_cert_year = CharField(u'Год получения сертификата', max_length=4)
    test2_value = DecimalField(u'Балл', max_digits=4, decimal_places=1)

    test3_subject = ForeignKey('TestSubject',related_name="+", verbose_name=u'Третий предмет')
    test3_cert_num = CharField(u'Номер сертификата', max_length=15)
    test3_cert_pin = CharField(u'Пин-код сертификата', max_length=4)
    test3_cert_year = CharField(u'Год получения сертификата', max_length=4)
    test3_value = DecimalField(u'Балл', max_digits=4, decimal_places=1)

    date = DateField(auto_now_add=True)
    creator = ForeignKey(User)

    @property
    def sum_bal(self):
        return self.att_srbal + self.test1_value + self.test2_value + self.test3_value

    def __unicode__(self):
        return u"%s %s %s" % (self.surname, self.name, self.father)

#class AbiturientAdmin(admin.ModelAdmin):
#   list_display = ('surname', 'name', 'father')

class EducationalForm(Model):
    name = CharField(u'Название', max_length=20)

    def __unicode__(self):
        return self.name

class Speciality(Model):
    code = CharField(u'Шифр специальности', max_length=15)
    name = CharField(u'Название', max_length=50)
    short_name = CharField(u'Короткое название', max_length=5)
    budget = IntegerField(u'Количество бюджетных мест')
    subject1 = ForeignKey('TestSubject',related_name="+")
    subject2 = ForeignKey('TestSubject',related_name="+")
    subject3 = ManyToManyField('TestSubject',related_name="+")

    def __unicode__(self):
        return self.name

class TestSubject(Model):
    name = CharField(max_length=30)

    def __unicode__(self):
        return self.name