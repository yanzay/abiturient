# coding=utf-8
import random
from models import *
import datetime
from django.contrib import auth
from decimal import Decimal

class AbitRequestHelper:
    def __init__(self):
        self.male_surnames = [s[:-1] for s in open('surnames.txt','r').readlines()]
        self.female_surnames = [s+'а' for s in self.male_surnames]
        self.male_names = [s[:-1] for s in open('names_male.txt','r').readlines()]
        self.female_names = [s[:-1] for s in open('names_female.txt','r').readlines()]
        self.male_fathers = [s[:-1] for s in open('middle_names_male.txt','r').readlines()]
        self.female_fathers = [s[:-1] for s in open('middle_names_female.txt','r').readlines()]
        self.sities = [s[:-1] for s in open('cities.txt').readlines()]

    def getSurname(self, sex):
        if sex=='male':
            return random.choice(self.male_surnames)
        return random.choice(self.female_surnames)

    def getName(self, sex):
        if sex=='male':
            return random.choice(self.male_names)
        return random.choice(self.female_names)

    def getDate(self, year1, year2):
        year=random.randint(year1,year2)
        month=random.randint(1,12)
        day=random.randint(1,28)
        return datetime.date(year,month,day)

    def getBall(self):
        return Decimal(str(random.uniform(124,200)))

    def getFather(self, sex):
        if sex=='male':
            return random.choice(self.male_fathers)
        return random.choice(self.female_fathers)

    def getCity(self):
        r = random.randint(1,10)
        if r > 6:
            return random.choice(self.sities)
        else:
            return self.sities[10]

class Generator:
    def addTestSubject(self, sname):
        TestSubject.objects.create(name=sname)
    
    def addTestSubjects(self):
        TestSubject.objects.all().delete()
        self.addTestSubject(u'Українська мова та література')
        self.addTestSubject(u'Математика')
        self.addTestSubject(u'Історія України')
        self.addTestSubject(u'Географія')
        self.addTestSubject(u'Фізика')
        self.addTestSubject(u'Хімія')
        self.addTestSubject(u'Біологія')
        self.addTestSubject(u'Англійська мова')
        self.addTestSubject(u'Французька мова')
        self.addTestSubject(u'Німецька мова')
    
    def getSubj(self, sname):
        return TestSubject.objects.get(name=sname)
    
    def addSpeciality(self, sname, short_name, scode, *args):
        s = Speciality(name=sname, code=scode)
        s.subject1 = self.getSubj(u'Українська мова та література')
        s.subject2 = self.getSubj(args[0])
        s.short_name = short_name
        s.save()
        for subj in args[1:]:
            s.subject3.add(self.getSubj(subj))
        s.save()        

    def addSpecialities(self):
        Speciality.objects.all().delete()
        
        self.addSpeciality(u'Економіка підприємства', u'еп', u'6.030504',
                            u'Математика',
                            u'Історія України',
                            u'Географія'
                            )
        self.addSpeciality(u'Інформатика', u'ін', u'6.040302',
                            u'Математика',
                            u'Фізика',
                            u'Англійська мова',
                            u'Французька мова',
                            u'Німецька мова'
                            )
        self.addSpeciality(u'Машинобудування', u'оп', u'6.050503',
                            u'Математика',
                            u'Хімія',
                            u'Фізика'
                            )
        self.addSpeciality(u'Екологія, охорона навколишнього середовища та збалансоване природокористування', u'ео', u'6.040106',
                            u'Математика',
                            u'Хімія',
                            u'Географія',
                            )
        self.addSpeciality(u'Хімічна технологія', u'ор', u'6.051301',
                            u'Хімія',
                            u'Математика',
                            u'Фізика'
                            )
        self.addSpeciality(u'Фармація', u'фп', u'7.120201',
                            u'Хімія',
                            u'Фізика',
                            u'Біологія'
                            )

    def addEducationalForm(self, edname):
        EducationalForm.objects.create(name=edname)
    
    def addEducationalForms(self):
        EducationalForm.objects.all().delete()
        self.addEducationalForm(u'Денна')
        self.addEducationalForm(u'Заочна')
    
    def generateBase(self):
        self.addTestSubjects()
        self.addSpecialities()
        self.addEducationalForms()
        
    def addAbitRequest(self,request):
        ab = AbitRequest()
        h = AbitRequestHelper()
        sex_opt = ['male','female']
        sex = random.choice(sex_opt)
        if sex == 'male':
            ab.sex = 'М'
        else:
            ab.sex = 'Ж'
        ab.surname = h.getSurname(sex)
        ab.name = h.getName(sex)
        ab.father = h.getFather(sex)
        ab.birth_date = h.getDate(1960,1994)
        ab.passport_ser = random.choice([u'ЕН',u'ЕК'])
        ab.passport_num = random.randint(111111,999999)
        ab.passport_date = datetime.date(ab.birth_date.year+16,ab.birth_date.month,ab.birth_date.day)
        ab.passport_org = u'Рубіжанським МВ УМВС України'
        ab.id_number = random.randint(1000000000,2599999999)
        ab.city = h.getCity()
        ab.address = u'ул. %s, д. %s, кв. %s' % (
            random.choice([u'Мира',u'Менделеева',u'Ленина',u'Пушкина']),
            random.randint(1,99),
            random.randint(1,200)
            )
        ab.phone = u'+38050%07d' % (random.randint(1,9999999))
        ab.att_school = u'ЗОШ №%s' % (random.randint(1,30))
        ab.att_date = datetime.date(ab.birth_date.year+18,ab.birth_date.month,ab.birth_date.day)
        ab.att_srbal = h.getBall()
        ab.speciality = random.choice(Speciality.objects.all())
        ab.edform = random.choice(EducationalForm.objects.all())
        ab.test1_subject = self.getSubj(ab.speciality.subject1)
        ab.test1_cert_num = random.randint(11111,99999)
        ab.test1_cert_pin = u'%04d' % random.randint(1,9999)
        ab.test1_cert_year = random.randint(2008,2012)
        ab.test1_value = h.getBall()
        ab.test2_subject = self.getSubj(ab.speciality.subject2)
        ab.test2_cert_num = ab.test1_cert_num
        ab.test2_cert_pin = ab.test1_cert_pin
        ab.test2_cert_year = ab.test1_cert_year
        ab.test2_value = h.getBall()
        ab.test3_subject = self.getSubj(ab.speciality.subject3.all()[0])
        ab.test3_cert_num = ab.test1_cert_num
        ab.test3_cert_pin = ab.test1_cert_pin
        ab.test3_cert_year = ab.test1_cert_year
        ab.test3_value = h.getBall()
        ab.creator = auth.get_user(request)
        ab.code = ab.speciality.short_name + ab.edform.name[0].lower() + '%03d' % random.randint(1,200)
        ab.save()
        
    def generateAbitRequests(self,request):
        AbitRequest.objects.all().delete()
        for i in range(1,354):
            self.addAbitRequest(request)
        
#def __main__(**args):
#    g = Generator()
#    g.generate()