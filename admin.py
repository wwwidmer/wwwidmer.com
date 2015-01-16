from django.contrib import admin
from wwidmer.models import page, blog, portfolio, project

# Register your models here.

class pageAdmin(admin.ModelAdmin):
	list_display=('title','id','onMenu')

class blogAdmin(admin.ModelAdmin):
	list_display=('title','pub_date')

class portAdmin(admin.ModelAdmin):
	list_display=('title','id')

class projAdmin(admin.ModelAdmin):
	list_display=('title','id')


admin.site.register(page, pageAdmin)
admin.site.register(blog, blogAdmin)
admin.site.register(portfolio, portAdmin)
admin.site.register(project,projAdmin)
