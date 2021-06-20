from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from cryptography.fernet import Fernet
from .models import Book, UserDetails
from .models import Contact
from .models import Book
from .models import Report
from .models import Diagnostic
from datetime import datetime



# Function work upon login process.
def homePage(request):

    if(request.method == 'POST'):
        #if("login" in request.POST):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            object = UserDetails.objects.get(email = email)
            key1 = object.key
            key1=key1[2:-1]
            key1 = bytes(key1,'utf-8')
            f = Fernet(key1)
            truepassword = object.password 
            truepassword = truepassword[2:-1]
            truepassword = bytes(truepassword,'utf-8')
            truepassword = f.decrypt(truepassword).decode('utf-8')        
        except:
            object = None
        
        if(object==None):
            context = {
                'message': "Email Does Not Exist"
            }
            return render(request,"login.html",context)

        elif(password == truepassword):
            if object.profession == "PATIENT":
                object1=UserDetails.objects.filter(profession="DOCTOR")
                # name=(object.name)
                # appointment(request,email,name)
                context1={
                    'message':'Welcome '+object.name,
                    'mail' : object.email,
                    'doctors':object1

                }
                return render(request,"index.html",context1)
                
            else:
                context2={
                    'message':'Welcome '+object.name,
                    'mail' : object.email
                }
                return render(request,"dindex.html",context2)
            
        else:
            return redirect("/")

    else:
        return render(request,"login.html",{})


# Function work upon signup process.
def signUpPage(request):

    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordVerif = request.POST.get('passwordVerif')
        profession = request.POST.get('user')
        data = request.POST.get('data')

        if(email ==''):
            context = {
                'message': "Please enter Email ID"
            }
            return render(request,"signup.html",context)

        elif(password == passwordVerif):
            key = Fernet.generate_key()
            f = Fernet(key)
            password = bytes(password,'utf-8')
            token = f.encrypt(password)
            key = str(key)
            print(key)
            UserDetails.objects.create(email=email, name=name , password=token, key = key, profession=profession, data=data)
            return redirect("/")
        
        else:
            context = {
                'message': "Password doesn't match"
            }
            return render(request,"signup.html",context)

    else:
        return render(request,"signup.html",{})


# Functions work upon calling about page.
def about(request):
    return render(request, 'about.html')
# Functions work upon calling services page.
def services(request):
    return render(request, 'services.html')
# Functions work upon calling contact page.
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        contact = Contact(email=email , name=name, phone=phone,address=address,date=datetime.today())
        contact.save()
    return render(request,"contact.html")

# Functions work upon calling book appointment page.
def book(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        book = Book(email=email , name=name, phone=phone,problem=address,date=datetime.today())
        book.save()
    return render(request,"book.html")

# Functions work upon calling report page.
def report(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        report = Report(email=email , name=name, phone=phone, message=message, date=datetime.today())
        report.save()
    return render(request,"report.html")

# Functions work upon calling diagnostic booking page.
def diag(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        tests = request.POST.get('drop1')
        tests = str(tests)
        if(email ==''):
            context = {
                'message': "Please enter Email ID"
            }
            return render(request,"diag.html",context)
        else:
            diag = Diagnostic(email=email , name=name, phone=phone, tests=tests, date=datetime.today())
            diag.save()
    return render(request,"diag.html")


# def appointment(request,email,name):
#     if request.method == "POST":
#         problem = request.POST.get('problem')
#         book = Appoint(problem=problem, email=email, name=name)
#         book.save()
#     return render(request,"index.html")