from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages 
from django.http import HttpResponse
import datetime
import math
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
                                                        # Login,Registration,Join.   15-95
                                                        #index                     98-181          
                                                        # Admin                    184-516
                                                        # User                     518-686
                                                        # Payments                 687-944
                                                        # Booking                  691-941
                                                        # Employee                 1097-1171 
                                                        # Forgetpassword           1177-1120

#  Login,Registration,Join-------------------------------------------------------------------
                                                                           
def l1(request):
    return render(request,'login.html')
def brand(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        sum=0
        s=[]
        datas=products.objects.all()
        for i in datas:
            if i.category not in s:
                s.append(i.category)
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        for i in datas2:
            sum=sum+i.item_details.price
    if request.method=='POST':
        d=request.POST['st']
        datasb=products.objects.filter(brand=d)
        return render(request,'inedx_brand.html',{'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'sum':sum,'datasb':datasb,'dff':s})
    return render(request,'index_brand.html')
def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        try:
            datas=reg.objects.get(username=u)
            if  datas.password==p:
                request.session['user']=u
                return redirect(user)
            # else:
            #     messages.add_message(request, messages.INFO, "Invalid Password")
        except Exception:
            messages.add_message(request, messages.INFO, "Invalid Username")
        try:
            if u=='admin' and p=='admin':
                request.session['admin']=u
                return redirect(admin)
        except:
            messages.add_message(request, messages.INFO, "Admin Not Login") 
        try:
            datas=Join.objects.get(username=u)
            if  datas.password==p:
                request.session['emp']=u
                return redirect(employee)
        except Exception:
            messages.add_message(request, messages.INFO, "Invalid Password")
    return render(request, 'login.html')
def join(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        location=request.POST['location']
        photo=request.FILES['photo']
        license=request.FILES['license']
        username=request.POST['username']
        password=request.POST['password']
        biodata=request.FILES['biodata']
        accoundnumber=request.POST['accoundnumber']
        request.session['emp']=username
        data=Join.objects.create(firstname=firstname,lastname=lastname,email=email,phone=phone,location=location,photo=photo,license=license,username=username,password=password,biodata=biodata,accoundnumber=accoundnumber)
        data.save()
        z='ekartqwe@gmail.com'
        send_mail('Request', f'{"Employes Waiting for  your Accept "}','settings.EMAIL_HOST_USER',[z],fail_silently=False)

    return redirect(jr)
def jr(request):
    return render(request,'join.html')
def registration(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        photo=request.FILES['photo']
        username=request.POST['username']
        password=request.POST['password']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        address=request.POST['address']
        try:
            data=reg.objects.get(username=username)
            if data is not None:
                messages.error(request,'Alredy Exits')
        except Exception:
            data=reg.objects.create(firstname=firstname,lastname=lastname,email=email,phone=phone,photo=photo,username=username,password=password,pincode=pincode,city=city,state=state,address=address)
            data.save()
            z=data.email
            send_mail('Congrats !!!', f'{"Successfully Register For Ecart"}','settings.EMAIL_HOST_USER',[z],fail_silently=False)

        return redirect(r1)
    return render(request,'login.html')
def r1(request):
    return render(request,'login.html')

    #index----------------------------------------------------------------------------

def index(request):
    datas=products.objects.filter(category='topselling')
    s=[]
    for i in datas:
        if i.brand not in s:
            s.append(i.brand)
    return render(request,'index.html',{'datas':datas,'s':s})
def Smartphones(request):
    datas=products.objects.filter(category='smartphone')
    s=[]
    for i in datas:
        if i.brand not in s:
            s.append(i.brand)
    return render(request,'smartphones.html',{'datas':datas,'s':s})
def laptops(request):
    datas=products.objects.filter(category='laptop')
    s=[]
    for i in datas:
        if i.brand not in s:
            s.append(i.brand)
    return render(request,'laptops.html',{'datas':datas,'s':s})
def Cameras(request):
    s=[]
    datas=products.objects.filter(category='camera')
    for i in datas:
        if i.brand not in s:
            s.append(i.brand)
    
    return render(request,'cameras.html',{'datas':datas,'s':s})
def headphones(request):
    s=[]
    datas=products.objects.filter(category='headphone')
    for i in datas:
        if i.brand not in s:
            s.append(i.brand)
   
    return render(request,'headphones.html',{'datas':datas,'s':s})
def servies(request):
    return render(request,'servies.html')
def categories(request):
    return render(request,'categories.html')

def search_index(request):
    if request.method=='POST':
        data=request.POST['sr']
        if data=='laptop':
            return redirect(laptops)
        elif data=='camera':
            return redirect(Cameras)
        elif data=='smartphone':
            return redirect(Smartphones)
        elif data=='headphone':
            return redirect(headphones)
        else:
            return redirect(index)

    return render(request,'index.html')
def quick_view(request,d):
    if 'user' in request.session:
        datas=products.objects.filter(pk=d)
        f=products.objects.all()
        d=preview.objects.filter(kk=d)
        details=reg.objects.get(username=request.session['user'])
        usr = reg.objects.get(username=details.username)
        o = orderitem.objects.all()
        l=[]
        p=[]
        po=0
        for i in o:
            if i.orderdet.user==usr:
                if i.orderdet.status=='Delivered':
                    l.append(i.product.pname)
        for i in f:
            for j in datas:
                if i.pname==j.pname:
                    if i.qut==0:
                        po=po+1
        return render(request,'quick_view.html',{'datas':datas,'d':d,'l':l,'po':po})
    else:
        return redirect(l1)
def checkout(request):
    if 'user' in request.session:
        pp=products.objects.all()
        sum=0
        m={}
        datas=reg.objects.filter(username=request.session['user'])
        details=reg.objects.get(username=request.session['user']) 
        datas2=c_rt.objects.filter(user_details=details)
        c=datas2
        cnt = c.count()
        if c:
            cl = {}
            t=0
            for i in c:
                cl[i.item_details]=[i.quantity,i.pk,i.item_details.price*i.quantity]
                t=t+(i.item_details.price*i.quantity)
            print(cl)
            for i in datas2:
                for j in pp:
                    if i.item_details.pname == j.pname:
                        if i.quantity > j.qut:
                           m[i.item_details.pname]=j.qut
                           sum=sum+1
            print(m)
            return render(request,'checkout.html',{'datas':datas,'datas2':datas2,'cnt':cnt,'total':t,'sub':cl,'pp':pp,'sum':sum,'m':m})
        return redirect(user)
    else:
        return redirect(l1)
    
def store(request):
    return render(request,'store.html')
  

# --------------------------Admin--------------------------

def admin(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='topselling')
        datas5=alert.objects.all().count()
        datas4=alert.objects.all()
        emp=products.objects.filter(category='topselling').first()
        pro=product_pic.objects.all()
        return render(request,'admin.html',{'datas':datas,'datas5':datas5,'datas4':datas4,'pro':pro})
    return redirect(l1)

def ad_camera(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='camera')
        return render(request,'ad_camera.html',{'datas':datas})
    return redirect(l1)
def ad_laptop(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='laptop')
        return render(request,'ad_laptop.html',{'datas':datas})
    return redirect(l1)
def ad_headphone(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='headphone')
        return render(request,'ad_headphone.html',{'datas':datas})
    return redirect(l1)
def ad_smartphone(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='smartphone')
        return render(request,'ad_smartphone.html',{'datas':datas})
    return redirect(l1)

def cr(request):
    return render(request,'ad_add_camera.html')
def ad_add_products(request):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        mi=request.FILES['m']
        fi=request.FILES['f']
        sm=request.FILES['s']
        tm=request.FILES['t']
        dis=request.POST['dis']
        qut=request.POST['qut']
        color=request.POST['color']
        discound=request.POST['discound']
        f1=request.POST['f1']
        f2=request.POST['f2']
        f3=request.POST['f3']
        f4=request.POST['f4']
        category=request.POST['1']
        data=products.objects.create(pname=pname,price=price,mi=mi,fi=fi,sm=sm,tm=tm,dis=dis,qut=qut,discound=discound,f1=f1,f2=f2,f3=f3,f4=f4,color=color,category=category)
        data.save()
    return redirect(lr)
def lr(request):
    return render(request,'ad_add_products.html')
def ad_laptop(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='laptop')
        return render(request,'ad_laptop.html',{'datas':datas})
    return redirect(l1)
def ad_view_employe(request):
    if 'admin' in  request.session:
        datas=Join.objects.all()
        return render(request,'ad_view_employe.html',{'datas':datas})
    return redirect(l1)
def admin_emp_edit(request,d):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        location=request.POST['location']
        # photo=request.FILES['photo']
        # license=request.FILES['license']
        username=request.POST['username']
        password=request.POST['password']
        # biodata=request.FILES['biodata']
        accoundnumber=request.POST['accoundnumber']
        datas=Join.objects.filter(pk=d).update(firstname=firstname,lastname=lastname,email=email,phone=phone,location=location,username=username,password=password,accoundnumber=accoundnumber)
    datas=Join.objects.filter(pk=d)
    return render(request,'admin_emp_edit.html',{'datas':datas})
def ad_headphone_edit(request,d):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        dis=request.POST['dis']
        mi=request.FILES['m']
        fi=request.FILES['f']
        sm=request.FILES['s']
        tm=request.FILES['t']
        qut=request.POST['qut']
        color=request.POST['color']
        discound=request.POST['discound']
        b=request.POST['b']
        f1=request.POST['f1']
        f2=request.POST['f2']
        f3=request.POST['f3']
        f4=request.POST['f4']
        datas=products.objects.filter(pk=d).update(pname=pname,price=price,dis=dis,qut=qut,discound=discound,f1=f1,f2=f2,f3=f3,f4=f4,color=color,brand=b,mi=mi,fi=fi,sm=sm,tm=tm)
    datas=products.objects.filter(pk=d)
    return render(request,'ad_headphone_edit.html',{'datas':datas})
def ad_smartphone_edit(request,d):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        dis=request.POST['dis']
        qut=request.POST['qut']
        discound=request.POST['discound']
        b=request.POST['b']
        f1=request.POST['f1']
        color=request.POST['color']
        f2=request.POST['f2']
        f3=request.POST['f3']
        f4=request.POST['f4']
        datas=products.objects.filter(pk=d).update(pname=pname,price=price,dis=dis,qut=qut,discound=discound,f1=f1,f2=f2,f3=f3,f4=f4,color=color,brand=b)
    datas=products.objects.filter(pk=d)
    return render(request,'ad_smartphone_edit.html',{'datas':datas})
def ad_camera_edit(request,d):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        dis=request.POST['dis']
        color=request.POST['color']
        qut=request.POST['qut']
        discound=request.POST['discound']
        b=request.POST['b']
        f1=request.POST['f1']
        f2=request.POST['f2']
        f3=request.POST['f3']
        f4=request.POST['f4']
        
        datas=products.objects.filter(pk=d).update(pname=pname,price=price,dis=dis,qut=qut,discound=discound,f1=f1,f2=f2,f3=f3,f4=f4,color=color,brand=b)
    datas=products.objects.filter(pk=d)
    return render(request,'ad_camera_edit.html',{'datas':datas})
def ad_laptop_edit(request,d):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        # mi=request.FILES['m']
        # fi=request.FILES['f']
        # sm=request.FILES['s']
        # tm=request.FILES['t']
        b=request.POST['b']
        dis=request.POST['dis']
        qut=request.POST['qut']
        color=request.POST['color']
        discound=request.POST['discound']
        f1=request.POST['f1']
        f2=request.POST['f2']
        f3=request.POST['f3']
        f4=request.POST['f4']
        datas=products.objects.filter(pk=d).update(pname=pname,price=price,dis=dis,qut=qut,discound=discound,f1=f1,f2=f2,f3=f3,f4=f4,color=color,brand=b)
    datas=products.objects.filter(pk=d)
    return render(request,'ad_laptop_edit.html',{'datas':datas})
def laptop_delete(request,d):
    datas=products.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_laptop)
# def selct_option_admin(request):
    # if request.method=='POST':
    #     data=request.POST['sr']
    #     if data=='viewuser':
    #         return redirect(ad_view_user)
    #     elif data=='viewemp':
    #         return redirect(ad_view_employe)
    #     elif data=='viewoder':
    #         return redirect(ad_viewoder)
    #     else:
    #         return redirect(admin)

def ad_topselling_edit(request,d):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        discound=request.POST['discound']
        # mi=request.FILES['m']
        # fi=request.FILES['f']
        # sm=request.FILES['s']
        # tm=request.FILES['t']
        b=request.POST['b']
        dis=request.POST['dis']
        qut=request.POST['qut']
        color=request.POST['color']
        f1=request.POST['f1']
        f2=request.POST['f2']
        f3=request.POST['f3']
        f4=request.POST['f4']
        datas=products.objects.filter(pk=d).update(pname=pname,price=price,discound=discound,dis=dis,qut=qut,color=color,f1=f1,f2=f2,f3=f3,f4=f4,brand=b,)
    datas=products.objects.filter(pk=d)
    return render(request,'ad_topselling_edit.html',{'datas':datas})
def tr(request):
    return render(request,'ad_add_topsellings.html')
def ad_topselling(request):
    if 'admin' in request.session:
        datas=products.objects.filter(category='topselling')
        return render(request,'ad_topselling.html',{'datas':datas})
    return redirect(l1)
def delete(request,d):
    datas=Join.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_view_employe)

def camera_delete(request,d):
    datas=products.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_camera)
def smartphone_delete(request,d):
    datas=products.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_smartphone)
def headphone_delete(request,d):
    datas=products.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_headphone)
