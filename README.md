# FastAPI Combined Path and Query Parameters

A FastAPI application demonstrating how to combine path parameters and query parameters in a single endpoint.

## 🚀 Features

- FastAPI framework with automatic OpenAPI documentation
- Demonstrates combining path and query parameters
- Shows multiple path parameters in a single route
- Includes optional query parameters with default values
- Interactive API documentation at `/docs` and `/redoc`
- Python 3.7+ compatibility
- Virtual environment setup

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/fastapi-combined-params-demo.git
   cd fastapi-combined-params-demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

The project uses the following main dependencies:
- `fastapi` - The web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI applications

To generate requirements.txt:
```bash
pip freeze > requirements.txt
```

## 🚀 Running the Application

1. **Start the development server**
   ```bash
   uvicorn main:app --reload --reload-exclude venv
   ```

2. **Access the application**
   - API: http://127.0.0.1:8000
   - Interactive docs: http://127.0.0.1:8000/docs
   - Alternative docs: http://127.0.0.1:8000/redoc

## 📡 API Endpoints

### GET /products/{category}/items/{item_id}
Returns product item details with combined path and query parameters.

**Path Parameters:**
- `category` (string): Product category (e.g., "electronics", "clothing")
- `item_id` (int): Unique identifier for the item

**Query Parameters:**
- `urgent` (bool, optional): Urgency flag (default: false)
- `discount` (float, optional): Discount percentage to apply (default: 0.0)

**Examples:**
```bash
# Basic request with only path parameters
curl "http://127.0.0.1:8000/products/electronics/items/123"

# With optional query parameters
curl "http://127.0.0.1:8000/products/electronics/items/123?urgent=true"
curl "http://127.0.0.1:8000/products/electronics/items/123?discount=15.5"

# With all parameters
curl "http://127.0.0.1:8000/products/electronics/items/123?urgent=true&discount=15.5"
```

**Sample Responses:**
```json
// Basic response
{
  "category": "electronics",
  "item_id": 123,
  "urgent": false,
  "discount_applied": 0.0
}

// With query parameters
{
  "category": "electronics",
  "item_id": 123,
  "urgent": true,
  "discount_applied": 15.5
}
```

## 🎯 Key Concept: Combining Path and Query Parameters

### Path Parameters
- **Syntax:** `{parameter_name}` in the URL path
- **Required:** Always mandatory
- **Position:** Part of the URL structure
- **Example:** `/products/{category}/items/{item_id}`

### Query Parameters
- **Syntax:** `?key=value&key2=value2` after the URL path
- **Optional:** Can have default values
- **Position:** After the `?` in the URL
- **Example:** `?urgent=true&discount=15.5`

### How FastAPI Distinguishes Them:
- Parameters defined in the path → **Path parameters**
- Parameters not in the path → **Query parameters**
- Automatic type validation for both
- Comprehensive documentation in OpenAPI schema

## 🧪 Testing the API

### Testing Different Combinations:

1. **Path parameters only:**
   ```bash
   curl "http://127.0.0.1:8000/products/electronics/items/123"
   curl "http://127.0.0.1:8000/products/clothing/items/456"
   ```

2. **With query parameters:**
   ```bash
   curl "http://127.0.0.1:8000/products/electronics/items/123?urgent=true"
   curl "http://127.0.0.1:8000/products/electronics/items/123?discount=10.0"
   curl "http://127.0.0.1:8000/products/electronics/items/123?urgent=true&discount=15.5"
   ```

3. **Interactive testing:** Use the Swagger UI at `/docs` to test various combinations

## 📁 Project Structure

```
fastapi-combined-params-demo/
├── main.py          # Main application file
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── venv/            # Virtual environment (gitignored)
```

## 🔧 Code Explanation

### main.py
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{category}/items/{item_id}")
async def read_product_item(
    category: str,       # Path parameter (required)
    item_id: int,        # Path parameter (required)
    urgent: bool = False, # Query parameter (optional)
    discount: float = 0.0 # Query parameter (optional)
):
    """
    Get product item details with combined path and query parameters.
    
    - category: Product category (path parameter, required)
    - item_id: Item identifier (path parameter, required)
    - urgent: Urgency flag (query parameter, optional, default: false)
    - discount: Discount percentage (query parameter, optional, default: 0.0)
    """
    item = {
        "category": category,
        "item_id": item_id,
        "urgent": urgent,
        "discount_applied": discount
    }
    # You would typically fetch this data from a database
    return item
```

### Key Points:
- **Path parameters:** `category` and `item_id` (no default values = required)
- **Query parameters:** `urgent` and `discount` (with default values = optional)
- **Automatic type conversion:** FastAPI converts string values to appropriate types
- **Validation:** Invalid types return descriptive error messages

## 🎓 Learning Points

1. **Path Parameters**: For essential, identifying information in URL structure
2. **Query Parameters**: For optional modifications, filtering, and flags
3. **Type Safety**: FastAPI validates both path and query parameters
4. **Default Values**: Make query parameters optional
5. **API Design**: Strategic use of both parameter types for clean API design

## 🔧 Troubleshooting

### Common Issues:

1. **Type conversion errors**
   - Ensure correct parameter types (e.g., `item_id` must be integer)

2. **Missing required path parameters**
   - All path parameters must be provided in the URL

3. **URL encoding**
   - Special characters in path parameters may need URL encoding

4. **Boolean parameter values**
   - Use `true`/`false` or `1`/`0` for boolean parameters

5. **Reload issues**
   ```bash
   uvicorn main:app --reload --reload-exclude venv
   ```

## 📚 Learning Resources

- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [FastAPI Parameter Combinations](https://fastapi.tiangolo.com/tutorial/body/#mix-path-query-and-body-parameters)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- Uvicorn team for the ASGI server
- Python community for ongoing support
