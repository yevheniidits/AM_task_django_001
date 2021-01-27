from django.shortcuts import render
from openpyxl import load_workbook

from main.models import Product


def main_page(request):
    if request.method == 'POST':
        file = request.FILES.get('upload')
        wb = load_workbook(file)
        ws = wb.active
        for i in ws.values:
            if i[0] is not None and type(i[0]) is int:
                product, created = Product.objects.get_or_create(vendor_code=i[0])
                product.category = i[1]
                product.manufacturer = i[2]
                product.model_name = i[3]
                product.dealer_price = i[4]
                product.retail_price = i[5]
                product.save()
    products = Product.objects.all().order_by('category')
    return render(request, 'main/main_page.html', context={'products': products})