def toselling_delete(request,d):
    datas=products.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_topselling)
def ad_view_user(request):
    if 'admin' in request.session:
        datas=reg.objects.all()
        return render(request,'ad_view_user.html',{'datas':datas})
    return redirect(l1)
def admin_user_edit(request,d):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        # photo=request.FILES['photo']
        username=request.POST['username']
        password=request.POST['password']
        datas=reg.objects.filter(pk=d).update(firstname=firstname,lastname=lastname,email=email,phone=phone,username=username,password=password)
    datas=reg.objects.filter(pk=d)
    return render(request,'admin_user_edit.html',{'datas':datas})
def delete2(request,d):
    datas=reg.objects.filter(pk=d)
    datas.delete()
    return redirect(ad_view_user)
def accept_request(request,d):
    Join.objects.filter(pk=d).update(status=1)
    return redirect(ad_request)

def ad_request(request):
    datas=Join.objects.all()
    return render(request,'ad_request.html',{'datas':datas})
def alert_dele(request,d):
    data=alert.objects.filter(pk=d)
    data.delete()
    return redirect(admin)
def rs(request):
    datas=products.objects.all()
    d=orderitem.objects.all()
    c={}
    for i in d:
        c[i.pk,i.product.pname]=[i.quantity]
    return render(request,'ad_stoks.html',{'datas':datas,'items':c})
