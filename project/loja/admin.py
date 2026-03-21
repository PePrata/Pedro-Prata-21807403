from django.contrib import admin

from .models import Categoria,Produto,Cliente,Pedido,LinhaPedido

# Register your models here.

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'lista_produtos')
    search_fields = ('nome',)
    inlines = [ProdutoInline]  # Create produtos directly inside Categoria

    def lista_produtos(self, obj):
        produtos = obj.produto_set.all()
        if not produtos.exists():
            return "Sem produtos"
        return ", ".join(p.nome for p in produtos)
    lista_produtos.short_description = 'Produtos'

admin.site.register(Categoria, CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome',)

admin.site.register(Produto, ProdutoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'lista_pedidos')
    search_fields = ('nome', 'endereco')

    def lista_pedidos(self, obj):
        pedidos = obj.pedido_set.all()
        if not pedidos.exists():
            return "Sem pedidos"
        return ", ".join(str(p.id) for p in pedidos)
    lista_pedidos.short_description = 'Pedidos'

admin.site.register(Cliente, ClienteAdmin)

class LinhaPedidoInline(admin.TabularInline):
    model = LinhaPedido
    extra = 1  # Add products to an order directly inside Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data', 'lista_produtos')
    list_filter = ('cliente', 'data')
    search_fields = ('cliente__nome',)
    readonly_fields = ('data',)  # auto_now_add must be readonly
    inlines = [LinhaPedidoInline]  # Add linha pedidos inside Pedido

    def lista_produtos(self, obj):
        linhas = obj.linhapedido_set.all()
        if not linhas.exists():
            return "Sem produtos"
        return ", ".join(f'{l.quantidade}x {l.produto.nome}' for l in linhas)
    lista_produtos.short_description = 'Produtos'

admin.site.register(Pedido, PedidoAdmin)

class LinhaPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'produto', 'quantidade')
    list_filter = ('produto',)
    search_fields = ('pedido__cliente__nome', 'produto__nome')

admin.site.register(LinhaPedido, LinhaPedidoAdmin)