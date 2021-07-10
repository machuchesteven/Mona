from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Product, Order, ProductCategory, Customer, Seller, Comment
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.http import Http404, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from .forms import *




# Create your views here
def homepage(request):
    context = {
        'title': 'Mona Sales',
        'feature': 'The Mostly advanced AI based study assistant',
        'products': Product.objects.all()[:],
        'author': 'Machuche Steven', 
    }
    return render(request, 'Overview/homepage.html', context=context)

# start use of generic views rather than the use of class based views
class Homepage(View):
    content = "This should be changed in the url"
    def get(self, request):
        return HttpResponse(self.content)

class UserListView(View):
    def get(self, request):
        return render(request, 'Overview/index.html')
def director(request):
    return redirect(homepage)
def user(request):
    return HttpResponse("<h1>User Object Called</h1>")

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "Overview/product_detail.html"
    queryset = Product.objects.all()

class Login(View):
    "Login View"
    pass

class NewProducts(View):
    "Products added based on the latest product on the list"
    pass


def logged_in(request):
    return HttpResponse("<h1>User Logged in</h1>")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/login")
        else:
            print("The form submitted was invalid")
            print(form)
            return redirect(logged_in)
    form = UserCreationForm
    return render(request, 'Overview/register.html', {'form': form})
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "Overview/create-product.html"
    context_object_name = "form"
    success_url = "http://127.0.0.1:8000"
    success_message = "Object added to database"
    
def detail(request, id):
    obj = get_object_or_404(Product, pk=id)
    return HttpResponse(obj)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(logged_in)
    else:
        print(username + 'tried to access the system')
        return HttpResponse(f"<h1>User Log In failed, the User {username} does not exist </h1>")

def login_page(request):
    return auth_views.LoginView

def add_comment(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        comment = CommentForm(data=request.POST)
        comment.product_id = id
        if comment.is_valid():
            comment.save()
            return redirect(homepage)
        else:
            print(comment.errors)
            print("Comment form validation failed")
            return reverse(add_comment, id=id)

    comment_form = CommentForm
    comments = Comment.objects.filter(product_id=id)
    return render(request, "Overview/index.html", context={'comment_form':comment_form, 'product':product, 'comments':comments})


def tryform(request):
    form = CommentForm(request.GET or None)
    return form

def get_comments(request):
    if request.is_ajax():
        comments = Comment.objects.all()
        print(comments)
        return HttpResponse(comments)
    else:
        return HttpResponse('<h1>Object Processing failed</h1>')