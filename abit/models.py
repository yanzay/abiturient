from django.db.models import *

class Abiturient(Model):
	surname = CharField(u'Фамилия', max_length=50)
	name = CharField(u'Имя', max_length=50)
	father = CharField(u'Отчество', max_length=50)
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
	att_srbal = FloatField(u'Средний балл аттестата')
	
	def __unicode__(self):
		return u"%s %s %s" % (self.surname, self.name, self.father)
	
#class AbiturientAdmin(admin.ModelAdmin):
#	list_display = ('surname', 'name', 'father')
	
class AbitRequest(Model):
	code = CharField(u'Шифр заявки', max_length=7)
	speciality = ForeignKey('Speciality')
	abiturient = ForeignKey(Abiturient, related_name='requests')
	testresults = ManyToManyField('TestResult')
	edform = ForeignKey('EducationalForm')
	
	def __unicode__(self):
		return u"%s %s" % (self.code, self.abiturient)
		
class EducationalForm(Model):
	name = CharField(u'Название', max_length=20)
	
	def __unicode__(self):
		return self.name
	
class Speciality(Model):
	code = CharField(u'Шифр специальности', max_length=15)
	name = CharField(u'Название', max_length=50)
	subjects = ManyToManyField('TestSubject')
	
	def __unicode__(self):
		return u"%s %s" % (self.code, self.name)
	
class TestSubject(Model):
	name = CharField(max_length=30)
	
	def __unicode__(self):
		return self.name
	
class TestResult(Model):
	abit = ForeignKey(Abiturient)
	subject = ForeignKey(TestSubject)
	cert_num = CharField(u'Номер сертификата', max_length=15)
	cert_pin = CharField(u'Пин-код сертификата', max_length=4)
	cert_year = CharField(u'Год получения сертификата', max_length=4)
	value = FloatField(u'Балл')
	
	def __unicode__(self):
		return u"%s %s %s" % (self.request, self.subject, self.value)

