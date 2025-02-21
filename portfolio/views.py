from django.shortcuts import render
import random
from datetime import datetime, timedelta

def index(request):
    return render(request, 'pages/portfolio.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def portfoliopage(request):  
    return render(request, 'pages/portfoliopage.html')

def activity2_dashboard(request):  
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": 12450},
    ]
    return render(request, 'pages/activity2_dashboard.html', {'data': data})


def reports(request):
    orders = [
        {"id": 1, "customer": "Juan Dela Cruz", "product": "Paracetamol", "quantity": 2, "total_price": "₱50", "date": "2025-02-19"},
        {"id": 2, "customer": "Maria Santos", "product": "Amoxicillin", "quantity": 1, "total_price": "₱50", "date": "2025-02-18"},
        {"id": 3, "customer": "Jose Rizal", "product": "Cetirizine", "quantity": 3, "total_price": "₱90", "date": "2025-02-17"},
        {"id": 4, "customer": "Andres Bonifacio", "product": "Ibuprofen", "quantity": 1, "total_price": "₱40", "date": "2025-02-16"},
        {"id": 5, "customer": "Melchora Aquino", "product": "Mefenamic Acid", "quantity": 2, "total_price": "₱70", "date": "2025-02-15"},
    ]

    filipino_names = [
        "Emilio Aguinaldo", "Gabriela Silang", "Marcelo Del Pilar", "Diego Silang", "Tandang Sora", 
        "Apolinario Mabini", "Antonio Luna", "Gregorio Del Pilar", "Manuel Quezon", "Sergio Osmeña",
        "Lapu-Lapu", "Rajah Humabon", "Corazon Aquino", "Benigno Aquino", "Josefa Llanes Escoda",
        "Macario Sakay", "Ramon Magsaysay", "Carlos P. Garcia", "Elpidio Quirino", "Mariano Ponce",
        "Felipe Agoncillo", "Julian Felipe", "Francisco Balagtas", "Leona Florentino", "Ishmael Bernal",
        "Fernando Poe Jr.", "Lino Brocka", "Manuel Roxas", "Pedro Paterno", "Lope K. Santos",
        "Juan Luna", "Felix Hidalgo", "Heneral Luna", "Jose Abad Santos", "Simeon Ola",
        "Vicente Lim", "Gliceria Marella de Villavicencio", "Anastacio Caedo", "Rodolfo Biazon", "Arturo Tolentino",
        "Paeng Nepomuceno", "Manny Pacquiao", "Efren Bata Reyes", "Lea Salonga", "Dingdong Dantes",
        "Angel Locsin", "Sarah Geronimo", "Catriona Gray", "Pia Wurtzbach", "Megan Young",
        "Dona Aurora", "Fidel V. Ramos", "Gloria Macapagal Arroyo", "Sotero Laurel", "Francisco Dagohoy",
        "Angelica Panganiban", "Daniel Padilla", "Kathryn Bernardo", "Liza Soberano", "Enrique Gil",
        "Jericho Rosales", "John Lloyd Cruz", "Tirso Cruz", "Boy Abunda", "Judy Ann Santos",
        "Rica Peralejo", "Charo Santos-Concio", "Gina Lopez", "Jessica Soho", "Mel Tiangco",
        "Kris Aquino", "Korina Sanchez", "Noli De Castro", "Ted Failon", "Atom Araullo"
    ]

    medicines = [
        {"name": "Paracetamol", "price": 25, "max_quantity": 100},
        {"name": "Amoxicillin", "price": 50, "max_quantity": 50},
        {"name": "Cetirizine", "price": 30, "max_quantity": 75},
        {"name": "Ibuprofen", "price": 40, "max_quantity": 30},
        {"name": "Mefenamic Acid", "price": 35, "max_quantity": 20},
    ]

    # Generate the rest of the 145 reports
    for i in range(6, 151):
        customer_name = filipino_names[(i - 6) % len(filipino_names)]
        medicine = medicines[i % len(medicines)]
        quantity = min((i % 5) + 1, medicine["max_quantity"])  # Ensures quantity does not exceed stock
        total_price = quantity * medicine["price"]
        date = f"2025-02-{(20 - (i % 20)):02d}"  # Distributes dates within Feb 2025

        orders.append({
            "id": i,
            "customer": customer_name,
            "product": medicine["name"],
            "quantity": quantity,
            "total_price": f"₱{total_price}",
            "date": date
        })

    return render(request, "pages/reports.html", {"orders": orders})

def inventory(request):
    items = [
        {"id": 1, "name": "Paracetamol", "category": "Pain Reliever", "quantity": 100, "price": 25, "status": "In Stock"},
        {"id": 2, "name": "Amoxicillin", "category": "Antibiotic", "quantity": 50, "price": 50, "status": "In Stock"},
        {"id": 3, "name": "Cetirizine", "category": "Antihistamine", "quantity": 75, "price": 30, "status": "Low Stock"},
        {"id": 4, "name": "Ibuprofen", "category": "Anti-inflammatory", "quantity": 30, "price": 40, "status": "Low Stock"},
        {"id": 5, "name": "Mefenamic Acid", "category": "Pain Reliever", "quantity": 20, "price": 35, "status": "Out of Stock"},
    ]

    return render(request, 'pages/inventory.html', {'items': items})