# coding=utf-8
import random
from models import *
import datetime
from django.contrib import auth

class Subjects:
    urk=0
    math=1
    hist=2
    geog=3
    phis=4
    chem=5
    bio=6
    eng=7
    fr=8
    de=9

class AbitRequestHelper:
    def __init__(self):
        self.male_surnames = [s[:-1] for s in open('surnames.txt','r').readlines()]
        self.female_surnames = [s+'а' for s in self.male_surnames]
        self.male_names = [s[:-1] for s in open('names_male.txt','r').readlines()]
        self.female_names = [s[:-1] for s in open('names_male.txt','r').readlines()]
        self.male_fathers = [s[:-1] for s in open('middle_names_male.txt','r').readlines()]
        self.female_fathers = [s[:-1] for s in open('middle_names_female.txt','r').readlines()]

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
        return random.uniform(124,200)

    def getFather(self, sex):
        if sex=='male':
            return random.choice(self.male_fathers)
        return random.choice(self.female_fathers)


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
    
    def addSpeciality(self, sname, scode, *args):
        s = Speciality(name=sname, code=scode)
        s.subject1 = self.getSubj(u'Українська мова та література')
        s.subject2 = self.getSubj(args[0])
        s.save()
        for subj in args[1:]:
            s.subject3.add(self.getSubj(subj))
        s.save()        

    def addSpecialities(self):
        Speciality.objects.all().delete()
        
        self.addSpeciality(u'Економіка підприємства', u'6.030504',
                            u'Математика',
                            u'Історія України',
                            u'Географія'
                            )
        self.addSpeciality(u'Інформатика', u'6.040302',
                            u'Математика',
                            u'Фізика',
                            u'Англійська мова',
                            u'Французька мова',
                            u'Німецька мова'
                            )
        self.addSpeciality(u'Машинобудування', u'6.050503',
                            u'Математика',
                            u'Хімія',
                            u'Фізика'
                            )
        self.addSpeciality(u'Екологія, охорона навколишнього середовища та збалансоване природокористування', u'6.040106',
                            u'Математика',
                            u'Хімія',
                            u'Географія',
                            )
        self.addSpeciality(u'Хімічна технологія', u'6.051301',
                            u'Хімія',
                            u'Математика',
                            u'Фізика'
                            )
        self.addSpeciality(u'Фармація', u'7.120201',
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
        ab.surname = h.getSurname(sex)
        ab.name = h.getName(sex)
        ab.father = h.getFather(sex)
        ab.birth_date = h.getDate(1960,1994)
        ab.passport_date = datetime.date(ab.birth_date.year+16,ab.birth_date.month,ab.birth_date.day)
        ab.att_date = datetime.date(ab.birth_date.year+18,ab.birth_date.month,ab.birth_date.day)
        ab.att_srbal = h.getBall()
        ab.speciality = random.choice(Speciality.objects.all())
        ab.edform = random.choice(EducationalForm.objects.all())
        ab.test1_subject = self.getSubj(ab.speciality.subject1)
        ab.test1_value = h.getBall()
        ab.test2_subject = self.getSubj(ab.speciality.subject2)
        ab.test2_value = h.getBall()
        ab.test3_subject = self.getSubj(ab.speciality.subject3.all()[0])
        ab.test3_value = h.getBall()
        ab.creator = auth.get_user(request)
        ab.save()
        
    def generateAbitRequests(self,request):
        AbitRequest.objects.all().delete()
        for i in range(1,50):
            self.addAbitRequest(request)
        
#def __main__(**args):
#    g = Generator()
#    g.generate()