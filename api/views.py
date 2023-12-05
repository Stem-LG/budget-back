from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import earningsSerializer, eventSerializer, eventsSerializer, expensesSerializer, fundsSerializer
from db.models import Earning, Event, Expense, Fund
from django.db.models import Sum
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from users.serializers import UserSerializer


#users

@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def usersView(request):
    users = User.objects.all()

    serializedUsers = UserSerializer(users, many=True).data

    return Response(serializedUsers)

#dashboard

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def statsView(request):
    #returns total funds, expenses, earnings
    funds_sum = Fund.objects.aggregate(Sum("amount"))['amount__sum']
    expenses_sum = Expense.objects.aggregate(Sum("amount"))['amount__sum']
    Earnings_sum = Earning.objects.aggregate(Sum("amount"))['amount__sum']
    stats = {
        "funds":funds_sum or 0,
        "expenses":expenses_sum or 0,
        "earnings":Earnings_sum or 0
    }


    return Response(stats)

#events
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eventsView(request):
    match request.method:
        case "GET":
            events = Event.objects.all()

            serializedEvents = eventsSerializer(events, many=True).data

            return Response(serializedEvents)
        case "POST":
            event = Event(
                name = request.data['name'],
                date = request.data['date'],
                location = request.data['location'],
                description = request.data['description'],
                manager = User.objects.get(pk=request.data['manager'])
            )

            event.save()

            serializedEvent = eventSerializer(event).data

            return Response(serializedEvent)


#event

@api_view(['GET','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eventView(request, id):

    match request.method:
        case "GET":
            event = Event.objects.get(id=id)

            funds_sum = Fund.objects.select_related('event').filter(event=id).aggregate(Sum("amount"))['amount__sum']
            expenses_sum = Expense.objects.select_related('event').filter(event=id).aggregate(Sum("amount"))['amount__sum']
            Earnings_sum = Earning.objects.select_related('event').filter(event=id).aggregate(Sum("amount"))['amount__sum']

            serializedEvent = eventSerializer(event).data
            serializedEvent["funds"] = funds_sum or 0
            serializedEvent["expenses"] = expenses_sum or 0
            serializedEvent["earnings"] = Earnings_sum or 0

            return Response(serializedEvent)
        
        case "PUT":
            event = Event.objects.get(id=id)
            event.name = request.data['name']
            event.date = request.data['date']
            event.location = request.data['location']
            event.description = request.data['description']
            event.manager = User.objects.get(pk=request.data['manager'])

            event.save()

            return Response(eventSerializer(event).data)

        case "DELETE":
            event = Event.objects.get(id=id)

            event.delete()

            return Response({"message":"Event deleted"})
    

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fundsView(request, event_id):

    match request.method:
        case 'GET':
            funds = Fund.objects.filter(event=event_id).all()

            serializedFund = fundsSerializer(funds, many=True).data

            return Response(serializedFund)
        case 'POST':

            fund = Fund(
                title = request.data['title'],
                date = request.data['date'],
                description = request.data['description'],
                amount = request.data['amount'],
                source = User.objects.get(pk=request.data['source']),
                returnable = request.data['returnable'] or False,
                event = Event.objects.get(pk=event_id)
            )

            fund.save()

            serializedFund = fundsSerializer(fund).data

            return Response(serializedFund)

@api_view(['DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fundView(request, id):
    match request.method:
        case 'PUT':
            fund = Fund.objects.get(id=id)
            fund.title = request.data['title']
            fund.date = request.data['date']
            fund.description = request.data['description']
            fund.amount = request.data['amount']
            fund.source = User.objects.get(pk=request.data['source'])
            fund.returnable = request.data['returnable'] or False

            fund.save()

            return Response(fundsSerializer(fund).data)
        case 'DELETE':
            fund = Fund.objects.get(id=id)

            fund.delete()

            return Response({"message":"Fund deleted"})
 

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def expensesView(request, event_id):

    match request.method:
        case 'GET':
            expenses = Expense.objects.filter(event=event_id).all()

            serializedExpense = expensesSerializer(expenses, many=True).data

            return Response(serializedExpense)
        case 'POST':
            expense = Expense(
                item = request.data['item'],
                date = request.data['date'],
                description = request.data['description'],
                amount = request.data['amount'],
                invoice = request.data['invoice'],
                spender = User.objects.get(pk=request.data['spender']),
                event = Event.objects.get(pk=event_id)
            )

            expense.save()

            serializedExpense = expensesSerializer(expense).data

            return Response(serializedExpense)
        
@api_view(['DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def expenseView(request, id):
    match request.method:
        case 'PUT':
            expense = Expense.objects.get(id=id)
            expense.item = request.data['item']
            expense.date = request.data['date']
            expense.description = request.data['description']
            expense.amount = request.data['amount']
            expense.invoice = request.data['invoice']
            expense.spender = User.objects.get(pk=request.data['spender'])

            expense.save()

            return Response(expensesSerializer(expense).data)
        
        case 'DELETE':
            expense = Expense.objects.get(id=id)

            expense.delete()

            return Response({"message":"Expense deleted"})

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def earningsView(request, event_id):

    match request.method:
        case 'GET':
            earnings = Earning.objects.filter(event=event_id).all()

            serializedEarnings = earningsSerializer(earnings, many=True).data

            return Response(serializedEarnings)
        case 'POST':
            earning = Earning(
                item = request.data['item'],
                date = request.data['date'],
                description = request.data['description'],
                amount = request.data['amount'],
                seller = User.objects.get(pk=request.data['seller']),
                event = Event.objects.get(pk=event_id)
            )

            earning.save()

            serializedEarning = earningsSerializer(earning).data

            return Response(serializedEarning)

@api_view(['DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def earningView(request, id):
    match request.method:
        case 'PUT':
            earning = Earning.objects.get(id=id)
            earning.item = request.data['item']
            earning.date = request.data['date']
            earning.description = request.data['description']
            earning.amount = request.data['amount']
            earning.seller = User.objects.get(pk=request.data['seller'])

            earning.save()

            return Response(earningsSerializer(earning).data)
        
        case 'DELETE':
            earning = Earning.objects.get(id=id)

            earning.delete()

            return Response({"message":"Earning deleted"})
