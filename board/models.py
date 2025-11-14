from django.db import models

class List(models.Model):
    name = models.CharField(max_length=100)
    listId = models.CharField(primary_key=True, unique=True, max_length=100)
    idBoard = models.CharField(max_length=100)

    def add_multiple_lists(lists):

        for item in lists:
            try:
                if item['cards']:
                    Card.add_multiple_cards(item['cards'])
                item = List.objects.get_or_create(
                    name= item['name'],
                    listId= item['id'],
                    idBoard= item['idBoard'])
                
            except Exception as e:
                print('Add Multiple lists Error', e)
        return lists

class Board(models.Model):
    name = models.CharField(max_length=100)
    idBoard = models.CharField(primary_key=True, unique=True, max_length=100)

    def add_multiple_boards(boards):
        for item in boards:
            try:
                item = Board.objects.get_or_create(
                    name= item['name'],
                    idBoard= item['id'])
            except Exception as e:
                print('Add Multiple Boards Error', e)
        return boards
    
    def get_name(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=100)
    cardId = models.CharField(primary_key=True, unique=True, max_length=100)
    listId = models.CharField(max_length=100)
    idBoard = models.CharField(max_length=100)

    def add_multiple_cards(boards):
        for item in boards:
            try:
                item = Card.objects.get_or_create(
                    name= item['name'],
                    cardId= item['id'],
                    listId= item['idList'],
                    idBoard= item['idBoard'],
                    )
            except Exception as e:
                print('Add Multiple card Error', e)
        return boards
