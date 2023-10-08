from django import forms
from .models import Student_Choices

class MyForm(forms.ModelForm):
  class Meta:
    model = Student_Choices
    
    fields = {'ID_number',    
              "First_name",
              "Last_name",   
              "email",        
              "Program_type_1",
              "Program_type_2",
              "Program_type_3",
              'Program_1',
              'Program_2',
              'Program_3',
              "DCIT101",      
              "DCIT102",      
              "DCIT103",      
              "DCIT104",      
              "MATH121",      
              "MATH122",      
              "MATH123",      
              "MATH126",      
              "STAT111",      
              "STAT112",      
              "PHYS105",      
              "PHYS106",      
              "PHYS143",      
              "PHYS144",      
              "ECON101",      
              "ABCS101",      
              "BOTN104",      
              "CHEM113",      
              "CHEM114",      
              "CHEM120",      
              "CHEM122",      
              "EASC101",      
              "EASC104",      
              "EASC106",      
              "RESULTS",
                }
    