from app.models import Category, Product

# def load_categories():
#     return [{
#         "id": 1,
#         "name": "Mobile"
#     }, {
#         "id": 2,
#         "name": "Tablet"
#     }]

def load_categories():
    return Category.query.order_by('id').all()

def load_products():
    query = Product.query
    return query.all()