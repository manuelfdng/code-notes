# From Flask to Django REST Framework: A Practical Guide

If you're coming from a Flask stack with Flask-SQLAlchemy, Flask-WTForms, Flask-RESTful, and Flask-Migrate, transitioning to Django and Django REST Framework (DRF) will require some mental remapping. This guide will help you translate your knowledge of these Flask extensions to Django's way of building APIs, using the Gunpla API example as a reference.

## Project Structure Comparison

### Flask vs Django

In Flask, your project structure is often something like:

```
flask-app/
├── app.py
├── models.py
├── resources.py
├── routes.py
└── requirements.txt
```

Django has a more opinionated structure, with a main project and separate apps:

```
django-gunpla-backend/
└── myproject/             # Project root
    ├── manage.py          # Django's command-line utility
    ├── gunpla/            # App directory
    │   ├── __init__.py
    │   ├── admin.py       # Admin site configuration
    │   ├── apps.py        # App configuration
    │   ├── models.py      # Database models
    │   ├── serializers.py # Similar to Flask-RESTful marshalling
    │   ├── tests.py       # Tests
    │   └── views.py       # Similar to Flask-RESTful resources
    └── myproject/         # Project configuration
        ├── __init__.py
        ├── asgi.py        # Async server config
        ├── settings.py    # Project settings (like Flask's config)
        ├── urls.py        # URL routing (like Flask's routes)
        └── wsgi.py        # WSGI server config
```

## Key Concept Mapping

| Flask Stack | Django Equivalent | Notes |
|---------------|-------------------|-------|
| `app = Flask(__name__)` | Settings in `settings.py` | Django has a global configuration |
| Routes (`@app.route()`) | URL patterns in `urls.py` | Django uses a URL dispatcher |
| Flask-SQLAlchemy Models | Django ORM Models | Similar concept, different syntax |
| Flask-SQLAlchemy relationships | Django model relationships | Django uses `ForeignKey`, `ManyToManyField`, etc. |
| Flask-Migrate | Django Migrations | `python manage.py makemigrations` and `migrate` |
| Flask-WTForms | Django Forms/DRF Serializers | Form validation and creation |
| Flask-RESTful Resources | DRF APIView or ViewSets | Similar approach with class-based views |
| Flask `request.json` | DRF `request.data` | Similar, but Django wraps the request |
| `jsonify()` | DRF Response | Django has a built-in JSON response system |
| Flask Blueprints | Django Apps | For organizing code into modules |

## Models: Flask-SQLAlchemy vs Django ORM

### In Flask-SQLAlchemy:

```python
class Gunpla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    series = db.Column(db.String(120), nullable=False)
    grade = db.Column(db.String(50), nullable=False)
    scale = db.Column(db.String(20), nullable=True)
    
    # Relationships example
    parts = db.relationship('GunplaPart', backref='gunpla', lazy=True)
```

### In Django ORM:

```python
class Gunpla(models.Model):
    name = models.CharField(max_length=80)
    series = models.CharField(max_length=120)
    grade = models.CharField(max_length=50)
    scale = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
        
# Relationships example (would be in the same file)
class GunplaPart(models.Model):
    name = models.CharField(max_length=100)
    gunpla = models.ForeignKey(Gunpla, on_delete=models.CASCADE, related_name='parts')
```

The Django ORM doesn't require you to explicitly define the ID field – it's added automatically. Also notice how `nullable=False` becomes implicit unless you specify `blank=True, null=True`. Relationships in Django are defined in the "many" side with `ForeignKey`, rather than in the "one" side like in SQLAlchemy.

## Serialization & Validation: Flask-RESTful + Flask-WTForms vs DRF Serializers

### In Flask-RESTful with Marshal:

```python
gunpla_fields = {
    'id': fields.Integer,
    'name': fields.String(required=True),
    'series': fields.String(required=True),
    'grade': fields.String(required=True),
    'scale': fields.String
}

class GunplaResource(Resource):
    @marshal_with(gunpla_fields)
    def get(self, gunpla_id=None):
        # Return data and let marshal_with handle serialization
```

