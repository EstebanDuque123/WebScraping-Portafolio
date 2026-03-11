from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import subprocess
import os
import csv
from django.http import FileResponse

def dashboard_view(request):
    # Verifica si hay un CSV de DEA para mostrarlo en el dashboard
    dea_file = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'fugitives_data.csv')
    dea_data = []

    if os.path.exists(dea_file):
        with open(dea_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                dea_data.append({'name': row[0], 'url': row[1]})

    context = {
        'dea_data': dea_data
    }
    return render(request, 'dashboard.html', context)

def ejecutar_scrape_ruia(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_ruia.py')
    try:
        subprocess.run(['python', path], check=True)
        messages.success(request, "✅ Script RUIA ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script RUIA.")
    return redirect('dashboard')

def ejecutar_scrape_sigep(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_sigep.py')
    try:
        subprocess.run(['python', path], check=True)
        messages.success(request, "✅ Script SIGEP ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script SIGEP.")
    return redirect('dashboard')

def ejecutar_scrape_dea(request):
    path = os.path.join(settings.BASE_DIR, 'webscraper', 'scrape_dea.py')
    try:
        subprocess.run(['python', path], check=True)
        messages.success(request, "✅ Script DEA ejecutado con éxito.")
    except subprocess.CalledProcessError:
        messages.error(request, "❌ Error al ejecutar el script DEA.")
    return redirect('dashboard')

def descargar_csv_dea(request):
    file_path = os.path.join(settings.BASE_DIR, 'webscraper', 'data', 'fugitives_data.csv')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='fugitives_data.csv')
    else:
        messages.error(request, "❌ El archivo DEA no fue encontrado.")
        return redirect('dashboard')