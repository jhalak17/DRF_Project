from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModelAdmin(UserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'name','tc', 'is_admin')                  # This works as list_display
    list_filter = ('is_admin',)
    fieldsets = (                                                           # This will be displayed when we click on user
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','tc',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (                                                            
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','tc', 'password1', 'password2'),  # This will be asked when we click on add user icon in admin site
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)

