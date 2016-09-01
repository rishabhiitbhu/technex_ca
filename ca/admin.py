from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin.options import ModelAdmin
from ca.models import *
from TechnexUser.models import UserStatus
#Define an inline admin descriptor for UserProfile model

class UserStatusInline(admin.StackedInline):
    model = UserStatus
    can_delete = False


class UserAdmin(UserAdmin):

    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)


    def college(obj):
        if obj.userstatus.is_ca == True:
            return "%s" % obj.caprofile.college
        else:
            return "%s" % obj.techprofile.college


    def mobile_number(obj):
        if obj.userstatus.is_ca == True:
            return "%s" % obj.caprofile.mobile_number
        else:
            return "%s" % obj.techprofile.mobile_number

    def CA(obj):
        return "%s" %obj.userstatus.is_ca

    def TechUser(obj):
        return "%s" %obj.userstatus.is_techuser

    name.short_description = 'Name'
    college.short_description = 'College'
    mobile_number.short_description = 'Mobile No.'

    inlines = (UserStatusInline, )
    list_display = ('email',name, college, mobile_number, CA , TechUser)

class MassNotificationAdmin(admin.ModelAdmin):
    list_display = ['mass_message']

class UserNotificationAdmin(admin.ModelAdmin):

    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    name.short_description = 'Name'
    list_display = [name,'message','mark_read']

class PosterAdmin(admin.ModelAdmin):

    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    name.short_description = 'Name'
    list_display = (name,'poster')


#Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Poster, PosterAdmin)
admin.site.register(CAProfile)
admin.site.register(User,UserAdmin)
admin.site.register(MassNotification, MassNotificationAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
# admin.site.register(TechnexUser,TechnexUserAdmin)
