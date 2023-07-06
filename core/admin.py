from django.contrib import admin

from core.models import Autor, Categoria, Compra, Editora, ItensCompra, Livro


# Register your models here.
class ItensInline(admin.TabularInline):
    model = ItensCompra


class MyAdminSite(admin.AdminSite, admin.ModelAdmin):
    site_title = 'Livraria DRF'
    site_header = 'Livraria'


admin_site = MyAdminSite()

admin_site.register(Autor)
admin_site.register(Categoria)
admin_site.register(Editora)
admin_site.register(Livro)
admin_site.register(Compra, inlines=(ItensInline,))
