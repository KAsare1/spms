from django.contrib import admin
from .models import Student_Choices
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PlacementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'ID_number', 'First_name', 'Last_name', 'Enrolment_Type','email', 'Program_1', 'Program_2','Program_3',"RESULTS","DCIT101",      
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
]
admin.site.register(Student_Choices, PlacementAdmin)