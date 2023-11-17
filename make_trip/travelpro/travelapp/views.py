import json
from django.shortcuts import render,HttpResponse
from .models import Destination,Package,Offer
from .models import Booking,Payment,Contact,Shop,Order,Customer,OrderItem,ShippingAddress
from django.contrib import messages
from django.http import JsonResponse

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


def booking(request,id):
    pay = Payment.objects.filter(pyment=id)
    return render(request,'booking.html',{'pay':pay})

def career(request):
    return render(request,'career.html')

def career_detail(request):
    return render(request,'career-detail.html')

def comming_soon(request):
    return render(request,'comming-soon.html')

def confirmation(request):
    return render(request,'confirmation.html')

def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if name:
        my_contact = Contact.objects.create(name=name,email=email,message=message)
        my_contact.save()


        messages.info(request,'Thank You For Submit')

    return render(request,'contact.html')

def destination(request):
    d = Destination.objects.all()
    data = Package.objects.filter()
    location = ''
    if data:
        location = data[0].destination.location_name
    return render(request,'destination.html',{'d':d,'data':data, 'location_name': location})



def faq(request):
    return render(request,'faq.html')

def gallery(request):
    return render(request,'gallery.html')

def index_v2(request):
    return render(request,'index-v2.html')

def package_detail(request,id):
    data = Package.objects.filter(id=id)
    price = ''
    if data:
        price = data[0].price
        print("ssss///", price)
    if data:
        tour_guide = data[0].tour_guide
    if data:
        insurance = data[0].insurance
    if data:
        tax = data[0].tax
    if data:
        total_cost1 = float(price) + float(tour_guide)+ float(insurance)+ float(tax)
        print("dddd///",total_cost1)
        data[0].total_cost1 = total_cost1
    return render(request,'package-detail.html',{'data':data,'price':price,'tour_guide':tour_guide,'insurance':insurance,'tax':tax,'total_cost1':total_cost1})

def package_offer(request):
    return render(request,'package-offer.html')

def product_cart(request):
    if request.user.is_authenticated:
        customer = Customer.objects.filter(user=request.user)
        print("fff//",customer)

        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        if customer:
            order, created = Order.objects.get_or_create(customer=customer[0], complete=False)
            items = order.orderitem_set.all()
    return render(request,'product-cart.html',{'items':items,'order':order})


# def pro_cart(request,id):
#     data = OrderItem.objects.filter(product=id)
#     print("ggggf///",data)
#     if request.user.is_authenticated:
#         customer = Customer.objects.filter(user=request.user)
#         print("fff//",customer)
#         order, created = Order.objects.get_or_create(customer=customer[0], complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total':0, 'get_cart_items':0}
#     return render(request,'product-cart.html',{'items':data,'order':order})


def product_checkout(request,id):
    data = ShippingAddress.objects.filter(customer=id)
    return render(request,'product-checkout.html',{'data':data})

def product_detail(request):
    return render(request,'product-detail.html')

def product_right(request):
    product = Shop.objects.all()
    return render(request,'product-right.html',{'product':product})

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


def usa(request,id):
    print("fdf/f/f//",id)
    data = Package.objects.filter(destination=id)
    location = ''
    if data:
        location = data[0].destination.country_name
        print("ssss///", location)
    return render(request,'usa.html',{'data':data, 'location_name': location})
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


def DestinationDtail(request,destination):
    return HttpResponse(destination)


def savedata(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        select = request.POST['select']
        booking_date = request.POST['booking_date']
        print("dd///",name,email,number,select)
        my_model = Booking(name=name,email=email,number=number,select=select,booking_date=booking_date)
        my_model.save()
        print("dffd///",my_model)
    data = Package.objects.filter(id=id)
    price = float(data[0].price) + float(data[0].insurance) +  float(data[0].tax) + float(data[0].tour_guide)
    return render(request,'booking.html',{'my_model':my_model,'data':data, 'price': price})



def confirm(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        month = request.POST.get('month')
        year = request.POST.get('year')
        cvv_code = request.POST.get('cvv_code')
        country = request.POST.get('country')
        street1 = request.POST.get('street1')
        street2 = request.POST.get('street2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        add_information = request.POST.get('add_information')
        if request.POST.get('name'):
            my_confirm = Payment.objects.create(name=name,email=email,number=number,card_name=card_name,card_number=card_number,month=month,year=year,cvv_code=cvv_code,country=country,street1=street1,street2=street2,city=city,state=state,postal_code=postal_code,add_information=add_information)
            my_confirm.save()
    data = Package.objects.filter(id=id)
    price = float(data[0].price) + float(data[0].insurance) + float(data[0].tax) + float(data[0].tour_guide)
    return render(request,'confirmation.html',{'my_confirm': my_confirm,'data':data, 'price': price})


def updateItem(request):
    data = json.loads(request.body)
    # try:
    #     data = json.loads(request.body)
    #     print('ffdfdfdf//',data)
    # except json.decoder.JSONDecodeError:
    #     # 👇️ this runs
    #     print('The string does NOT contain valid JSON')
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)


    customer = request.user.customer
    product = Shop.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer[0], complete=False)

    orderItem, created = OrderItem.ojects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)






