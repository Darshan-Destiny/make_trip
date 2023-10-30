from django.shortcuts import render
from .models import Destination,Package,Offer

# Create your views here.
def index(request):
    d = Destination.objects.all()[:4]
    p = Package.objects.all()[:3]
    o = Offer.objects.all()
    return render(request,'index.html',{'d':d,'p':p,'o':o})

def index2(request):
    return render(request,'index2.html')



def about(request):
    return render(request,'about.html')

def blog_archive(request):
    return render(request,'blog-archive.html')

def blog_archive_both(request):
    return render(request,'blog-archive-both.html')


def blog_archive_left(request):
    return render(request,'blog-archive-left.html')


def blog_single(request):
    return render(request,'blog-single.html')


def booking(request):
    return render(request,'booking.html')

def career(request):
    return render(request,'career.html')

def career_detail(request):
    return render(request,'career-detail.html')

def comming_soon(request):
    return render(request,'comming-soon.html')

def confirmation(request):
    return render(request,'confirmation.html')

def contact(request):
    return render(request,'contact.html')

def destination(request):
    d = Destination.objects.all()
    return render(request,'destination.html',{'d':d})



def faq(request):
    return render(request,'faq.html')

def gallery(request):
    return render(request,'gallery.html')

def index_v2(request):
    return render(request,'index-v2.html')

def package_detail(request):
    return render(request,'package-detail.html')

def package_offer(request):
    return render(request,'package-offer.html')

def product_cart(request):
    return render(request,'product-cart.html')

def product_checkout(request):
    return render(request,'product-checkout.html')

def product_detail(request):
    return render(request,'product-detail.html')

def product_right(request):
    return render(request,'product-right.html')

def search_page(request):
    return render(request,'search-page.html')

def service(request):
    return render(request,'service.html')

def single_page(request):
    return render(request,'single-page.html')

def testimonial_page(request):
    return render(request,'testimonial-page.html')

def tour_cart(request):
    return render(request,'tour-cart.html')

def tour_guide(request):
    return render(request,'tour-guide.html')

def tour_packages(request):
    p = Package.objects.all()[:3]
    return render(request,'tour-packages.html',{'p':p})

def wishlist_page(request):
    return render(request,'wishlist-page.html')

def page(request):
    return render(request,'404.html')



def dashboard(request):
    return render(request,'dashboard.html')

def db_add_package(request):
    return render(request,'db-add-package.html')

def db_booking(request):
    return render(request,'db-booking.html')

def db_comment(request):
    return render(request,'db-comment.html')

def db_package_active(request):
    return render(request,'db-package-active.html')

def db_package_expired(request):
    return render(request,'db-package-expired.html')

def db_package_pending(request):
    return render(request,'db-package-pending.html')

def db_wishlist(request):
    return render(request,'db-wishlist.html')

def forgot(request):
    return render(request,'forgot.html')

def login(request):
    return render(request,'login.html')

def new_user(request):
    return render(request,'new-user.html')

def user(request):
    return render(request,'user.html')

def user_edit(request):
    return render(request,'user-edit.html')


def usa(request):
    return render(request,'usa.html')
def indonesia(request):
    return render(request,'indonesia.html')

def toronto(request):
    return render(request,'toronto.html')
def india(request):
    return render(request,'india.html')

def thailand(request):
    return render(request,'thailand.html')

def japan(request):
    return render(request,'japan.html')

def new_zealand(request):
    return render(request,'new_zealand.html')

def singapore(request):
    return render(request,'singapore.html')

def dubai(request):
    return render(request,'dubai.html')







