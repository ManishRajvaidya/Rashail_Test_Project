from rest_framework import serializers

class DoseSerializer(serializers.Serializer):    
    dose = serializers.FloatField()
