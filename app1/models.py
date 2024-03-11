from django.db import models

# Create your models here.
class reg(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    photo=models.FileField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    address=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.firstname
class products(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    mi=models.FileField()
    fi=models.FileField()
    sm=models.FileField()
    tm=models.FileField()
    color=models.CharField(max_length=20)
    dis=models.CharField(max_length=500)
    qut=models.IntegerField()
    discound=models.IntegerField()
    brand=models.CharField(max_length=100)
    f1=models.CharField(max_length=100)
    f2=models.CharField(max_length=100)
    f3=models.CharField(max_length=100)
    f4=models.CharField(max_length=100)
    category=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.pname
class Join(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    location=models.CharField(max_length=50)
    photo=models.FileField()
    license=models.FileField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    biodata=models.FileField()
    accoundnumber=models.IntegerField()
    status=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.firstname
class user_details(models.Model):
    user_details=models.ForeignKey(reg,on_delete=models.CASCADE)

# class booking(models.Model):
#     user_details=models.ForeignKey(reg,on_delete=models.CASCADE)
#     item_details=models.ForeignKey(products,on_delete=models.CASCADE)
#     date=models.CharField(max_length=30)
#     quantity=models.IntegerField()
#     item_price=models.IntegerField()
#     total_price=models.IntegerField()

class c_rt(models.Model):
    user_details=models.ForeignKey(reg,on_delete=models.CASCADE)
    item_details=models.ForeignKey(products,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)
    date=models.CharField(max_length=30)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    tprice=models.IntegerField()
    delivered=models.BooleanField(default=False)


class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    text=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class preview(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    text=models.CharField(max_length=200)
    date=models.CharField(max_length=30)
    star=models.IntegerField()
    kk=models.IntegerField()
    photo=models.FileField()
    def __str__(self) -> str:
        return self.name
class Wishlist(models.Model):
    user_details=models.ForeignKey(reg,on_delete=models.CASCADE)
    item_details=models.ForeignKey(products,on_delete=models.CASCADE)
    date=models.CharField(max_length=30)
    status=models.IntegerField(default=0)

class order(models.Model):
    user = models.ForeignKey(reg, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    orderstatus = (
        ('Order Received','Order Received'),
        ('Order Processed','Order Processed'),
        ('Order Dispatched','Order Dispatched'),
        ('Pending','Pending'),
        ('Out for shipping','Out for shipping'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status = models.CharField(max_length=150,choices=orderstatus, default='pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return f'{self.tracking_no}'

class profile(models.Model):
    user = models.OneToOneField(reg,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.user.username}'

class orderitem(models.Model):
    orderdet = models.ForeignKey(order,on_delete=models.CASCADE)
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    status=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.orderdet}'

class PasswordReset(models.Model):
    user = models.ForeignKey(reg, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
class PasswordResetemp(models.Model):
    user = models.ForeignKey(Join, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
class profilepic(models.Model):
    user = models.OneToOneField(Join,on_delete=models.CASCADE)
    propic = models.FileField(upload_to='images/profilepic')

class profilepic_user(models.Model):
    user = models.OneToOneField(reg,on_delete=models.CASCADE)
    propic = models.FileField(upload_to='images/profilepic')

class product_pic(models.Model):
    user = models.OneToOneField(products,on_delete=models.CASCADE)
    propic1 = models.FileField(upload_to='images/profilepic')
    propic2 = models.FileField(upload_to='images/profilepic')
    propic3 = models.FileField(upload_to='images/profilepic')
    propic4 = models.FileField(upload_to='images/profilepic')
   
class SigleBooking(models.Model):
    user_details=models.ForeignKey(reg,on_delete=models.CASCADE)
    item_details=models.ForeignKey(products,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)
    date=models.CharField(max_length=30)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    tprice=models.IntegerField()
    delivered=models.BooleanField(default=False)

class alert(models.Model):
    item=models.CharField(max_length=100)
    messge=models.CharField(max_length=200)
    

