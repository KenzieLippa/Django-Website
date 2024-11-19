from django.db import models

# Create your models here.

class AccountOwner(models.Model):
    '''can have 0 to many bank accounts'''

    name = models.CharField(max_length=120)
    ssn = models.CharField(max_length=9)

    def __str__(self):
        return self.name
    
    # access list of accounts here
    def get_accounts(self):
        '''generating related objects from the object its related to, create this first and then make the bank accounts'''
        return BankAccount.objects.filter(owner=self)
    
class BankAccount(models.Model):
    '''account number and other information'''
    number = models.IntegerField()
    balance = models.FloatField()
    owner = models.ForeignKey(AccountOwner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} ({self.owner})'
    

#################################################
#course and students

class Course(models.Model):
    number = models.CharField(max_length=12)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.number}: {self.name}'
    

class Student(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    

class Registration(models.Model):
    '''Represents the many to many relationship between students and courses as two one to many
    one course to many students and one student to many courses'''


    # gives more flexibility for creating stsuff this way
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    reg_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2)


    def __str__(self):
        return f'{self.course.number}, {self.student.name}'



################################################
# geneology example

class Person(models.Model):

    name = models.CharField(max_length=120)

    # dont use child because not gaurenteed but mother and father are
    mother = models.ForeignKey('Person', 
                               related_name= 'mother_person',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    father = models.ForeignKey('Person', 
                               related_name= 'father_person',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    # both are allowed to be null
    #first one for db second is for model form

    def __str__(self):
        if self.father and self.mother:
            return f'{self.name}, child of {self.mother.name} and {self.father.name}'
        elif self.father:
            return f'{self.name}, child of {self.father.name}'
        elif self.mother:
            return f'{self.name}, child of {self.mother.name}'
        else:
            return f'{self.name}'


