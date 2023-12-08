from django.urls import path
from .views import home,contact
from .views import index,LoginPage,login_post,logout
from .views import index_kurir,tambah_kurir,post_kurir,update_kurir,post_update_kurir,delete_kurir
from .views import index_barang,tambah_barang,post_barang,update_barang,post_update_barang,delete_barang
from .views import index_task,tambah_task,post_task,update_task,post_update_task,delete_task
# from .views import change_password

urlpatterns = [
    # path('ubah-password/', ubah_password, name='ubah_password'),

    path('home', home, name='home'),
    path('contact', contact, name='contact'),


    path('', LoginPage, name='LoginPage'),
    # path('admin/signup', admin_signup, name='admin_signup'),
    path('login_post', login_post, name='loginPost'),
    path('logout', logout, name='logout'),
    path('index',index, name='index'),
    
    #CRUD Kurir
    path('index_kurir/', index_kurir, name='indexKurir'),
    path('tambah_kurir/', tambah_kurir, name='tambahKurir'),
    path('post_kurir', post_kurir, name='postKurir'), 
    path('update_kurir/<str:id_kurir>/', update_kurir, name='updateKurir'),
    path('post_update_kurir/', post_update_kurir, name='post_updateKurir'),
    path('delete_kurir/<str:id_kurir>/', delete_kurir, name='deleteKurir'),

    #CRUD Barang
    path('index_barang/', index_barang, name='indexBarang'),
    path('tambah_barang/', tambah_barang, name='tambahBarang'),
    path('post_barang', post_barang, name='postBarang'),
    path('update_barang/<str:id_barang>/', update_barang, name='updateBarang'),
    path('post_update_barang/', post_update_barang, name='post_updateBarang'),
    path('delete_barang/<str:id_barang>/', delete_barang, name='deleteBarang'),
    
    #CRUD Task
    path('index_task/', index_task, name='indexTask'),
    path('tambah_task/', tambah_task, name='tambahTask'),
    path('post_task', post_task, name='postTask'),
    path('update_task/<str:id_task>/', update_task, name='updateTask'),
    path('post_update_task/', post_update_task, name='post_updateTask'),
    path('delete_task/<str:id_task>/', delete_task, name='deleteTask'),
    

]
