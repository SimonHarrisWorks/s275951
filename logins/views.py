from django.shortcuts import render, redirect
from .models import stock,customer
from .forms import customerSignup
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# defines the home page so that when it is called it will take you to the correct page
def homepage(request):
    return render(request, "home.html")

# defines the stock page so that when it is called it will take you to the correct page in
#the TS:totalstock assigns totalstock varible which shows all the stock to the TS varible so that it is callable in the html 
def stockpage(request):
     TotalStock = stock.objects.all
     return render(request, "stock.html", {'TS':TotalStock})

# the following 3 defines use a method called "POST" to check if something has been filled in a form and grabbing what they typed in
# then using it appropriately
def search_results_page(request):
    if request.method == "POST":
        search = request.POST['search']
        ## filters the input data to look for the same stockname or if it contains it
        result = stock.objects.filter(StockName__contains = search)

        # sents the user to the search results page while also sending what they searched for as the search variable and the results of the
        # search as the result varible
        return render(request, "search_results.html",
                      {'search' :search,
                       'result':result}
                      )
    # if it fails it will still send you to the results page but will display and error messages
    else:
        return render(request, "search_results.html")

def signuppage(request):
    if request.method == "POST":
        form = customerSignup(request.POST or None)
        ##checks if the form was filled out properly and if so saves it to the customer table
        if form.is_valid():
            form.save()
            ## sends the user back to the home page with a thank you pop up message
            messages.success(request,("Thank you for signing up!"))
            return redirect("home")
        else:
            # if the form is not valid it will ask the user to try again and reload the signup page
            messages.success(request,("Sorry something went wrong! Please try again"))
            return render(request, "signup.html")
        # makes it so the nav bar still takes users to the signup page 
    else:
        return render(request, "signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        ## using the import of django's auth to check usernames and passwords that where input by the user
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # when the form is not blame and submitted it says thank you if it was successfull and return the user to the home page
            login(request, user)
            messages.success(request,("Thank you for logging in!"))
            return redirect("home")
        else:
            #if the form is blank or the password or username is incorrect it will reload the page 
            messages.success(request,("Please try again."))
            return redirect("login")
        # makes it so the nav bar still takes users to the login page 
    else:
        return render(request, "login.html")

# using the logout import in django users can easily log out and are thus redirected to the homepage with a message
def logout_user(request):
    logout(request)
    messages.success(request,("You have successfully logged out"))
    return redirect("home")