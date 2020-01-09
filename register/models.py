from django.db import models

# Create your models here.
class admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class faculty(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
class meta:
    db_table:"register_faculty" 

class addstudent(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class meta:
    db_table:"register_addstudent" 

class students(models.Model):
    stdid=models.IntegerField(null=True,blank=True)
    admno=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    dob=models.DateField(max_length=20)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(default=0)
    admdate=models.DateField(max_length=20)
    guardian=models.CharField(max_length=20)
    batch=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class meta:
    db_table:"register_students"     
         
class facultys(models.Model):
    factid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    dob=models.DateField(max_length=20)
    gender=models.CharField(max_length=20)
    qualification=models.CharField(max_length=30)
    mobile=models.IntegerField(default=0)
    email=models.CharField(max_length=20)
    assignedatch=models.CharField(max_length=30)
class meta:
    db_table:"register_faculty" 


class studentattendance(models.Model):
    date=models.DateField(max_length=20)
    stdid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=20)
    hr1status=models.CharField(max_length=10)
    hr2status=models.CharField(max_length=10)
    hr3status=models.CharField(max_length=10)
    hr4status=models.CharField(max_length=10)
class meta:
    db_table:"register_studentattendance"     
class leave(models.Model):
    name=models.CharField(max_length=20)
    to=models.CharField(max_length=10)
    leavereason=models.CharField(max_length=20)
    from_date=models.DateField(max_length=20)
    to_date=models.DateField(max_length=20)
class meta:
    db_table:"register_leave"    
    
class stdleave(models.Model):
    name=models.CharField(max_length=20)
    to=models.CharField(max_length=10)
    leavereason=models.CharField(max_length=20)
    from_date=models.DateField(max_length=20)
    to_date=models.DateField(max_length=20)
class meta:
    db_table:"register_stdleave" 
class studentmark(models.Model):
      stdid=models.IntegerField(null=True,blank=True)
      name=models.CharField(max_length=20)
      assessmentno=models.IntegerField(null=True,blank=True)
      sub1mark=models.IntegerField(null=True,blank=True)
      sub2mark=models.IntegerField(null=True,blank=True)
      sub3mark=models.IntegerField(null=True,blank=True)
      percentage=models.IntegerField(null=True,blank=True) 
class meta:
    db_table:"register_studentmark"       
