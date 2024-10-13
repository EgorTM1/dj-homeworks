from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        bus_station_list = []

        for row in file_reader:
            bus_station_list.append(row)

    paginator = Paginator(bus_station_list, 5)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {'bus_stations': page.object_list, 'page': page, 'page_number': page_number}

    return render(request, 'stations/index.html', context)
