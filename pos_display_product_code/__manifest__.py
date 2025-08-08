{
    "name": "POS: Display Internal Reference in Product List",
    "version": "17.0",
    "category": "Point of Sale",
    "summary": "Show product internal reference (default code) in the POS interface for better product identification and selection.",
    "description": """
        Enhance your Point of Sale experience by displaying product internal references (default codes) directly in the product list.
        
        Key Features:
        - Automatically shows internal reference alongside product names in the POS screen.
        - Helps cashiers and operators quickly identify similar products.
        - Ideal for retail environments with multiple variants or barcode-like naming conventions.
        - Lightweight and seamlessly integrates into the existing POS view.
        - No configuration required—install and activate.
        
        This module improves product lookup and selection efficiency, especially in fast-paced sales environments.
    """,

    "author": "Hi Spark Solutions",
    "company": "Hi Spark Solutions",
    "maintainer": "Hi Spark Solutions",
    "website": "https://www.hisparksolutions.com/",

    "depends": ["point_of_sale"],
    "demo": [],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {},

    "images": ["static/description/banner.gif"],
    "qweb": [],
    "live_test_url": "",

    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": "5",
    "currency": "USD",
}
