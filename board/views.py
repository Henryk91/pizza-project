from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from .models import Board, List

from dotenv import load_dotenv
load_dotenv()

import os
TRELLO_KEY = os.getenv('TRELLO_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')

def index(request):
    url = f'https://api.trello.com/1/members/me/boards?key={TRELLO_KEY}&token={TRELLO_TOKEN}'
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        Board.add_multiple_boards(data)
        return render(request, "board/index.html", {"boards": data})
    else:
        return render(request, "board/index.html")

def detail(request, pk):
    url = f"https://api.trello.com/1/boards/{pk}/lists?cards=all&key={TRELLO_KEY}&token={TRELLO_TOKEN}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        List.add_multiple_lists(data)

        board_obj = Board.objects.get(idBoard=pk)
        return render(request, "board/detail.html", {"detail": data, "board_obj":board_obj})
    else:
        return HttpResponseRedirect(f'/board/')

def newCard(request, pk):
    list_obj = List.objects.get(listId=pk)
    board_obj = Board.objects.get(idBoard=list_obj.idBoard)
    return render(request, "board/new-card.html", {"list_obj": list_obj, "board_obj":board_obj})

def create_card(request, list_id):
    url = f'https://api.trello.com/1/cards/?key={TRELLO_KEY}&token={TRELLO_TOKEN}'

    query = {
        'idList': list_id,
        'name': request.POST['new_card']
    }

    try:
        requests.request(
            "POST",
            url,
            headers={"Accept": "application/json"},
            params=query
        )
        list_obj = List.objects.get(listId=list_id)
        return HttpResponseRedirect(f'/board/{list_obj.idBoard}/details')
    except (KeyError):
        return render(request, 'board/new-card.html', {
            'error_message': "Something went wrong",
        })

