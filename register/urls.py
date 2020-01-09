from django.urls import path
from register import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/', TemplateView.as_view(template_name='admin.html'),name='admin'),
    # path('addfact/', TemplateView.as_view(template_name='addfact.html'),name='addfact'),
     path('faculty/', TemplateView.as_view(template_name='faculty.html'),name='faculty'),
     #cd path('add_student', TemplateView.as_view(template_name='addstudent.html'),name='addstudent'),
    path('index',views.authentication,name='submit'),
    path('addfact/',views.addfaculty,name='addfact'),
    path('addstudent/',views.addstd,name='addstudent'),
    path('studentsignup/',views.signupstd,name='student registration'),
    path('facultysignup/',views.signupfaculty,name='faculty registration'),
    path('studentreg/', TemplateView.as_view(template_name='stdreg.html'),name='stdreg'),
    path('studetat/', TemplateView.as_view(template_name='studattd.html'),name='studattd'),
    path('studattd/',views.studentattend,name='stdatt'),
    path('leave_apply', TemplateView.as_view(template_name='leave.html'),name='leave'),
    path('leave/',views.leaveapply,name='leaves'),
    path('sleave_apply', TemplateView.as_view(template_name='studapplyleave.html'),name='studapplyleave'),
    path('studapplyleave/',views.stdleaveapply,name='studapplyleave'),
    path('stdmrk', TemplateView.as_view(template_name='studentmark.html'),name='studentmark'),
    path('stdmark/',views.studmark,name='studentmark'),
    path('mydetails/',TemplateView.as_view(template_name='personaldetails.html'),name='personaldetails'),
    path('details/',views.detailsstudent,name='personaldetails'),
    path('mymarks/',TemplateView.as_view(template_name='viewmark.html'),name='viewmark'),
    path('markdetails/',views.markview,name='viewmark'),
    path('emailedit/',TemplateView.as_view(template_name='email.html'),name='email'),
    path('passwordedit/',TemplateView.as_view(template_name='password.html'),name='password'),
    path('mobiledit/',TemplateView.as_view(template_name='mobile.html'),name='mobile'),
    path('mystud/',TemplateView.as_view(template_name='viewstudent.html'),name='viewstudent'),
    path('studentdetails/',views.studview,name='viewstud'),
    path('myfac/',TemplateView.as_view(template_name='viewfaculty.html'),name='viewfaculty'),
    path('facdetails/',views.facview,name='view'),
    path('myattendence/',TemplateView.as_view(template_name='myattend.html'),name='myattend'),
    path('attendencedetails/',views.attendview,name='myattend'),
    path('log/',TemplateView.as_view(template_name='logout.html'),name='logout'),
    


    

    
    




    

]