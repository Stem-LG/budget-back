from rest_framework import serializers

from db.models import Earning, Event, Expense, Fund


class eventsSerializer(serializers.ModelSerializer):
    manager = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id","name","description","manager"]

    def get_manager(self, obj):
        return {"id":obj.manager.id,"name":obj.manager.username}
    
    
class eventSerializer(serializers.ModelSerializer):
    manager = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id","name","date","location","description","manager"]
    
    def get_manager(self, obj):
        return {"id":obj.manager.id, "name": obj.manager.username}
    
    
class fundsSerializer(serializers.ModelSerializer):
    source = serializers.SerializerMethodField()

    class Meta:
        model = Fund
        fields = ["id","title","date","description","amount","source","returnable"]

    def get_source(self, obj):
        return {"id":obj.source.id,"name":obj.source.username}
    
class expensesSerializer(serializers.ModelSerializer):
    spender = serializers.SerializerMethodField()
    class Meta:
        model = Expense
        fields = ["id","item","date","description","amount","invoice","spender"]
    def get_spender(self,obj):
        return {"id":obj.spender.id,"name":obj.spender.username}

class earningsSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    class Meta:
        model= Earning
        fields = ["id","item","date","description","amount","seller"]
    def get_seller(self, obj):
        return {"id":obj.seller.id,"name":obj.seller.username}
