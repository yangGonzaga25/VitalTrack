#Tanya Grace S. Gonzaga - Activity3
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.http import require_http_methods
from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.http.multipartparser import MultiPartParser

medicines = []

@csrf_exempt
@require_GET
def get_medicines(request):
    search_query = request.GET.get('search', '')
    filtered_medicines = [medicine for medicine in medicines if search_query.lower() in medicine['name'].lower()]
    return JsonResponse({'medicines': filtered_medicines if search_query else medicines}, status=200)

@csrf_exempt
@require_GET
def get_medicine(request, medicine_id):
    try:
        medicine = next((medicine for medicine in medicines if medicine['id'] == medicine_id), None)
        if medicine:
            return JsonResponse({'medicine': medicine}, status=200)
        else:
            return JsonResponse({'error': f'Medicine {medicine_id} not found'}, status=404)
    except ValueError:
        return JsonResponse({'error': 'Invalid medicine ID'}, status=400)

@csrf_exempt
@require_POST
def add_medicine(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            name = data.get('name')
        else:
            name = request.POST.get('name')

        if not name:
            return JsonResponse({'error': 'Name is required'}, status=400)

        new_medicine = {'id': len(medicines) + 1, 'name': name}
        medicines.append(new_medicine)
        return JsonResponse({'message': 'Medicine added', 'medicine': new_medicine}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def update_medicine(request, medicine_id):
    try:
        medicine_id = int(medicine_id)
        medicine = next((medicine for medicine in medicines if medicine['id'] == medicine_id), None)
        if not medicine:
            return JsonResponse({'error': 'Medicine not found'}, status=404)
        print("Request Content-Type:", request.content_type)
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                name = data.get('name')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        elif request.content_type.startswith('multipart/form-data'):
            request.upload_handlers = [TemporaryFileUploadHandler()]
            parser = MultiPartParser(request.META, request, request.upload_handlers)
            data, files = parser.parse()
            name = data.get('name')
            print("Form Data Name:", name)
        else:
            return JsonResponse({'error': 'Unsupported content type'}, status=415)
        if name:
            medicine['name'] = name
            return JsonResponse({'message': 'Medicine updated', 'medicine': medicine}, status=200)
        else:
            return JsonResponse({'error': 'No valid data provided'}, status=400)
    except ValueError:
        return JsonResponse({'error': 'Invalid medicine ID'}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_medicine(request, medicine_id):
    global medicines
    try:
        medicines = [medicine for medicine in medicines if medicine['id'] != medicine_id]
        return JsonResponse({'message': 'Medicine deleted'}, status=200)
    except ValueError:
        return JsonResponse({'error': 'Invalid medicine ID'}, status=400)
