from django.contrib import admin

from .models import Loots, Ordering, FastOrdering
# Register your models here.

class LootsAdmin( admin.ModelAdmin ):
	list_display = ['name',
									'img',
									'size_loot',
									'descr',
									'price',
									'data']
	list_display_links = ['name', ]
	prepopulated_fields = {'slug': ('name', )}
	list_editable = ['price']

admin.site.register(Loots, LootsAdmin)
admin.site.register(Ordering)
admin.site.register(FastOrdering)