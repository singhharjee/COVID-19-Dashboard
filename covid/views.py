from django.shortcuts import render
from django.views import View
import json
import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-key': "24b00017e6msh677a490cda6e420p13922ajsn39e33329a18c",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()
# print(response)


def Index(request):
    country_list = []
    noofcountries = 220
    for country in range(noofcountries):
        country_list.append(
            response['countries_stat'][country]['country_name'])

    if request.method == "POST":
        selected_country = request.POST.get('countryname')
        # print(selected_country)
        for data in range(noofcountries):
            if selected_country == response['countries_stat'][data]['country_name']:
                total_cases = response['countries_stat'][data]['cases']
                # print(response['countries_stat'][data]['cases'])
                total_deaths = response['countries_stat'][data]['deaths']
                total_recovered = response['countries_stat'][data]['total_recovered']
                new_deaths = response['countries_stat'][data]['new_deaths']
                new_cases = response['countries_stat'][data]['new_cases']
                serious_critical = response['countries_stat'][data]['serious_critical']
                active_cases = response['countries_stat'][data]['active_cases']
                context = {'selectedcountry': selected_country, 'country_list': country_list, 'total_cases': total_cases, 'total_deaths': total_deaths, 'total_recovered': total_recovered,
                           'new_deaths': new_deaths, 'new_cases': new_cases, 'serious_critical': serious_critical, 'active_cases': active_cases}
                return render(request, 'covid/index.html', context)

    context = {'country_list': country_list}
    return render(request, 'covid/index.html', context)
