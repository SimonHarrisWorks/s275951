from django.urls import path, include
from . import views

# defines all urls and redirects with names and points to the html pages
urlpatterns = [
    path("",views.homepage, name = "home"),
    path("stock/",views.stockpage, name = "stock"),
    path("signup/",views.signuppage, name = "signup"),
    path("search_results/",views.search_results_page, name = "search_results"),
    path("login",views.login_user, name = "login"),
    path("logout",views.logout_user, name = "logout"),
]