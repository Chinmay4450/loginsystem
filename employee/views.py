from .models import employee
from .serializers import employeeSerializer
from rest_framework import viewsets,status
from rest_framework import permissions
from rest_framework.response import Response


class empcreateView(viewsets.ModelViewSet):
    serializer_class = employeeSerializer
    queryset = employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        data = request.data
        data['hr_id'] = request.user.id
        serializer = employeeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
        return Response({'message': 'employee is created'}, status=status.HTTP_201_CREATED)  