def ad_stoks(request):
    datas=products.objects.all()
    d=orderitem.objects.all()
    c={}
    for i in d:
        c[i.pk,i.product.pname]=[i.quantity]
    ct=d.count()
    # for i in datas:
    #     for j in d:
    #         if i.pname==j.product.pname:
    #             st=i.qut-j.quantity
    #             stok=products.objects.filter(pname=j.product.pname).update(qut=st)
    #     return redirect(rs)
    return render(request,'ad_stoks.html',{'datas':datas,'items':c})
def ad_stock_update(request,d):
    if request.method=='POST':
        p=request.POST['qut']
        dat=products.objects.all()
        datas=products.objects.filter(pk=d).update(qut=p)
        return redirect(ad_stoks)
    da=products.objects.filter(pk=d)
    return render(request,'ad_stock_update.html',{'datas':da})
def ad_DeliveryDetails(request):
    l=0
    l2=0
    l3=0
    l4=0
    kk=[]
    items=orderitem.objects.all()
    for i in items:
        if i.orderdet.status=='Delivered':
            l=l+1
        elif i.orderdet.status=='Out for shipping':
            l2=l2+1
        elif i.orderdet.status=='pending':
            l3=l3+1
        elif i.orderdet.status=='Cancelled':
            l4=l4+1
    for i in items:
        kk.append(i.status)
    return render(request,'ad_DeliveryDetails.html',{'items':items,'l':l,'l2':l2,'l3':l3,'l4':l4})
def ad_sigle_empdetails(request,d):
    datas=Join.objects.filter(pk=d)
    return render(request,'ad_sigle_empdetails.html',{'datas':datas})
def ad_order_distribute(request):
    items=orderitem.objects.all()
    datas=Join.objects.all()
    l=[]
    z=[]
    for i in items:
        l.append(i.status)
    # print(l)
    for i in l:
        z.append(l.count(i))
    return render(request,'ad_order_distribute.html',{'items':items,'datas':datas})
