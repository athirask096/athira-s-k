from django.shortcuts import render
from django.shortcuts import render
from register.models import admin,faculty
from register.models import addstudent,students,facultys,studentattendance
from register.models import leave,stdleave,studentmark
from django.http import HttpResponse

# Create your views here
def authentication(request):
    if request.method=='POST':
        username=request.POST.get('username')  
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username,password=password)
        c=0
        if u.count()==1:
            return render (request,'admin.html')
        else:
            u=faculty.objects.filter(username=username,password=password)
            if u.count()==1:
                return render(request,'factpage.html')
            else:
                u=students.objects.filter(name=username,password=password)
                if u.count()==1:
                    request.session['nm']=username
                    qry=students.objects.all().filter(name=username)[0]
                    request.session['stdid']=qry.stdid
                    return render(request,'studentprof.html')
                else:
                    return HttpResponse('login unsuccessful')    
def addfaculty(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        b=faculty(username=username,password=password)
        b.save()
    return render(request,'addfact.html')   


def addstd(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        c=addstudent(name=name,password=password)
        c.save()
    return render(request,'addstudent.html')       
def signupstd(request): 
    if request.method== 'POST':
        id=request.POST.get('id')
        stdid=request.POST.get('stdid')
        admno=request.POST.get('admno')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        admdate=request.POST.get('admdate')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')
        d=students(id=id,stdid=stdid,admno=admno,name=name,address=address,dob=dob,gender=gender,mobile=mobile,admdate=admdate,guardian=guardian,batch=batch,email=email,password=password)
        d.save()
    return render(request,'stdreg.html')   
def signupfaculty(request): 
    if request.method== 'POST':
         factid=request.POST.get('factid')
         name=request.POST.get('name')
         address=request.POST.get('address')
         dob=request.POST.get('dob')
         gender=request.POST.get('gender')
         qualification=request.POST.get('qualification')
         mobile=request.POST.get('mobile')
         email=request.POST.get('email')
         assignedatch=request.POST.get('assignedatch')
         e=facultys(factid=factid,name=name,address=address,dob=dob,gender=gender,qualification=qualification,mobile=mobile,email=email,assignedatch=assignedatch)
         e.save()
    return render(request,'faculty.html') 
def studentattend(request): 
    if request.method== 'POST':
        date=request.POST.get('date')
        stdid=request.POST.get('stdid')
        name=request.POST.get('name')
        hr1status=request.POST.get('hr1status')
        hr2status=request.POST.get('hr2status')
        hr3status=request.POST.get('hr3status')
        hr4status=request.POST.get('hr4status')
        f=studentattendance(date=date,stdid=stdid,name=name,hr1status=hr1status,hr2status=hr2status,hr3status=hr3status,hr4status=hr4status)
        f.save()
    return render(request,'studattd.html')   
def leaveapply(request): 
    if request.method== 'POST':
        name=request.POST.get('name')
        to=request.POST.get('to')
        leavereason=request.POST.get('leavereason')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        g=leave(name=name,to=to,leavereason=leavereason,from_date=fromdate,to_date=todate)
        g.save()
    return render(request,'leave.html') 
def stdleaveapply(request): 
    if request.method== 'POST':
        name=request.POST.get('name')
        to=request.POST.get('to')
        leavereason=request.POST.get('leavereason')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        h=stdleave(name=name,to=to,leavereason=leavereason,from_date=fromdate,to_date=todate)
        h.save()
    return render(request,'studapplyleave.html') 
def studmark(request):
    if request.method=='POST':
        stdid=request.POST.get('stdid')
        name=request.POST.get('name')
        assessmentno=request.POST.get('assessmentno')
        sub1mark=request.POST.get('sub1mark')
        sub2mark=request.POST.get('sub2mark')
        sub3mark=request.POST.get('sub3mark')
        percentage=request.POST.get('percentage')
        p=studentmark(stdid=stdid,name=name,assessmentno=assessmentno,sub1mark=sub1mark,sub2mark=sub2mark,sub3mark=sub3mark,percentage=percentage)
        p.save()
    return render(request,'studentmark.html') 
def detailsstudent(request):
    queryset=students.objects.all().filter(name=request.session['nm'])
    return render(request,'personaldetails.html',{'authors':queryset})
def markview(request):
    querysett=studentmark.objects.all().filter(stdid=request.session['stdid'])
    return render(request,'viewmark.html',{'authorss':querysett})    
def studview(request):
    querysettttt=students.objects.all().filter()
    return render(request,'viewstudent.html',{'authorsssss':querysettttt})    
def facview(request):
    querysetttt=facultys.objects.all().filter()
    return render(request,'viewfaculty.html',{'authorssss':querysetttt})
def attendview(request):
    querysettt=studentattendance.objects.all().filter(stdid=request.session['stdid'])
    return render(request,'myattend.html',{'authorsss':querysettt})  