### Adding Flask-WTForms for validation:

```python
class GunplaForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    series = StringField('Series', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    scale = StringField('Scale')
    
class GunplaResource(Resource):
    def post(self):
        # Parse JSON to form
        form = GunplaForm(data=request.json)
        if form.validate():
            gunpla = Gunpla(
                name=form.name.data,
                series=form.series.data,
                grade=form.grade.data,
                scale=form.scale.data
            )
            db.session.add(gunpla)
            db.session.commit()
            return marshal(gunpla, gunpla_fields), 201
        return {'errors': form.errors}, 400
```

### In Django REST Framework:

```python
class GunplaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gunpla
        fields = ['id', 'name', 'series', 'grade', 'scale']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name field is required.")
        return value
```

DRF's serializers combine the functionality of both Flask-RESTful's marshalling and Flask-WTForms validation

## Views/Resources: Flask-RESTful vs DRF

### In Flask-RESTful:

```python
class GunplaListResource(Resource):
    def get(self):
        gunplas = Gunpla.query.all()
        return marshal(gunplas, gunpla_fields)
    
    def post(self):
        args = parser.parse_args()
        gunpla = Gunpla(**args)
        db.session.add(gunpla)
        db.session.commit()
        return marshal(gunpla, gunpla_fields), 201

class GunplaResource(Resource):
    def get(self, gunpla_id):
        gunpla = Gunpla.query.get_or_404(gunpla_id)
        return marshal(gunpla, gunpla_fields)
    
    def put(self, gunpla_id):
        gunpla = Gunpla.query.get_or_404(gunpla_id)
        args = parser.parse_args()
        for key, value in args.items():
            setattr(gunpla, key, value)
        db.session.commit()
        return marshal(gunpla, gunpla_fields)
    
    def delete(self, gunpla_id):
        gunpla = Gunpla.query.get_or_404(gunpla_id)
        db.session.delete(gunpla)
        db.session.commit()
        return {'message': 'Gunpla model deleted successfully'}
```

### In Django REST Framework:

```python
class GunplaList(APIView):
    def get(self, request):
        gunplas = Gunpla.objects.all()
        serializer = GunplaSerializer(gunplas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GunplaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class GunplaDetail(APIView):
    def get_object(self, pk):
        try:
            return Gunpla.objects.get(pk=pk)
        except Gunpla.DoesNotExist:
            raise Http404("Not found.")
    
    def get(self, request, pk):
        gunpla = self.get_object(pk)
        serializer = GunplaSerializer(gunpla)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        gunpla = self.get_object(pk)
        serializer = GunplaSerializer(gunpla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gunpla = self.get_object(pk)
        gunpla.delete()
        return Response({"message": "Gunpla model deleted successfully"}, status=status.HTTP_200_OK)
```

The pattern is similar, but notice how Django makes you explicitly specify status codes using constants. Also, notice how the serializer handles both validation and creating/updating objects with `.save()`.

## Routing: Flask vs Django

### In Flask:

```python
api.add_resource(GunplaListResource, '/gunplas')
api.add_resource(GunplaResource, '/gunplas/<int:gunpla_id>')
```

### In Django (urls.py):

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gunplas', GunplaList.as_view()),  # Matches GET/POST /gunplas
    path('gunplas/<int:pk>', GunplaDetail.as_view()),  # Matches GET/PUT/DELETE /gunplas/<pk>
]
```

Django's URL patterns use the `path()` function and match views to URLs. The `<int:pk>` syntax captures a parameter, similar to Flask's `<int:gunpla_id>`.

## Error Handling

### In Flask-RESTful:

```python
def not_found_error(e):
    return jsonify({"message": "Resource not found"}), 404

