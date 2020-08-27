from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from tutorials.models import Tutorial
from tutorials.models import Homehead
from tutorials.models import Children
from tutorials.models import Transaction
from tutorials.models import Exphead
from tutorials.models import Expdetail
from tutorials.models import Event

from tutorials.serializers import TutorialSerializer
from tutorials.serializers import HomeheadSerializer
from tutorials.serializers import ChildrenSerializer
from tutorials.serializers import TransactionSerializer
from tutorials.serializers import ExpheadSerializer
from tutorials.serializers import ExpdetailSerializer
from tutorials.serializers import EventSerializer
from rest_framework.decorators import api_view


@api_view ( ['GET', 'POST', 'DELETE'] )
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all ()

        title = request.GET.get ( 'name', None )
        if title is not None:
            tutorials = tutorials.filter ( title__icontains=title )

        tutorials_serializer = TutorialSerializer ( tutorials, many=True )
        return JsonResponse ( tutorials_serializer.data, safe=False )
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser ().parse ( request )
        tutorial_serializer = TutorialSerializer ( data=tutorial_data )
        if tutorial_serializer.is_valid ():
            tutorial_serializer.save ()
            return JsonResponse ( tutorial_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Tutorial.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Tutorials were deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def tutorial_detail(request, pk):
    try:
        tutorials = Tutorial.objects.get ( pk=pk )
    except Tutorial.DoesNotExist:
        return JsonResponse ( {'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer ( tutorials )
        return JsonResponse ( tutorial_serializer.data )

    elif request.method == 'PUT':
        tutorial_data = JSONParser ().parse ( request )
        tutorial_serializer = TutorialSerializer ( tutorials, data=tutorial_data )
        if tutorial_serializer.is_valid ():
            tutorial_serializer.save ()
            return JsonResponse ( tutorial_serializer.data )
        return JsonResponse ( tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        tutorials.delete ()
        return JsonResponse ( {'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter ( published=True )

    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer ( tutorials, many=True )
        return JsonResponse ( tutorials_serializer.data, safe=False )


@api_view ( ['GET', 'POST', 'DELETE'] )
def homehead_list(request):
    if request.method == 'GET':
        homeheads = Homehead.objects.all ()

        title = request.GET.get ( 'name', None )
        if title is not None:
            homeheads = homeheads.filter ( title__icontains=title )

        homeheads_serializer = HomeheadSerializer ( homeheads, many=True )
        return JsonResponse ( homeheads_serializer.data, safe=False )
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        homehead_data = JSONParser ().parse ( request )
        homehead_serializer = HomeheadSerializer ( data=homehead_data )
        if homehead_serializer.is_valid ():
            homehead_serializer.save ()
            return JsonResponse ( homehead_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( homehead_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Homehead.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Family Head were deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def homehead_detail(request, pk):
    try:
        homeheads = Homehead.objects.get ( pk=pk )
    except Homehead.DoesNotExist:
        return JsonResponse ( {'message': 'The Family Head does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        homehead_serializer = HomeheadSerializer ( homeheads )
        return JsonResponse ( homehead_serializer.data )

    elif request.method == 'PUT':
        homehead_data = JSONParser ().parse ( request )
        homehead_serializer = HomeheadSerializer ( homeheads, data=homehead_data )
        if homehead_serializer.is_valid ():
            homehead_serializer.save ()
            return JsonResponse ( homehead_serializer.data )
        return JsonResponse ( homehead_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        homeheads.delete ()
        return JsonResponse ( {'message': 'Family Head was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def homehead_list_published(request):
    homeheads = Homehead.objects.filter ( published=True )

    if request.method == 'GET':
        homeheads_serializer = HomeheadSerializer ( homeheads, many=True )
        return JsonResponse ( homeheads_serializer.data, safe=False )


@api_view ( ['GET', 'POST', 'DELETE'] )
def children_list(request):
    if request.method == 'GET':
        children = Children.objects.all ()

        title = request.GET.get ( 'name', None )
        if title is not None:
            children = children.filter ( title__icontains=title )
        children_serializer = ChildrenSerializer ( children, many=True )
        return JsonResponse ( children_serializer.data, safe=False )
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        children_data = JSONParser ().parse ( request )
        children_serializer = ChildrenSerializer ( data=children_data )
        if children_serializer.is_valid ():
            children_serializer.save ()
            return JsonResponse ( children_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( children_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Children.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Children were deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def children_detail(request, pk):
    try:
        children = Children.objects.get ( pk=pk )
    except Children.DoesNotExist:
        return JsonResponse ( {'message': 'The Children does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        children_serializer = ChildrenSerializer ( children )
        return JsonResponse ( children_serializer.data )

    elif request.method == 'PUT':
        children_data = JSONParser ().parse ( request )
        children_serializer = HomeheadSerializer ( children, data=children_data )
        if children_serializer.is_valid ():
            children_serializer.save ()
            return JsonResponse ( children_serializer.data )
        return JsonResponse ( children_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        children.delete ()
        return JsonResponse ( {'message': 'Children was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def children_list_published(request):
    children = Children.objects.filter ( published=True )

    if request.method == 'GET':
        children_serializer = ChildrenSerializer ( children, many=True )
        return JsonResponse ( children_serializer.data, safe=False )


# **********************

@api_view ( ['GET', 'POST', 'DELETE'] )
def transaction_list(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all ()

        title = request.GET.get ( 'name', None )
        if title is not None:
            transactions = transactions.filter ( title__icontains=title )

        transactions_serializer = TransactionSerializer ( transactions, many=True )
        return JsonResponse ( transactions_serializer.data, safe=False )
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        transaction_data = JSONParser ().parse ( request )
        transaction_serializer = TransactionSerializer ( data=transaction_data )
        if transaction_serializer.is_valid ():
            transaction_serializer.save ()
            return JsonResponse ( transaction_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Transaction.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Transaction were deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def transaction_detail(request, pk):
    try:
        transaction = Transaction.objects.get ( pk=pk )
    except Transaction.DoesNotExist:
        return JsonResponse ( {'message': 'The Transaction does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        transaction_serializer = TransactionSerializer ( transaction )
        return JsonResponse ( transaction_serializer.data )

    elif request.method == 'PUT':
        transaction_data = JSONParser ().parse ( request )
        transaction_serializer = TransactionSerializer ( transaction, data=transaction_data )
        if transaction_serializer.is_valid ():
            transaction_serializer.save ()
            return JsonResponse ( transaction_serializer.data )
        return JsonResponse ( transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        transaction.delete ()
        return JsonResponse ( {'message': 'Transaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def transaction_list_published(request):
    transactions = Transaction.objects.filter ( published=True )

    if request.method == 'GET':
        transaction_serializer = TransactionSerializer ( transactions, many=True )
        return JsonResponse ( transaction_serializer.data, safe=False )


# $$$$$$$$
@api_view ( ['GET', 'POST', 'DELETE'] )
def exphead_list(request):
    if request.method == 'GET':
        expheads = Exphead.objects.all ()

        title = request.GET.get ( 'exp_head', None )
        if title is not None:
            expheads = expheads.filter ( title__icontains=title )

        expheads_serializer = ExpheadSerializer ( expheads, many=True )
        return JsonResponse ( expheads_serializer.data, safe=False )
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        exphead_data = JSONParser ().parse ( request )
        exphead_serializer = ExpheadSerializer ( data=exphead_data )
        if exphead_serializer.is_valid ():
            exphead_serializer.save ()
            return JsonResponse ( exphead_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( exphead_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Exphead.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Expheads were deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def exphead_detail(request, pk):
    try:
        exphead = Exphead.objects.get ( pk=pk )
    except Exphead.DoesNotExist:
        return JsonResponse ( {'message': 'The Exphead does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        Exphead_serializer = ExpheadSerializer ( exphead )
        return JsonResponse ( Exphead_serializer.data )

    elif request.method == 'PUT':
        exphead_data = JSONParser ().parse ( request )
        exphead_serializer = ExpheadSerializer ( exphead, data=exphead_data )
        if exphead_serializer.is_valid ():
            exphead_serializer.save ()
            return JsonResponse ( exphead_serializer.data )
        return JsonResponse ( exphead_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        exphead.delete ()
        return JsonResponse ( {'message': 'Exphead was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def exphead_list_published(request):
    exphead = Exphead.objects.filter ( published=True )

    if request.method == 'GET':
        exphead_serializer = ExpheadSerializer ( exphead, many=True )
        return JsonResponse ( exphead_serializer.data, safe=False )


# $$$$$$$$
@api_view ( ['GET', 'POST', 'DELETE'] )
def expdetails_list(request):
    if request.method == 'GET':
        expdetails = Expdetail.objects.all ()

        title = request.GET.get ( 'exp_details', None )
        if title is not None:
            expdetails = expdetails.filter ( title__icontains=title )

        expdetails_serializer = ExpdetailSerializer ( expdetails, many=True )
        return JsonResponse ( expdetails_serializer.data, safe=False )
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        expdetails_data = JSONParser ().parse ( request )
        expdetails_serializer = ExpdetailSerializer ( data=expdetails_data )
        if expdetails_serializer.is_valid ():
            expdetails_serializer.save ()
            return JsonResponse ( expdetails_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( expdetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Expdetail.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Expdetails were deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def expdetails_detail(request, pk):
    try:
        expdetail = Expdetail.objects.get ( pk=pk )
    except Expdetail.DoesNotExist:
        return JsonResponse ( {'message': 'The Expdetails does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        Expdetail_serializer = ExpdetailSerializer ( expdetail )
        return JsonResponse ( Expdetail_serializer.data )

    elif request.method == 'PUT':
        expdetails_data = JSONParser ().parse ( request )
        expdetails_serializer = ExpdetailSerializer ( expdetail, data=expdetails_data )
        if expdetails_serializer.is_valid ():
            expdetails_serializer.save ()
            return JsonResponse ( expdetails_serializer.data )
        return JsonResponse ( expdetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        expdetail.delete ()
        return JsonResponse ( {'message': 'Expdetails was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def expdetails_list_published(request):
    expdetail = Expdetail.objects.filter ( published=True )

    if request.method == 'GET':
        expdetails_serializer = ExpdetailSerializer ( expdetail, many=True )
        return JsonResponse ( expdetails_serializer.data, safe=False )
#  ********************************************
@api_view ( ['GET', 'POST', 'DELETE'] )
def event_list(request):
    if request.method == 'GET':
        event = Event.objects.all ()

        title = request.GET.get ( 'event_venue', None )
        if title is not None:
            event = event.filter ( title__icontains=title )
        event_serializer = EventSerializer ( event, many=True )
        return JsonResponse ( event_serializer.data, safe=False )
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        event_data = JSONParser ().parse ( request )
        event_serializer = EventSerializer ( data=event_data )
        if event_serializer.is_valid ():
            event_serializer.save ()
            return JsonResponse ( event_serializer.data, status=status.HTTP_201_CREATED )
        return JsonResponse ( event_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        count = Event.objects.all ().delete ()
        return JsonResponse ( {'message': '{} Event was deleted successfully!'.format ( count[0] )},
                              status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET', 'PUT', 'DELETE'] )
def event_detail(request, pk):
    try:
        event = Event.objects.get ( pk=pk )
    except Event.DoesNotExist:
        return JsonResponse ( {'message': 'The Event does not exist'}, status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        event_serializer = EventSerializer ( event )
        return JsonResponse ( event_serializer.data )

    elif request.method == 'PUT':
        event_data = JSONParser ().parse ( request )
        event_serializer = EventSerializer ( event, data=event_data )
        if event_serializer.is_valid ():
            event_serializer.save ()
            return JsonResponse ( event_serializer.data )
        return JsonResponse ( event_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        event.delete ()
        return JsonResponse ( {'message': 'Event was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT )


@api_view ( ['GET'] )
def event_list_published(request):
    event = Event.objects.filter ( published=True )

    if request.method == 'GET':
        event_serializer = EventSerializer ( event, many=True )
        return JsonResponse ( event_serializer.data, safe=False )
