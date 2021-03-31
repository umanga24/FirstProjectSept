from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django import views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from lib_mgmt_sys.models import *
from lib_mgmt_sys.forms import *
from django.views.generic import TemplateView, ListView, CreateView,UpdateView,DetailView, DeleteView
from django.contrib.auth.models import Group

from lib_mgmt_sys.serializer import BookSerializer


def is_librarian(user):
    return user.groups.filter(name='librian').exists()








# Create your views here.

class sample_view(views.View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, "index.html", {'loginform': login_form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('home')
        else:
            if user.is_active:
                login(request, user=user)
                return redirect('lms:list_books')

            else:
                return redirect('home')


def gallery(request):
    return render(request, 'gallery.html')


@login_required(login_url='/lms/login/')
@user_passes_test(is_librarian, login_url=reverse_lazy('lms:login_user'))
def add_author(request):
    if request.method == 'GET':
        author_form = AuthorModelForm
        return render(request, 'lms/add_author.html', {'author_form': author_form})

    else :
        author_form = AuthorModelForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('lms:list_authors')
        else:
            return render(request, 'lms/list_authors.html', {'author_form':author_form})

@login_required(login_url='/lms/login/')
def list_author(request):
    authors = Author.objects.all()
    return render(request, 'lms/list_authors.html', {'authors': authors})



@login_required(login_url='/lms/login/')
@user_passes_test(is_librarian, login_url=reverse_lazy('lms:login_user'))
def edit_author(request, id):
    author = Author.objects.get(id = id)
    if request.method ==    'GET':
        edit_author = AuthorModelForm(instance = author)
        return render(request, 'lms/edit_author.html', {'edit_author':edit_author})
    elif request.method == 'POST':
        edit_author = AuthorModelForm(request.POST, instance= author)
        if edit_author.is_valid():
            edit_author.save()
            return redirect('lms:list_authors')
        else:
            return render(request, 'lms/edit_author.html', {'author':author})

@login_required(login_url='/lms/login/')
@user_passes_test(is_librarian, login_url=reverse_lazy('lms:login_user'))
def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('lms:delete_author')



@login_required(login_url='/lms/login/')
def list_books(request):
    books= Books.objects.all()
    return render(request, 'lms/list_books.html', context= {'books':books})

@login_required(login_url='/lms/login/')
@user_passes_test(is_librarian, login_url=reverse_lazy('lms:login_user'))
def add_books(request):
    if request.method == 'GET':
        book_form = BookModelForm()
        return render(request, 'lms/add_books.html', {'book_form': book_form})
    else:
        book_form = BookModelForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('lms:list_books')
        else:
            return render(request, 'lms/add_books.html', {'book_form': book_form})

@login_required(login_url='/lms/login/')
@user_passes_test(is_librarian, login_url=reverse_lazy('lms:login_user'))
def edit_book(request, id):
    book = Books.objects.get(id=id)
    if request.method == "GET":
        edit_form = BookModelForm(instance=book)
        return render(request, 'lms/edit_book.html', {'edit_form': edit_form})
    elif request.method == 'POST':
        edit_book = BookModelForm(request.POST, instance=book)
        if edit_book.is_valid():
            edit_book.save()
            return redirect('lms:list_books')
        else:
            return render(request, 'lms/add_books.html', {'edit_book': edit_book})
@login_required(login_url='/lms/login/')
@user_passes_test(is_librarian, login_url=reverse_lazy('lms:login_user'))
def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('lms:list_books')

class StudentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = reverse_lazy('lms:login_user')
    model = Students
    template_name = 'lms/list_student.html'
    context_object_name = 'students'

    def test_func(self):
        return self.request.user.groups.filter(name='librian').exists()
    def handle_no_permission(self):
        return redirect('lms:login_user')

class StudentAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse_lazy('lms:login_user')
    model = Students
    template_name = 'lms/add_student.html'
    fields = '__all__'
    success_url = reverse_lazy('lms:list_student')
    #form_class = BookModelForm

    def test_func(self):
        return self.request.user.groups.filter(name='librian').exists()
    def handle_no_permission(self):
        return redirect('lms:login_user')


class StudentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse_lazy('lms:login_user')
    model = Students
    fields = '__all__'
    template_name = 'lms/edit_student.html'
    success_url = reverse_lazy('lms:list_student')
    def test_func(self):
        return self.request.user.groups.filter(name='librian').exists()
    def handle_no_permission(self):
        return redirect('lms:login_user')


    """def get_object(self, queryset=None):
        id= self.kwargs.get('id')
        return Author.objects.get(id=id)"""

class StudentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = reverse_lazy('lms:login_user')
    model = Students
    template_name = 'lms/detail_student.html'
    context_object_name = 'student'

    def test_func(self):
        return self.request.user.groups.filter(name='librian').exists()
    def handle_no_permission(self):
        return redirect('lms:login_user')

class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse_lazy('lms:login_user')
    model = Students
    template_name = 'lms/delete_student.html'
    context_object_name = 'student'
    success_url = reverse_lazy('lms:list_student')


    def test_func(self):

        return self.request.user.groups.filter(name='librian').exists()

    def handle_no_permission(self):
        return redirect('lms:login_user')





class loginUserView(views.View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'lms/login.html',{'loginform': login_form})

    def  post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user is None:
            return redirect('lms:login_user')
        else:
            if user.is_active:
                login(request, user=user)
                return redirect('lms:list_books')

            else:
                return redirect('lms:login_user')

#
# class loginUserViews(views.View):
#     def get(self, request):
#         login_form = LoginForm()
#         return render(request,'index.html', {'loginform': login_form})
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return redirect('lms:login_user')
#         else:
#             if user.is_active:
#                 login(request, user=user)
#                 return redirect('lms:list_books')
#
#             else:
#                 return redirect('lms:login_user')


class LogoutUserView(views.View):
    def get(self, request):
        logout(request)
        return redirect('home')

class RegisterUserView(views.View):
    def get(self, request):
        user_form = UserModelForm()
        return render(request, 'lms/register.html',{'form' : user_form})

    def post(self, request):
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
           user =  user_form.save()
           user.set_password(user.password)
           user.save()
           student_group = Group.objects.get(name='student')
           user.groups.add(student_group)
           login(request, user)
           return redirect('lms:list_books')
        else:
            return render(request, 'lms/register.html', {'form': user_form})




class BookAPI(views.View):
    def get(self, request):
        BooksQs = Books.objects.all()
        ser = BookSerializer(BooksQs, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        ser =  BookSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        return JsonResponse(ser.errors, status=500)



class BookObjectAPI(views.View):
    def get(self, request, id):
        book = Books.objects.get(id=id)
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

    def put(self, request, id):
        book = Books.objects.get(id=id)
        data = JSONParser().parse(request)
        ser = BookSerializer(book, data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        return JsonResponse(ser.errors, status=500)

    def delete(self, request, id):
        book = Books.objects.get(id=id)
        book.delete()
        return HttpResponse(status=200)
    

CsrfBookAPI = csrf_exempt(BookAPI.as_view())
CsrfBookObjectAPI = csrf_exempt(BookObjectAPI.as_view())





























# class AboutUsView(TemplateView):
#     template_name = 'lms/about_us.html'
#
#     def get_context_data(self):
#         return {'phone no':9887777}
#












