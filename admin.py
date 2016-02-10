from django.contrib import admin
from wwwidmer.models import Experience, TechnicalSkill


class technicalSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars')


class experienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company')


admin.site.register(TechnicalSkill, technicalSkillAdmin)
admin.site.register(Experience, experienceAdmin)

