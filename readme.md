# sportventory (Sports Equipment Inventory System)


## Setup

1. Go into the project directory:
   ```
   cd sportventory/
   ```

2. Create a virtual environment and activate it (>python 3.8):
   ```
   python -m venv venv
   source venv/bin/activate`
   ```

3. Install the pip-tools package:
   ```
   pip install pip-tools
   ```
   
4. Install requirements:
   ```
   pip-sync requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/inventory/v1/items/`: Create a new item
- `PATCH /api/inventory/v1/items/<id>/`: Partially update an item's quantity or other fields
- `PUT /api/inventory/v1/items/<id>/`: Fully update an item's details
- `GET /api/inventory/v1/items/`: Get all items (supports query parameters, e.g., ?quantity=0 for items with zero quantity)
- `GET /api/inventory/v1/items/<id>/`: Retrieve a specific item by its ID
- `DELETE /api/inventory/v1/items/<id>/`: Delete a specific item by its ID


## Automated Task

Automated task to checks for items with zero quantity every minute.

## Running Tests

To run the unit tests:

```
python manage.py test
```


