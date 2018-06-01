from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q

from .models import Passenger
# Create your views here.

def home(request):
	render(request, 'passengers/home.html')

def embarkation(request):
    return render(request, 'passengers/embarkation.html')

def embarkation_data(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')
    #print(dataset)

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]
       
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic\'s Passengers By Embarkation Port'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }
    
    #print(list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset)))
    # [{'name': 'Cherbourg', 'y': 270}, {'name': 'Queenstown', 'y': 123}, {'name': 'Southampton', 'y': 914}]
    return JsonResponse(chart)

def survivor(request):
    return render(request, 'passengers/survivor.html')

def survivor_data(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)), not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    #print(dataset)
    #print (list(map(lambda row : {'ticket_class': row['ticket_class'] }, dataset )) )
	# [
	# 	{'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
	# 	{'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
	# 	{'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
	# ]

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis' :{'categories': list(map(lambda row : 'Class ' + str(row['ticket_class']), dataset )) },
        'series': [
    				{
			            'name': 'Survived',
			            'data': list(map(lambda row: {'name': 'survived_count', 'y': row['survived_count']}, dataset)),
			            'color': 'green'},
		            {
			            'name': 'Not Survived',
			            'data': list(map(lambda row: {'name': 'not_survived_count', 'y': row['not_survived_count']}, dataset)),
			            'color': 'red'
           	 		}]
    		} 
    return JsonResponse(chart)




















