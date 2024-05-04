from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    def add_user(request):
        if request.method == 'POST':
            uname = request.POST.get('name')
            uemail = request.POST.get('email')
            umobile = request.POST.get('mobile')
            models.User.objects.create(name=uname, email=uemail, mobile=umobile)
            return redirect('index')
        return render(request, 'useradd.html')


class LoanViewSet(viewsets.ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def part_payment(self, request, pk=None):
        loan = self.get_object()
        amount_to_pay = request.data.get('amount', 0)

        if amount_to_pay <= 0:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        if amount_to_pay > loan.amount:
            return Response({'error': 'Amount exceeds loan balance'}, status=status.HTTP_400_BAD_REQUEST)

        loan.amount -= amount_to_pay
        loan_term = loan.term
        loan_term -= 1
        loan.save()

        # Update repayment amounts
        repayment_amount = loan.amount / loan_term

        for i in range(1, loan_term + 1):
            models.Repayment.objects.create(loan=loan, amount=repayment_amount, date=i*7, status='PENDING')

        return Response({'message': 'Part payment successful'}, status=status.HTTP_200_OK)


class RepaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Repayment.objects.all()
    serializer_class = serializers.RepaymentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def part_payment(self, request, pk=None):
        repayment = self.get_object()
        amount_to_pay = request.data.get('amount', 0)

        if amount_to_pay <= 0:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        if amount_to_pay > repayment.amount:
            return Response({'error': 'Amount exceeds repayment balance'}, status=status.HTTP_400_BAD_REQUEST)

        repayment.amount -= amount_to_pay
        repayment.save()

        return Response({'message': 'Part payment successful'}, status=status.HTTP_200_OK)


def loan_list(request):
    return render(request, 'loan_list.html')

def add_repayment(request):
    return render(request, 'repayment_add.html')

def index(request):
        return render(request, 'index.html')


    
