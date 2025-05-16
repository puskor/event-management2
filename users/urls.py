from django.urls import path
from users.views import sign_up,Sign_up_view,sign_in,Sign_in_view,sign_out,Sign_out_view,activate_user,admin_dashboard,assign_roll,create_group,group_list,Profile_view,Password_change,Password_change_done,Password_reset,Password_reset_confirm
# from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    
    # path("sign_up/",sign_up,name="sign_up"),
    path("sign_up/",Sign_up_view.as_view(),name="sign_up"),
    
    # path("sign_in/",sign_in,name="sign_in"),
    path("sign_in/",Sign_in_view.as_view(),name="sign_in"),
    
    path("sign_out/",sign_out,name="sign_out"),
    # path("sign_out/",Sign_out_view.as_view(),name="sign_out"),
    
    
    
    path("activate/<int:user_id>/<str:token>/",activate_user, name="activate_user"),
    path("admin_dashboard/",admin_dashboard,name="admin_dashboard"),
    path("<int:user_id>/assign_roll/",assign_roll,name="assign_roll"),
    path("create_group/",create_group,name="create_group"),
    path("group_list/",group_list,name="group_list"),
    path("profile_view/",Profile_view.as_view(),name="profile_view"),
    path("password_change/",Password_change.as_view(),name="password_change"),
    path("password_change_done/",Password_change_done.as_view(),name="password_change_done"),
    path("password_reset/",Password_reset.as_view(),name="password_reset"),
    path("password_reset_confirm/<uidb64>/<token>/",Password_reset_confirm.as_view(),name="password_reset_confirm")
]
