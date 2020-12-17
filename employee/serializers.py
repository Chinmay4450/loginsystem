
from rest_framework import serializers
from .models import employee  


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"
    
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['hr_id'] = instance.hr_id.username
    #     return ret

    
    


    
            
              

