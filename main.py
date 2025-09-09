from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

@app.get("/products/{category}/items/{item_id}")
async def read_product_item(
    category: str,  # Corrected type from 'ste' to 'str'
    item_id: int,
    urgent: bool = False,
    discount: float = 0.0
):
    """
    Get the product item details with combined path and query parameters.

    - category: Product category (path parameter, required)
    - item_id: Item identifier (path parameter, required)
    - urgent: Urgent flag (query parameter, optional, default: False)
    - discount: Discount percentage (query parameter, optional, default: 0.0)
    """

    # Create item dictionary with provided parameters
    item = {
        "category": category,
        "item_id": item_id,
        "urgent": urgent,
        "discount_applied": discount
    }

    return item
