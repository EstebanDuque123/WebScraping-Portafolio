import subprocess
import os
import sys

from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import render

def dashboard_view(request):
    return render(request, "dashboard.html")


# ---------------------------
# Scrapers ejecutables
# ---------------------------
def ejecutar_scrape_europol(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_europol.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script Europol ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script Europol.")
    return redirect('dashboard')


def ejecutar_scrape_mwalemania(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_mwalemania.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script mwalemania ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script mwalemania.")
    return redirect('dashboard')


def ejecutar_scrape_mw_guatemala(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_mw_guatemala.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script Most Wanted Guatemala ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script Most Wanted Guatemala.")
    return redirect('dashboard')


def ejecutar_scrape_mwsalvador(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_mwsalvador.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script Most Wanted El Salvador ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script Most Wanted El Salvador.")
    return redirect('dashboard')


def ejecutar_scrape_argentina_profugos_de_la_justicia(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_argentina_profugos_de_la_justicia.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script Argentina prófugos de la justicia ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script Argentina prófugos de la justicia.")
    return redirect('dashboard')


def ejecutar_scrape_profugos_por_la_justicia_argentina(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_profugos_por_la_justicia_argentina.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script prófugos buscados por la justicia Argentina ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script prófugos buscados por la justicia Argentina.")
    return redirect('dashboard')


def ejecutar_scrape_listado_personas_desaparecidas(request):
    script_path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_listado_de_personas_desaparecidas_UBPD.py')
    try:
        subprocess.run([sys.executable, script_path], check=True)
        messages.success(request, "✅ Script listado personas desaparecidas ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar listado personas desaparecidas.")
    return redirect('dashboard')

# ---------------------------
# Descargar archivos CSV
# ---------------------------

def descargar_xlsx_europol(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'Europol.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='Europol.xlsx')
    else:
        raise Http404("Archivo Europol no encontrado.")


def descargar_xlsx_mwalemania(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'Mas_buscados_Alemania.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='Mas_buscados_Alemania.xlsx')
    else:
        raise Http404("Archivo mwalemania no encontrado.")


def descargar_xlsx_mw_guatemala(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'MWGuatemala.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='MWGuatemala.xlsx')
    else:
        raise Http404("Archivo MWGuatemala no encontrado.")


def descargar_xlsx_mwsalvador(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'MWSalvador.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='MWSalvador.xlsx')
    else:
        raise Http404("Archivo MWSalvador no encontrado.")


def descargar_xlsx_argentina_profugos_de_la_justicia(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'ARGENTINA_PROFUGOS_DE_LA_JUSTICIA.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='ARGENTINA_PROFUGOS_DE_LA_JUSTICIA.xlsx')
    else:
        raise Http404("Archivo Argentina prófugos no encontrado.")


def descargar_xlsx_profugos_por_la_justicia_argentina(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'PROFUGOS BUSCADOS POR LA JUSTICIA - ARGENTINA.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='PROFUGOS BUSCADOS POR LA JUSTICIA - ARGENTINA.xlsx')
    else:
        raise Http404("Archivo prófugos justicia Argentina no encontrado.")


def descargar_xlsx_listado_personas_desaparecidas(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'listado_personas_desaparecidas.xlsx')
    if os.path.exists(path):
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='listado_personas_desaparecidas.xlsx')
    else:
        raise Http404("Archivo listado personas desaparecidas no encontrado.")