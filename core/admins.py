from django.contrib import admin

admin.site.site_header = 'POS Admin'  # default: "Django Administration"
admin.site.index_title = ''  # default: "Site administration"
admin.site.site_title = 'Django POS Admin |'  # default: "Django site admin"
admin.site.site_url = '/'


class CoreTabularInlineAdmin(admin.TabularInline):
    exclude = ['is_removed', 'deleted_at']

    class Meta:
        abstract = True


class CoreModelAdmin(admin.ModelAdmin):
    exclude = ['is_removed', 'deleted_at']

    class Meta:
        abstract = True
