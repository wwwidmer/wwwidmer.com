from django.contrib import admin
from wwwidmer.models import page, blog, portfolio, project, index_image

# Register your models here.

class pageAdmin(admin.ModelAdmin):
	list_display=('title','id','onMenu')

class blogAdmin(admin.ModelAdmin):
	list_display=('title','pub_date')

class portAdmin(admin.ModelAdmin):
	list_display=('title','id')

class imageAdmin(admin.ModelAdmin):
    list_display = ('id','image')


admin.site.register(page, pageAdmin)
admin.site.register(blog, blogAdmin)
admin.site.register(portfolio, portAdmin)
admin.site.register(index_image, imageAdmin)