def ad_order_status(request,d):
    if request.method=='POST':
        n=request.POST['sr']
        print(n)
        datas=orderitem.objects.filter(pk=d).update(status=n)
        return redirect(ad_order_distribute)
def ad_feedback(request):
    datas=Feedback.objects.all()
    return render(request,'ad_feedback.html',{'datas':datas})
def replymaill(request,d):
    datas=Feedback.objects.filter(pk=d)
    return render(request,'replymail.html',{'datas':datas})
def repl(request):
    if request.method == 'POST':
        email=request.POST['email']
        z='ekartqwe@gmail.com'
        re=request.POST['message']
        send_mail('Ekart Message', f'{email},{re}','settings.EMAIL_HOST_USER',[z],fail_silently=False)
    return redirect(admin)
def search_admin(request):
    if request.method=='POST':
        data=request.POST['sr']
        if data=='laptop':
            return redirect(ad_laptop)
        elif data=='camera':
            return redirect(ad_camera)
        elif data=='smartphone':
            return redirect(ad_smartphone)
        elif data=='headphone':
            return redirect(ad_headphone)
        elif data=='topselling':
            return redirect(ad_topselling)
        elif data=='view employee':
            return redirect(ad_view_employe)
        elif data=='view user':
            return redirect(ad_view_user)
        elif data=='view oder':
            return redirect(ad_view_orders)
        elif data=='request':
            return redirect(ad_request)
        elif data=='feedback':
            return redirect(ad_feedback)
    return redirect(admin)
def ad_view_orders(request):
    items=orderitem.objects.all()
    return render(request,'ad_viewoders.html',{'items':items})
def ad_propicupdate(request,d):
    if request.method=='POST':
        mi=request.FILES['m']
        fi=request.FILES['f']
        sm=request.FILES['s']
        tm=request.FILES['t']
        datas=products.objects.filter(pk=d).update(mi=mi,fi=fi,sm=sm,tm=tm)
    return render(request,'ad_product_picedit.html')

# ------------------User--------------------------------------------------------------#

