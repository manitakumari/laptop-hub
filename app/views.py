# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from app.models import UserProfile,New_Product

class IndexView(TemplateView):
    template_name = "index.html"
    def posts(self):
        posts = New_Product.objects.all()
        return posts[::-1]


class NewItemsView(TemplateView):
    template_name = "newItems.html"

    def post(self, request, *args, **kwargs):
        #model = request.POST.get('model')
        
        p_img = request.POST.get(request.FILES['p_img'])
        p_name = request.POST.get('p_name')
        p_price = request.POST.get('p_price')
        p_desc = request.POST.get('p_desc')
        p_rating = request.POST.get('p_rating')
        
        src = request.FILES['p_img']
        file_path= f'static/img/{p_name}.jpg'.replace(' ', '_').lower()
        # file_path= f'static/img/profiles/{p_name}.png'.replace(' ', '_').lower()
        with open('app/'+file_path, 'wb+') as fh:
            for chunk in src.chunks():
                fh.write(chunk)
        
        value = New_Product(
                p_img = file_path,
                p_name = p_name,
                p_price = p_price,
                p_desc = p_desc,
                p_rating = p_rating
            )
        value.save()                       
        messages.success(request,'Product added successfully')             
        return HttpResponseRedirect('/filetest')

class ProductDetailsView(TemplateView):
    template_name = "product_details.html"
    def display(self):
        # display = New_Product.objects.filter(p_name=p_name).values_list('id', flat=True)
        display = New_Product.objects.all()
        return display

class PaymentView(TemplateView):
    template_name = "payment.html"
    


class FiletestView(TemplateView):
    template_name = "filetest.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            return render(request, 'filetest.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'filetest.html')

class HomeView(TemplateView):
    template_name = "home.html"

class SignupView(TemplateView):
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        username = email.split('@')[0]
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('User already exists in the system. Please login instead.')

        user = User.objects.create_user(username, email, password)

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.profile.roles = [request.POST.get('role')]
        user.profile.save()
        user.save()

        login(request, user)
        return HttpResponseRedirect('/home')

class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email:
            user = User.objects.filter(email=email).first()
            username = user.username if user else None
        user = User.objects.filter(username=username).first()

        if not user:
            return HttpResponse("User doesn't exist. Please signup and try again.")

        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse("Password incorrect. Please try again or reset password.")

        login(request, user)
        return HttpResponseRedirect('/home')




class FileTestView(TemplateView):
    template_name = "file-test.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            return render(request, 'file-test.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'file-test.html')