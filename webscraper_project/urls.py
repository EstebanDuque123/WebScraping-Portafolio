# webscraper_project/urls.py
from django.contrib import admin
from django.urls import path, include
from webscraper import views as scraper_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scraper_views.dashboard_view, name='dashboard'),

    # Ejecutar scrapers
    path('ejecutar/mwalemania/', scraper_views.ejecutar_scrape_mwalemania, name='ejecutar_mwalemania'),
    path('ejecutar/argentina_profugos_de_la_justicia/', scraper_views.ejecutar_scrape_argentina_profugos_de_la_justicia, name='ejecutar_argentina_profugos_de_la_justicia'),
    path('ejecutar/europol/', scraper_views.ejecutar_scrape_europol, name='ejecutar_europol'),
    path('ejecutar/mw_guatemala/', scraper_views.ejecutar_scrape_mw_guatemala, name='ejecutar_mw_guatemala'),
    path('ejecutar/profugos_por_la_justicia_argentina/', scraper_views.ejecutar_scrape_profugos_por_la_justicia_argentina, name='ejecutar_scrape_profugos_por_la_justicia_argentina'),
    path('ejecutar/listado_personas_desaparecidas/', scraper_views.ejecutar_scrape_listado_personas_desaparecidas, name='ejecutar_scrape_listado_personas_desaparecidas'),
    path('ejecutar/mwsalvador/', scraper_views.ejecutar_scrape_mwsalvador, name='ejecutar_mwsalvador'),

    # Descargar CSVs
    path('descargar/mwalemania/', scraper_views.descargar_xlsx_mwalemania, name='descargar_mwalemania'),
    path('descargar/argentina_profugos_de_la_justicia/', scraper_views.descargar_xlsx_argentina_profugos_de_la_justicia, name='descargar_argentina_profugos_de_la_justicia'),
    path('descargar/europol/', scraper_views.descargar_xlsx_europol, name='descargar_europol'),
    path('descargar/mw_guatemala/', scraper_views.descargar_xlsx_mw_guatemala, name='descargar_mw_guatemala'),
    path('descargar/profugos_por_la_justicia_argentina/', scraper_views.descargar_xlsx_profugos_por_la_justicia_argentina, name='descargar_xlsx_profugos_por_la_justicia_argentina'),
    path('descargar/listado_personas_desaparecidas/', scraper_views.descargar_xlsx_listado_personas_desaparecidas, name='descargar_xlsx_listado_personas_desaparecidas'),
    path('descargar/mwsalvador/', scraper_views.descargar_xlsx_mwsalvador, name='descargar_mwsalvador'),
]
