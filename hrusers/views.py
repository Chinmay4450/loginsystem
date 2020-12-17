from .models import hrAccounts
from .serializers import hrAccountsSerializer,gethrAccountsSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework import permissions

class RegisterView(viewsets.ModelViewSet):
    serializer_class = hrAccountsSerializer
    queryset = hrAccounts.objects.all()
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response({'Message': 'You have register successfully'},
                        status=status.HTTP_201_CREATED)


class gethrView(viewsets.ModelViewSet):
    serializer_class = gethrAccountsSerializer
    queryset = hrAccounts.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]

