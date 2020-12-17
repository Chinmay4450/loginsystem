
from rest_framework import serializers
from .models import hrAccounts  


class hrAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hrAccounts
        fields = ['name','username','password',]

    def create(self, validated_data):
            user = hrAccounts(name=validated_data['name'],username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            message="You have successfully register"
            return user
    
class gethrAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hrAccounts
        fields = ['id','username',]

    
            
              

