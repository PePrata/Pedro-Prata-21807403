from django.urls import path
from . import views

urlpatterns = [
    path('', views.tecnologias_view), 
    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('tecnologias/novo', views.novo_tecnologia_view, name="novo_tecnologias"),
    path('tecnologias/<int:tecnologia_id>/edita', views.edita_tecnologia_view, name="edita_tecnologia"),
    path('tecnologias/<int:tecnologia_id>/apaga', views.apaga_tecnologia_view,name="apaga_tecnologia"),

    path('licenciatura/', views.licenciatura_view, name="licenciatura"),
    
    path('docentes/', views.docentes_view, name="docentes"),

    path('cadeiras/', views.cadeiras_view, name="cadeiras"),
    
    path('formacoes/', views.formacoes_view, name="formacoes"),

    path('area_tematica/', views.areaTematica_view, name="area_tematica"),

    path('tfc/', views.tfcs_view, name = "tfcs"),
    
    
    path('projetos/', views.projetos_view, name="projetos"),
    path('projetos/novo', views.novo_projeto_view, name="novo_projeto"),
    path('projetos/<int:projeto_id>/edita', views.edita_projeto_view, name="edita_projeto"),
    path('projetos/<int:projeto_id>/apaga', views.apaga_projeto_view, name="apaga_projeto"),
]
