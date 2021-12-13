import csv

from apps.products.models import Category, Product


# python manage.py runscript import_products_csv

def run():
    # Category,Product Name, Product QTY, Product Price
    # clothes,pant,1,10
    # clothes,shirt,1,9

    # Category.objects.all().delete()
    # Product.objects.all().delete()

    file = open('products/all.csv')
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        print(row)
        category, created = Category.objects.get_or_create(slug=row[0])
        product = Product(name=row[1], category=category, quantity=row[2], price=row[3])
        product.save()