app.register_error_handler(404, not_found_error)
```

### In Django REST Framework:

```python
# In the view:
def get_object(self, pk):
    try:
        return Gunpla.objects.get(pk=pk)
    except Gunpla.DoesNotExist:
        raise Http404("Not found.")
```

DRF handles common exceptions automatically. Raising `Http404` will return a proper 404 response with a JSON payload.

## Testing: Flask vs Django

### In Flask (using pytest):

```python
def test_get_gunplas(client):
    response = client.get('/gunplas')
    assert response.status_code == 200
    assert len(response.json) == 1
```

### In Django:

```python
def test_get_gunplas(self):
    """Test getting list of gunplas."""
    response = self.client.get(self.base_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.json()), 1)
    gunpla_data = response.json()[0]
    self.assertEqual(gunpla_data['name'], "RX-78-2 Gundam")
```

Django's testing system includes a test client with methods like `get()`, `post()`, etc. Django uses the more traditional `self.assertEqual()` style assertions (though pytest is still popular with Django developers).

## Beyond the Basics: Django REST Framework Features

What makes DRF different from Flask-RESTful is the additional features:

### 1. ViewSets and Routers

Instead of `APIView`, you can use `ViewSet` to reduce repetition:

```python
from rest_framework import viewsets

class GunplaViewSet(viewsets.ModelViewSet):
    queryset = Gunpla.objects.all()
    serializer_class = GunplaSerializer

# Then in urls.py:
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gunplas', GunplaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

This automatically generates all CRUD endpoints with far less code!

### 2. Authentication and Permissions

DRF has built-in auth systems, unlike Flask-RESTful where you'd typically use Flask-JWT:

```python
from rest_framework.permissions import IsAuthenticated

class GunplaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # ...
```

### 3. Pagination

DRF handles pagination elegantly:

```python
# In settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### 4. Browsable API

One killer feature of DRF is the browsable HTML API interface that you get for free.

## Implementation Differences to Watch Out For

### 1. Request Data

- Flask: `data = request.json`
- DRF: `data = request.data`

### 2. Response Format

- Flask: `return jsonify(data), 200`
- DRF: `return Response(data, status=status.HTTP_200_OK)`

### 3. 404 Handling

- Flask: `item = Model.query.get_or_404(id)`
- DRF: Use try/except with `Http404` or `get_object_or_404()`

### 4. Form Processing

- Flask: `request.form` or `request.json`
- DRF: Both parsed into `request.data` automatically

## Data Validation Approaches

### Flask-RESTful:

```python
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('series', type=str, required=True)
# In the resource method:
args = parser.parse_args()
```

### Django REST Framework:

```python
# In the serializer:
def validate_name(self, value):
    if not value:
        raise serializers.ValidationError("Name field is required.")
    return value

# In the view:
serializer = GunplaSerializer(data=request.data)
if serializer.is_valid():
    # use the data
else:
    # handle errors
```

DRF separates validation into the serializer, making views cleaner.

## Common Django Commands

Coming from Flask, here are common commands you'll use:

| Flask (with Flask-Script) | Django |
|---------------------------|--------|
| `python manage.py runserver` | `python manage.py runserver` |
| `python manage.py shell` | `python manage.py shell` |
| `python manage.py db migrate` | `python manage.py makemigrations` |
| `python manage.py db upgrade` | `python manage.py migrate` |
| `python manage.py test` | `python manage.py test` |

## Conclusion

If you're coming from Flask, Django's structure may initially feel restrictive, but its "batteries-included" approach provides many tools that you'd have to add piecemeal in Flask.

The key differences to remember:
1. Django is more structured and opinionated
2. Django REST Framework offers more out-of-the-box features
3. Django's ORM is tightly integrated, compared to SQLAlchemy in Flask
4. Django has an admin interface built-in
5. Django uses class-based views, similar to Flask-RESTful's Resources

Both frameworks can build great APIs - Django's strength is in its comprehensive ecosystem, while Flask offers maximum flexibility. Choose what works best for your project!