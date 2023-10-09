from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PROGRAM_TYPE =(
    ("Single_Major", "Single Major"),
    ("Major_Minor", "Major-Minor"),
    ("Combined_Major", "Combined Major"),
)

ENROLMENT_TYPE=(
    ("Regular", "Regular"),
    ("Fee paying", "Fee Paying"),
    ("International", "International")
)

GRADES =(
    ("N/A","N/A"),
    ("A","A"),
    ("B+","B+"),
    ("B","B"),
    ("C+","C+"),
    ("C","C"),
    ("D+","D+"),
    ("D","D"),
    ("E","E"),
    ("F","F"),
)

PROGRAMMES =(
    #single major
("Actuarial Science", "Actuarial Science"),
('Applied Geology', "Applied Geology"),
("Applied Geophysics", "Applied Geophysics"),
("Biomathematics", "Biomathematics"),
("Chemistry", "Chemistry"),
("Computer Science", "Computer Science"),
("Geology", "Geology"),
("Geophysics", "Geophysics"),
("Information Technology", "Information Technology"),
("Mathematics", "Mathematics"),
("Physics", "Physics"),
("Statistics", "Statistics"),
#major minor
("Computer Science with Mathematics", "Computer Science with Mathematics"),
("Computer Science with Physics", "Computer Science with Physics"),
("Computer Science with Statistics", "Computer Science with Statistics"),
("Geology with Physics", "Geology with Physics"),
("Geology with Mathematics", "Geology with Mathematics"),
("Mathematics with Computer Science", "Mathematics with Computer Science"),
("Mathematics with Physics", "Mathematics with Physics"),
("Mathematics with Statistics", "Mathematics with Statistics"),
("Mathematics with Geology", "Mathematics with Geology"),
("Physics with Computer Science", "Physics with Computer Science"),
("Physics with Geology", "Physics with Geology"),
("Physics with Mathematics", "Physics with Mathematics"),
("Statistics with Computer Science", "Statistics with Computer Science"),
("Statistics with Mathematics", "Statistics with Mathematics"),
("Physics with Statistics", "Physics with Statistics"),
#combined major
("Chemistry and a Biological Science programme","Chemistry and a Biological Science programme"),
("Chemistry and Physics","Chemistry and Physics"),
("Computer Science and Mathematics","Computer Science and Mathematics"),
("Computer Science and Statistics","Computer Science and Statistics"),
("Computer Science and Physics","Computer Science and Physics"),
("Mathematics and Statistics","Mathematics and Statistics"),
("Physics and Mathematics","Physics and Mathematics"),
("Physics and Statistics","Physics and Statistics")
)


class ProgramType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Program(models.Model):
    programtype = models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
       
    def __str__(self):
        return self.name


class Student_Choices(models.Model):
    ID_number = models.IntegerField() 
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Enrolment_Type = models.CharField(choices=ENROLMENT_TYPE, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.EmailField()
    Program_type_1 = models.CharField(choices=PROGRAM_TYPE, max_length=200)
    Program_type_2 = models.CharField(choices=PROGRAM_TYPE, max_length=200)
    Program_type_3 = models.CharField(choices=PROGRAM_TYPE, max_length=200)
    Program_1 = models.CharField(choices=PROGRAMMES, max_length=200)
    Program_2 = models.CharField(choices=PROGRAMMES, max_length=200)
    Program_3 = models.CharField(choices=PROGRAMMES, max_length=200)
    DCIT101 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    DCIT102 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    DCIT103 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    DCIT104 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    MATH121 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    MATH122 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    MATH123 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    MATH126 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    STAT111 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    STAT112 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    PHYS105 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    PHYS106 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    PHYS143 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    PHYS144 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    ECON101 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    ABCS101 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    BOTN104 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    CHEM113 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    CHEM114 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    CHEM120 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    CHEM122 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    EASC101 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    EASC104 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    EASC106 = models.CharField(max_length=100, choices=GRADES, default='N/A')
    RESULTS = models.FileField( upload_to='')