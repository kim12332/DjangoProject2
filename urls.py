from django.urls import path
from CompApp import views
from django.conf.urls import url,include
urlpatterns=[
     url('contact/',views.contact),
     url('category',views.category),
     #url('complain',views.complain_info_view),
     url('view-complain',views.viewComplain),
     url('new-complain',views.newComplain),
     url('^$',views.about),
     url('add',views.add),
     url('edit-complain',views.editComplain),
   url('edit',views.edit),
    url('delete-complain',views.deleteComplain),
     url('search-complain',views.searchComplain),
      url('search',views.search),
      #url('login',views.userLogin),
        #url('logout',views.userLogout),
]
