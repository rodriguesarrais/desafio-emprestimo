from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# API
@csrf_exempt
def customer_loans(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # informacoes do cliente
        age = data.get('age')
        income = data.get('income')
        location = data.get('location')
        name = data.get('name')
        loans = []
        
        # verificacao das condicoes para cada tipo de emprestimo

        # emprestimo pessoal
        if income <= 3000:
            loans.append({
                "type": "PERSONAL",
                "interest_rate": 4
            })
        elif 3000 < income <= 5000 and age < 30 and location == "SP":
            loans.append({
                "type": "PERSONAL",
                "interest_rate": 4
            })
        
        # consignado
        if income >= 5000:
            loans.append({
                "type": "CONSIGNMENT",
                "interest_rate": 2
            })
        
        # garantia
        if income <= 3000:
            loans.append({
                "type": "GUARANTEED",
                "interest_rate": 3
            })
        elif 3000 < income <= 5000 and age < 30 and location == "SP":
            loans.append({
                "type": "GUARANTEED",
                "interest_rate": 3
            })
        
        response = {
            "customer": name,
            "loans": loans
        }
        
        return JsonResponse(response, status=200)
    
    return JsonResponse({"error": "Invalid request method."}, status=400)

# view do html
def customer_loans_form(request):
    if request.method == 'POST':
        # dados do formulário
        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        age = int(request.POST.get('age'))
        income = float(request.POST.get('income'))
        location = request.POST.get('location')

        # dados do cliente
        customer_data = {
            "name": name,
            "cpf": cpf,
            "age": age,
            "income": income,
            "location": location
        }

        response = requests.post('http://127.0.0.1:8000/customer-loans', json=customer_data)
        response_data = response.json()

        return render(request, 'loans/loan_form.html', {
            'loans': response_data.get('loans'),
            'customer': response_data.get('customer')
        })
    
    return render(request, 'loans/loan_form.html')
