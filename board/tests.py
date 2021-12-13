from django.test import TestCase
from django.urls import reverse
from .models import Board, List, Card
import uuid

def create_board(name, idBoard):
    """
    Create a board
    """
    return Board.objects.get_or_create(name=name, idBoard=idBoard)

def create_list(name, listId, idBoard):
    """
    Create a list
    """
    return List.objects.create(name=name, listId=listId, idBoard=idBoard)

def create_card(name, cardId, listId, idBoard):
    """
    Create a card
    """
    return Card.objects.create(name=name, cardId=cardId, listId=listId, idBoard=idBoard)

class BoardViewTests(TestCase):

    def test_has_board(self):
        """
        Page has "Select board"
        """
        response = self.client.get(reverse('board:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Select Your board")

class BoardModelTests(TestCase):

    def test_board_create_model(self):
        """
        Board create has a name and id
        """

        idBoard = uuid.uuid4().hex
        boardName = 'Board Name'
        
        create_board(boardName, idBoard)
        board_obj = Board.objects.get(idBoard=idBoard)

        self.assertIs(board_obj.idBoard == idBoard, True)
        self.assertIs(board_obj.name == boardName, True)

class ListModelTests(TestCase):
    
    def test_list_create_model(self):
        """
        List create has a name, id and idBoard
        """

        idBoard = uuid.uuid4().hex
        listId = uuid.uuid4().hex
        cardId = uuid.uuid4().hex
        boardName = 'Board Name'
        listName = 'List Name'
        cardName = 'Card Name'

        create_board(boardName, idBoard)
        create_list(listName, listId, idBoard)
        create_card(cardName, cardId, listId, idBoard)

        list_obj = List.objects.get(idBoard=idBoard)

        self.assertIs(list_obj.listId == listId, True)
        self.assertIs(list_obj.idBoard == idBoard, True)
        self.assertIs(list_obj.name == listName, True)

class CardModelTests(TestCase):
    
    def test_card_create_model(self):
        """
        Card create has a name and id
        """

        idBoard = uuid.uuid4().hex
        listId = uuid.uuid4().hex
        cardId = uuid.uuid4().hex
        cardName = 'Card Name'
        
        create_card(cardName, cardId, listId, idBoard)

        card_obj = Card.objects.get(idBoard=idBoard)

        self.assertIs(card_obj.cardId == cardId, True)
        self.assertIs(card_obj.listId == listId, True)
        self.assertIs(card_obj.idBoard == idBoard, True)
        self.assertIs(card_obj.name == cardName, True)
