from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
urlpatterns = [
    
# ----------------Index---------------------------------------------

    path('',views.index),
    path('brand',views.brand),
    path('quick_view/<int:d>',views.quick_view),
    path('store',views.store),
    path('login',views.login),
    path('logout',views.logout),
    path('l1',views.l1),
    path('laptops',views.laptops),
    path('smartphones',views.Smartphones),
    path('cameras',views.Cameras),
    path('headphones',views.headphones),
    path('search_index',views.search_index),
    path('about',views.about),
    path('contact',views.contact),

    # admin---------------------------------------------------------------------

    path('admin',views.admin),
    path('ad_camera',views.ad_camera),
    path('ad_headphone',views.ad_headphone),
    path('ad_laptop',views.ad_laptop),
    path('ad_smartphone',views.ad_smartphone),
    path('cr',views.cr),
    path('ad_add_products',views.ad_add_products),
    path('lr',views.lr),
    path('ad_view_employe',views.ad_view_employe),
    path('admin_emp_edit/<int:d>',views.admin_emp_edit),
    path('admin_user_edit/<int:d>',views.admin_user_edit),
    path('ad_headphone_edit/<int:d>',views.ad_headphone_edit),
    path('ad_smartphone_edit/<int:d>',views.ad_smartphone_edit),
    path('ad_laptop_edit/<int:d>',views.ad_laptop_edit),
    path('ad_camera_edit/<int:d>',views.ad_camera_edit),
    path('ad_view_user',views.ad_view_user),
    path('ad_request',views.ad_request),
    path('delete2/<int:d>',views.delete2),
    path('delete/<int:d>',views.delete),
    path('laptop_delete/<int:d>',views.laptop_delete),
    path('camera_delete/<int:d>',views.camera_delete),
    path('smartphone_delete/<int:d>',views.smartphone_delete),
    path('headphone_delete/<int:d>',views.headphone_delete),
    path('toselling_delete/<int:d>',views.toselling_delete),
    path('ad_topselling_edit/<int:d>',views.ad_topselling_edit),
    path('ad_topselling',views.ad_topselling),
    path('ad_view_orders',views.ad_view_orders),
    path('statusup/<wal>',views.statusup,name="statusup"),
    path('tr',views.tr),
    path('sample',views.sample),
    path('accept/<int:d>',views.accept_request),
    path('ad_feedback',views.ad_feedback),
    path('search_admin',views.search_admin),
    path('ad_DeliveryDetails',views.ad_DeliveryDetails),
    path('ad_sigle_empdetails/<int:d>',views.ad_sigle_empdetails),
    path('ad_order_distribute',views.ad_order_distribute),
    path('ad_order_status/<int:d>',views.ad_order_status),
    path('ad_stoks',views.ad_stoks),
    path('ad_stock_update/<int:d>',views.ad_stock_update),
    path('alert_dele/<int:d>',views.alert_dele),
    path('ad_propicupdate/<int:d>',views.ad_propicupdate),
    path('replymaill/<int:d>',views.replymaill),

    #forgotpassword------------------------------------------------------------------
    path("forgot",views.forgot_password,name="forgot"),
    path("forgot_emp",views.forgot_password_emp,name="forgot_emp"),
    path("reset/<token>",views.reset_password,name="reset"),
    path("reset_emp/<token>",views.reset_password_emp,name="reset_emp"),
    path("reset/reset2/<token>",views.reset_password2,name="reset2"),
    path("reset_emp/reset3/<token>",views.reset_password3,name="reset3"),
    path('emailsent',views.emailsent),

   


    
    path('r1',views.r1),
    path('jr',views.jr),

    # user----------------------------------------------------------------------------

    path('user',views.user),
    path('myaccound',views.myaccound),
    path('user_laptop',views.user_laptop),
    path('user_camera',views.user_camera),
    path('user_smartphone',views.user_smartphone),
    path('user_headphone',views.user_headphone),
    path('u1',views.u1),
    path('registration',views.registration),
    path('join',views.join),
    path('accound_edit',views.accound_edit),
    path('Preview/<int:d>',views.Preview),
    path('feedback',views.feedback),
    path('servies',views.servies),
    path('search',views.search_index),
    path('user_brand',views.user_brand),
    path('search_user',views.search_user),



    # ------------------------Payments-----------------------------------

    path('checkout_single/<int:d>',views.checkout_single),
    path('single_pro_booking/<int:d>',views.single_pro_booking),
    path('checkout',views.checkout),
    path('Singl_booking_cansel/<int:d>',views.Singl_booking_cansel),
    path('place-order', views.placeorder, name='placeorder'),
    path('placeorder2',views.placeorder2,name='placeorder2'),
    path('proceed-to-pay', views.razorpaycheck, name='proceed-to-pay'),
    path('proceed-to-pay2',views.razorpaycheck2,name='proceed-to-pay2'),
    path('r6/<int:d>',views.r6),
    path('rs',views.rs),

#    Cart,CartUpdate,Booking,SingleBooking,---------------------------------

    path('update_cart',views.update_cart),
    path('minuscart/<int:de>',views.minuscart),
    path('pluscart/<int:de>',views.pluscart),
    path('myorder', views.orderss),
    path('oder_del/<int:d>',views.oder_del),
    path('viewcart',views.viewcart),
    path('add_to_cart/<int:d>',views.car),
    path('wishlist/<int:d>',views.wishlist),
    path('delete_w/<int:d>',views.delete_w),
    path('delete_c/<int:d>',views.delete_c),
    path('categories',views.categories),
    path('view_wisul',views.view_wisul),
    
    #employee----------------------------------------------------------------------

    path('employee',views.employee),
    path('emp_cash',views.emp_cash),
    path('emp_myoders',views.emp_myoders),
    path('volapcard',views.volapcard),
    path('emp_userdetails/<int:d>',views.emp_userdetails),
    path('emp_editprofile',views.emp_editprofile),
    path('emp_chnagepassword/<int:d>',views.emp_chnagepassword),
    path('stock_slert',views.stock_slert),
    path('emp_stockmessage',views.emp_stockmessage),

    #_________________MESSAGES__________________________

    # path('messeges',views.mess1,name='messages'),
    path('reply/<int:d>',views.reply,name='reply'),
    path('reply/replymail',views.replymail,name='replymail'),
    path('deletemsg/<int:d>',views.deletemsg,name='deletemsg'),
   ]