def user(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        s=[]
        po=[]
        summ=0
        f=products.objects.all()
        datas=products.objects.filter(category='topselling')
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        sum=0
        for i in datas2:
            sum=sum+i.item_details.price
        for i in datas:
            if i.brand not in s:
                s.append(i.brand)
        for i in f:
            for j in datas:
                if i.pname==j.pname:
                    if i.qut==0:
                        summ=summ+1
                        po.append(i.pname)
        # print(po)
        return render(request,'user.html',{'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'sum':sum,'details':details,'s':s,'po':po})
    return redirect(l1)
def myaccound(request):
    if 'user' in request.session:
        datas=reg.objects.filter(username=request.session['user']).first()
        pro=profilepic_user.objects.filter(user=datas).first() 
        return render(request,'my accound.html',{'datas':datas,'pro':pro})
    else:
        return redirect(l1)
def accound_edit(request):
    if 'user' in request.session:
        emp=reg.objects.filter(username=request.session['user']).first()
        pro=profilepic_user.objects.filter(user=emp).first()
        if request.method=='POST':
            emp.firstname=request.POST.get('firstname')
            emp.lastname=request.POST.get('lastname')
            emp.email=request.POST.get('email')
            emp.phone=request.POST.get('phone')
            emp.password=request.POST.get('password')
            photo=request.FILES.get('Photo')
            if photo == None:
                emp.save()
            else:
                if pro:
                    pro.user=emp
                    pro.propic=photo
                    emp.save()
                    pro.save()
                else:
                    cr=profilepic_user.objects.create(user=emp,propic=photo)
                    cr.save()
            return redirect(user)
        return render(request,'accound_edit.html',{'datas':emp,'pro':pro})
    return redirect(l1)
def user_camera(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        s=[]
        sum=0
        po=[]
        summ=0
        f=products.objects.all()
        datas=products.objects.filter(category='camera')
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        for i in datas2:
            sum=sum+i.item_details.price
        for i in datas:
            if i.brand not in s:
                s.append(i.brand)
        for i in f:
            for j in datas:
                if i.pname==j.pname:
                    if i.qut==0:
                        summ=summ+1
                        po.append(i.pname)
        return render(request,'user_camera.html',{'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'sum':sum,'s':s,'po':po})
    return redirect(l1)
def user_smartphone(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        s=[]
        sum=0
        po=[]
        summ=0
        f=products.objects.all()
        datas=products.objects.filter(category='smartphone')
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        for i in datas2:
            sum=sum+i.item_details.price
        for i in datas:
            if i.brand not in s:
                s.append(i.brand)
        for i in f:
            for j in datas:
                if i.pname==j.pname:
                    if i.qut==0:
                        summ=summ+1
                        po.append(i.pname)
        return render(request,'user_smartphone.html',{'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'sum':sum,'s':s,'po':po})
    return redirect(l1)
def user_headphone(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        sum=0
        s=[]
        po=[]
        summ=0
        f=products.objects.all()
        datas=products.objects.filter(category='headphone')
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        for i in datas2:
            sum=sum+i.item_details.price
        for i in datas:
            if i.brand not in s:
                s.append(i.brand)
        for i in f:
            for j in datas:
                if i.pname==j.pname:
                    if i.qut==0:
                        summ=summ+1
                        po.append(i.pname)
        return render(request,'user_headphone.html',{'sum':sum,'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'s':s,'po':po})
    return redirect(l1)

def user_laptop(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        s=[]
        sum=0
        po=[]
        summ=0
        f=products.objects.all()
        datas=products.objects.filter(category='laptop')
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        for i in datas2:
            sum=sum+i.item_details.price
        for i in datas:
            if i.brand not in s:
                s.append(i.brand)
        for i in f:
            for j in datas:
                if i.pname==j.pname:
                    if i.qut==0:
                        summ=summ+1
                        po.append(i.pname)
        return render(request,'user_laptop.html',{'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'sum':sum,'s':s,'po':po})
    return redirect(l1)

def u1(request):
    return render(request,'user.html')
def user_brand(request):
    if 'user' in request.session:
        l=[]
        l2=[]
        sum=0
        s=[]
        datas=products.objects.all()
        for i in datas:
            if i.category not in s:
                s.append(i.category)
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details).count()
        datas4=Wishlist.objects.filter(user_details=details)
        for i in datas4:
            l2.append(i.item_details)
        datas5=Wishlist.objects.filter(user_details=details).count()
        for i in datas2:
            sum=sum+i.item_details.price
    if request.method=='POST':
        d=request.POST['st']
        datasb=products.objects.filter(brand=d)
        return render(request,'user_brand.html',{'datas':datas,'datas2':datas2,'datas3':datas3,'datas4':datas4,'datas5':datas5,'datas6':l,'datas7':l2,'sum':sum,'datasb':datasb,'dff':s})
    return render(request,'user_brand.html')
def search_user(request):
    if request.method=='POST':
        datas=products.objects.all()
        data=request.POST['sr']
        if data=='laptop':
            return redirect(user_laptop)
        elif data=='camera':
            return redirect(user_camera)
        elif data=='smartphone':
            return redirect(user_smartphone)
        elif data=='headphone':
            return redirect(user_headphone)
        elif data=='myaccound':
            return redirect(myaccound)
        elif data=='cart':
            return redirect(viewcart)
        elif data=='checkout':
            return redirect(checkout)
        elif data=='about':
            return redirect(about)
        elif data=='Feedback':
            return redirect(contact)
        elif data =='':
            return redirect(user)
        for i in datas:
            if data not in i.category:
                return redirect(user)
    return redirect(user)
def about(request):
    return render(request,'about.html')
def contact(request):
    if 'user' in request.session:
        return render(request,'contact.html')
    return redirect(l1)
def logout(request):
    if 'user' in request.session or 'admin' in request.session or 'emp' in request.session:
        request.session.flush()
    return redirect(index)
def sample(request):
    return render(request,'sample.html')
def Preview(request,d):
    if 'user' in request.session:
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            text=request.POST['text']
            date=datetime.datetime.now()
            star=request.POST['rating']
            pho=request.FILES['ph']
            kk=request.POST['pp']
            data=preview.objects.create(name=name,email=email,text=text,date=date,star=star,kk=kk,photo=pho)
            data.save()
        return redirect(quick_view,d)
    return redirect(l1)
def oder_del(request,d):
    if 'user' in request.session:
        datas=order.objects.filter(pk=d)
        z=''
        s=0
        for i in datas:
            z=i.user.email
            s=i.total_price
            messsage='Refund to your bank account'
            if i.payment_mode=='Razorpay':
                send_mail('Refund', f'{messsage},{s}','settings.EMAIL_HOST_USER',[z],fail_silently=False)
        datas.delete()
        return redirect(orderss)
    return redirect(l1)

def feedback(request):
    if 'user' in request.session:
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            text=request.POST['message']
            data=Feedback.objects.create(name=name,email=email,text=text)
            data.save()
        return render(request,'contact.html')
    return redirect(l1)

# -------------------------------------Payments----------------------------------------

def Singl_booking_cansel(request,d):
    p=SigleBooking.objects.filter(pk=d)
    p.delete()
    return redirect(user)
# def checkout1(request):
#     return render(request,'checkout1.html')
def single_pro_booking(request,d):
    if 'user' in request.session:
        if request.method=='POST':
            prodetail=products.objects.filter(pk=d)
            userdetail=reg.objects.get(username=request.session['user'])
            tprice=request.POST['total_l']
            quantity=request.POST['quantity']
            datas=SigleBooking.objects.create(user=userdetail,product=prodetail,quantity=quantity,price=tprice)
            datas.save()
        return redirect(user)
    return redirect(l1)
def placeorder(r):
    if 'user' in r.session:
        f=products.objects.all()
        details=reg.objects.get(username=r.session['user'])
        print(details)
        usr = reg.objects.get(username = details.username)
        c = c_rt.objects.filter(user_details=details).all()
        t=0
        for i in c:
            t=t+(i.item_details.price*i.quantity)
        if r.method == 'POST':   
            if r.POST.get('save')=='save':
                fname = r.POST.get('fname')
                lname = r.POST.get('lname')
                email = r.POST.get('email')
                phone = r.POST.get('phone')
                address = r.POST.get('address')
                city = r.POST.get('city')
                state = r.POST.get('state')
                pincode = r.POST.get('pincode')
                pro = profile.objects.filter(user=usr).first()  
                if pro:    
                    pro.fname = r.POST.get('fname')
                    pro.lname = r.POST.get('lname')
                    pro.email = r.POST.get('email')
                    pro.phone = r.POST.get('phone')
                    pro.address = r.POST.get('address')
                    pro.city = r.POST.get('city')
                    pro.state = r.POST.get('state')
                    pro.pincode = r.POST.get('pincode')
                    pro.save()
                else:
                    cr = profile.objects.create(user=usr,fname=fname,lname=lname,email=email,phone=phone,address=address,city=city,state=state,pincode=pincode)
                    cr.save()
                return redirect(placeorder)
            else:
                neworder = order()
                neworder.user = usr
                neworder.fname = r.POST.get('fname')
                neworder.lname = r.POST.get('lname')
                neworder.email = r.POST.get('email')
                neworder.phone = r.POST.get('phone')
                neworder.address = r.POST.get('address')
                neworder.city = r.POST.get('city')
                neworder.state = r.POST.get('state')
                neworder.pincode = r.POST.get('pincode')

                neworder.total_price = t

                neworder.payment_mode = r.POST.get('payment_mode')
                neworder.payment_id = r.POST.get('payment_id')

                trackno = 'ecart'+str(random.randint(1111111,9999999))
                while order.objects.filter(tracking_no=trackno) is None:
                    trackno = 'ecart'+str(random.randint(1111111,9999999))
                neworder.tracking_no = trackno
                neworder.save()

                for item in c:
                    orderitem.objects.create(
                        orderdet = neworder,
                        product = item.item_details,
                        price = item.item_details.price,
                        quantity = item.quantity
                    )
                datas=orderitem.objects.all()
                da=products.objects.all()
                for i in da:
                    for j in c:
                        if i.pname==j.item_details.pname:
                            sum=i.qut-j.quantity
                            dat=products.objects.filter(pname=j.item_details.pname).update(qut=sum)
                            if sum<5:
                                z='ekartqwe@gmail.com'
                                send_mail('Stock Messsage', f'{j.item_details.pname},{"Out Of Stock"}','settings.EMAIL_HOST_USER',[z],fail_silently=False)
                c_rt.objects.filter(user_details=details).delete()
                messages.success(r, 'Your order has been placed successfully')
                payMode = r.POST.get('payment_mode')
                if payMode == "Razorpay":
                    return JsonResponse({'status':'Your order has been placed successfully'})
        return redirect(checkout)
def orderss(r):
    if 'user' in r.session:
        details=reg.objects.get(username=r.session['user'])
        usr = reg.objects.get(username=details.username)
        o = order.objects.all()
        l=[]
        for i in o:
            if i.user==usr:
                l.append(i)
        return render(r,'myoders.html',{'l':l})
    return render(r,'myorder.html')
def razorpaycheck(r):
    if 'user' in r.session:
        se = reg.objects.get(username=r.session['user'])
        c = c_rt.objects.filter(user_details=se).all()
        t=0
        for i in c:
            t=t+(i.item_details.price*i.quantity)

    return JsonResponse({
        'total_price':int(t)
    })
def razorpaycheck2(r):
    if 'user' in r.session:
        se = reg.objects.get(username=r.session['user'])
        s = SigleBooking.objects.filter(user_details=se).all()
        t=0
        for i in s:
            t=t+(i.item_details.price*i.quantity)
            print(i.item_details.pname)
    return JsonResponse({
        'total_price':int(t)
    })
def checkout_single(request,d):
    if 'user' in request.session:
        if request.method=='POST':
            u_de=reg.objects.get(username=request.session['user'])
            p_de=products.objects.get(pk=d)
            d_time=datetime.datetime.now()
            quantity=request.POST['quantity']
            total_price=request.POST['total_l']
            details=SigleBooking.objects.create(user_details=u_de,item_details=p_de,date=d_time,quantity=quantity,tprice=total_price,price=0)
            details.save()
            return redirect(r6,d)
        return render(request,'checkout_single.html')
    return redirect(l1)
def r6(re,d):
    if 'user' in re.session:
        c=d
        pp=products.objects.all()
        details=reg.objects.get(username=re.session['user'])
        p_de=SigleBooking.objects.filter(user_details=details)
        d=SigleBooking.objects.filter(item_details=d)
        f=SigleBooking.objects.all()
        # for i in pp:
        #     for j in d:
        #         if i.pname==j.item_details.pname:
        #             print(i.pname)
        return render(re,'checkout_single.html',{'datas':details,'data':p_de,'d':d,'j':c,'f':f,'pp':pp})
    return redirect(l1)


def placeorder2(r):
    if 'user' in r.session:
        details=reg.objects.get(username=r.session['user'])
        print(details)
        usr = reg.objects.get(username = details.username)
        c = SigleBooking.objects.filter(user_details=details).all()
        t=0
        for i in c:
            t=t+(i.item_details.price*i.quantity)
        if r.method == 'POST':   
            if r.POST.get('save')=='save':
                fname = r.POST.get('fname')
                lname = r.POST.get('lname')
                email = r.POST.get('email')
                phone = r.POST.get('phone')
                address = r.POST.get('address')
                city = r.POST.get('city')
                state = r.POST.get('state')
                pincode = r.POST.get('pincode')
                pro = profile.objects.filter(user=usr).first()  
                if pro:    
                    pro.fname = r.POST.get('fname')
                    pro.lname = r.POST.get('lname')
                    pro.email = r.POST.get('email')
                    pro.phone = r.POST.get('phone')
                    pro.address = r.POST.get('address')
                    pro.city = r.POST.get('city')
                    pro.state = r.POST.get('state')
                    pro.pincode = r.POST.get('pincode')
                    pro.save()
                else:
                    cr = profile.objects.create(user=usr,fname=fname,lname=lname,email=email,phone=phone,address=address,city=city,state=state,pincode=pincode)
                    cr.save()
                return redirect(placeorder2)
            else:
                neworder = order()
                neworder.user = usr
                neworder.fname = r.POST.get('fname')
                neworder.lname = r.POST.get('lname')
                neworder.email = r.POST.get('email')
                neworder.phone = r.POST.get('phone')
                neworder.address = r.POST.get('address')
                neworder.city = r.POST.get('city')
                neworder.state = r.POST.get('state')
                neworder.pincode = r.POST.get('pincode')
                neworder.total_price = t
                neworder.payment_mode = r.POST.get('payment_mode')
                neworder.payment_id = r.POST.get('payment_id')
                trackno = 'ecart'+str(random.randint(1111111,9999999))
                while order.objects.filter(tracking_no=trackno) is None:
                    trackno = 'ecart'+str(random.randint(1111111,9999999))
                neworder.tracking_no = trackno
                neworder.save()

                for item in c:
                    orderitem.objects.create(
                        orderdet = neworder,
                        product = item.item_details,
                        price = item.item_details.price,
                        quantity = item.quantity
                    )
                datas=orderitem.objects.all()
                for i in c:
                    print(i.item_details.pname)
                da=products.objects.all()
                sum=0
                for i in da:
                    for j in c:
                        if i.pname==j.item_details.pname:
                            sum=i.qut-j.quantity
                            dat=products.objects.filter(pname=j.item_details.pname).update(qut=sum)
                            if sum<5:
                                z='ekartqwe@gmail.com'
                                send_mail('Stock Messsage', f'{j.item_details.pname},{"Out Of Stock"}','settings.EMAIL_HOST_USER',[z],fail_silently=False)

                SigleBooking.objects.filter(user_details=details).delete()
                messages.success(r, 'Your order has been placed successfully')
                payMode = r.POST.get('payment_mode')
                if payMode == "Razorpay":
                    return JsonResponse({'status':'Your order has been placed successfully'})
        return redirect(user)
    
def razorpaycheck2(r):
    if 'user' in r.session:
        se = reg.objects.get(username=r.session['user'])
        c = SigleBooking.objects.filter(user_details=se).all()
        print(c)
        t=0
        for i in c:
            t=t+(i.item_details.price*i.quantity)
    return JsonResponse({
        'total_price':int(t)
    })
def viewcart(request):
    if 'user' in request.session:
        pp=products.objects.all()
        details=reg.objects.get(username=request.session['user'])  #single user details get
        datas2=c_rt.objects.filter(user_details=details)
        c=datas2
        sum=[]
        l=0
        d=products.objects.all()
        t=0

        sub={}
        su=datas2
        for i in su:
            sub[i.item_details]=[i.quantity,i.pk,i.item_details.price*i.quantity]
        print(sub)
        for i in c:
            t=t+(i.item_details.price*i.quantity)
        for i in sub:
            sum.append(sub[i])
        print(sum)

        return render(request,'view_car.html',{'datas':datas2,'total':t,'sub':sub,'cl':sub,'d':d})  
def car(request,d):
    if 'user' in request.session:
        u_de=reg.objects.get(username=request.session['user'])
        p_de=products.objects.get(pk=d)
        date_t=datetime.datetime.now()
        datas=c_rt.objects.create(user_details=u_de,item_details=p_de,date=date_t,price=0,tprice=0)
        datas.save()
        if p_de.category=='laptop':
            return redirect(user_laptop)
        elif p_de.category=='camera':
            return redirect(user_camera)
        elif p_de.category=='headphone':
            return redirect(user_headphone)
        elif p_de.category=='smartphone':
            return redirect(user_smartphone)
        elif p_de.category=='topselling':
            return redirect(user)
    return redirect(l1)
def wishlist(request,d):
    if 'user' in request.session:
        u_de=reg.objects.get(username=request.session['user'])
        p_de=products.objects.get(pk=d)
        date_t=datetime.datetime.now()
        datas=Wishlist.objects.create(user_details=u_de,item_details=p_de,date=date_t)
        datas.save()
        if p_de.category=='laptop':
            return redirect(user_laptop)
        elif p_de.category=='camera':
            return redirect(user_camera)
        elif p_de.category=='headphone':
            return redirect(user_headphone)
        elif p_de.category=='smartphone':
            return redirect(user_smartphone)
        elif p_de.category=='topselling':
            return redirect(user)
    return redirect(l1)
def delete_w(request,d):
    datas=Wishlist.objects.get(pk=d)
    datas.delete()
    return redirect(user)
def delete_c(request,d):
    datas=c_rt.objects.get(pk=d)
    datas.delete()
    return redirect(viewcart)
def view_wisul(request):
    if 'user' in request.session:
        details=reg.objects.get(username=request.session['user'])
        datas=Wishlist.objects.filter(user_details=details)
        l=[]
        l2=[]
        for i in datas:
            l.append(i.item_details)
        datas2=c_rt.objects.filter(user_details=details)
        for i in datas2:
            l2.append(i.item_details)
        datas3=c_rt.objects.filter(user_details=details)
        return render(request,'view_wisul.html',{'datas':datas,'datas1':l,'datas2':l2})
    return redirect(r1)
def update_cart(request):
    if request.session['user']:
        l=[]
        if request.method=='POST':
            tprice=request.POST['overall_total']
            price=request.POST['in_total']
            quantity=request.POST['quantity']
            print(price)    
        return redirect(viewcart)
    return redirect(l1)


# ---------------------------Decreasing cart items---------------------------

def minuscart(d2,de):
    if 'user' in d2.session:
        c=c_rt.objects.get(id=de)
        if c.quantity>1:
            c.quantity = c.quantity - 1
            c.save()
        else:
            c.delete()
    return redirect(viewcart)
    

# -----------------------Increasing cart items----------------------------

def pluscart(d3,de):
    if 'user' in d3.session:
        c=c_rt.objects.get(id=de)
        c.quantity = c.quantity + 1
        c.save()
    return redirect(viewcart)

def statusup(r,wal):
    if r.method == "POST":
        st = order.objects.get(id=wal)
        st.status = r.POST.get('status')
        st.save()
        return redirect(emp_myoders)
    



# ----------------------------Employee------------------------------------

def stock_slert(request):
    if request.method=='POST':
        item=request.POST['sr']
        messge=request.POST['message']
        z=request.POST['email'] 
        send_mail('Stock Messsage', f'{item},{messge}','settings.EMAIL_HOST_USER',[z],fail_silently=False)
    return redirect(emp_myoders)

def employee(request):
    if 'emp' in request.session:
        return render(request,'employee.html')
    else:
        return redirect(jr)
def emp_chnagepassword(request,d):
    if request.session['emp']:
        datas=Join.objects.filter(pk=d)
        if request.method=='POST':
            # username=request.POST['username']
            password=request.POST['password']
            cr=Join.objects.filter(pk=d).update(password=password)
        return render(request,'emp_chnagepassword.html',{'datas':datas})
    return redirect(l1)
def emp_cash(request):
    if 'emp' in request.session:
        datas=Join.objects.get(username=request.session['emp'])
        return render(request,'emp_cash.html',{'datas':datas})
    return redirect(jr)

def emp_myoders(request):
    if 'emp' in request.session:
        d=Join.objects.get(username=request.session['emp'])
        datas=orderitem.objects.filter(status=d.pk)
        d=products.objects.all()
        # items=orderitem.objects.all()
        return render(request,'emp_myoders.html',{'datas':datas,'d':d})
    return redirect(jr)

def emp_userdetails(request,d):
    datas=reg.objects.filter(id=d)
    return render(request,'emp_userdetails.html',{'datas':datas})
def emp_editprofile(request):
    if 'emp' in request.session:
        emp=Join.objects.filter(username=request.session['emp']).first()
        pro=profilepic.objects.filter(user=emp).first()
        if request.method=='POST':
            emp.firstname=request.POST.get('firstname')
            emp.lastname=request.POST.get('lastname')
            emp.accoundnumber=request.POST.get('accoundnumber')
            emp.email=request.POST.get('email')
            emp.phone=request.POST.get('phone')
            emp.location=request.POST.get('location')
            photo=request.FILES.get('Photo')
            if photo == None:
                emp.save()
            else:
                if pro:
                    pro.user=emp
                    pro.propic=photo
                    emp.save()
                    pro.save()
                else:
                    cr=profilepic.objects.create(user=emp,propic=photo)
                    cr.save()
            return redirect(employee)
        return render(request,'emp_editprofile.html',{'datas':emp,'pro':pro})
    return redirect(l1)
def volapcard(request):
    if 'emp' in request.session:
        datas=Join.objects.filter(username=request.session['emp'])
        emp=Join.objects.filter(username=request.session['emp']).first()
        pro=profilepic.objects.filter(user=emp).first()
    return render(request,'emp-apcard.html',{'datas':datas,'pro':pro})
def emp_stockmessage(request):
    d='ekartqwe@gmail.com'
    datas=products.objects.all()
    return render(request,'emp_stockmessage.html',{'d':d,'datas':datas})


# -------------------------Forgetpassword-------------------------------


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = reg.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)
        
        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        
        try: 
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'password_reset_sent.html')
def forgot_password_emp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Join.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password_emp)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordResetemp.objects.create(user=user, token=token)
        
        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        
        try: 
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            return render(request, 'emailsent_emp.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)
    return render(request, 'password_reset_sent_emp.html')
def emailsent(request):
    return render(request,'emailsent.html')
def reset_password(request, token):
    # Verify token and reset the password
    password_reset = PasswordReset.objects.get(token=token)
    usr = reg.objects.get(id=password_reset.user_id)
    return render(request, 'reset_password.html',{'token':token})
def reset_password_emp(request, token):
    # Verify token and reset the password
    password_reset = PasswordResetemp.objects.get(token=token)
    usr = Join.objects.get(id=password_reset.user_id)
    return render(request, 'reset_password_emp.html',{'token':token})
def reset_password2(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    usr = reg.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('repeatpassword')
        if repeat_password == new_password:
            password_reset.user.password = new_password
            password_reset.user.save()
            password_reset.delete()
            return redirect(login)
    return render(request, 'reset_password.html')
def reset_password3(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordResetemp.objects.get(token=token)
    usr = Join.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('repeatpassword')
        if repeat_password == new_password:
            password_reset.user.password = new_password
            password_reset.user.save()
            password_reset.delete()
            return redirect(login)
    return render(request, 'reset_password_emp.html')


# def mess1(r):
#     l=alert.objects.all()
#     return render(r,'messages.html',{'l':l})
# def reply(r,em):
#     l=alert.objects.filter(id=em).first()
#     return render(r,"replymail.html",{'l':l})def
# def mess1(r):
#     l=Feedback.objects.all()
#     return render(r,'ad_feedback.html',{'l':l})
def reply(r,d):
    l=Feedback.objects.filter(id=d).first()
    return render(r,"replymail.html",{'l':l})
def replymail(r):
    if r.method=='POST':
        n=r.POST.get('message')
        e=r.POST.get('email')
        k=r.POST.get('sr')
        message='midhunsasi2001@gmail.com'
        try:
            send_mail('Employee Stock Messsage', f'{k},{n}','settings.EMAIL_HOST_USER',[e],fail_silently=False)
            return redirect(ad_feedback)
        except:
            ms = "NETWORK CONNECTION FAILED"
            return render(r, 'replymail.html',{"ms":ms})
    return render(r, 'replymail.html')
def deletemsg(r,d):
    l=Feedback.objects.get(id=d)
    l.delete()
    return redirect(ad_feedback)
# def deletemsg(r,em):
#     l=alert.objects.get(id=em)
#     l.delete()
#     return redirect(mess1)

# def stock_qut(request):
#     datas=products.objects.all()
#     d=orderitem.objects.all()
#     sum=0
#     for i in datas:
#         for j in d:
#             if i.pname==j.product.pname:
#                 sum=i.qut-j.quantity
#                 datas=products.objects.filter(pname=j.product.pname).update(qut=sum)
    
                
