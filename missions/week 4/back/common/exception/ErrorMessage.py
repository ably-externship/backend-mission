from enum import Enum


class ErrorMessage(Enum):
    PRODUCT_NOT_FOUND = ("PRODUCT_001",  "Product Not Found")
    PRODUCT_VALIDATION_ERROR = ("PRODUCT_002", "Product Post Invalid Error")
    MARKET_NOT_FOUND = ('MARKET_001', 'Market Not Found')
    PRODUCT_CATEGORY_NOT_FOUND = ("PRODUCT_CATEGORY_001", "Product Category Not Found")
    MARKET_ID_NOT_CORRECT = ("MARKET_001", 'Market Id Is Not Correct')



    def __init__(self, code, message):
        self.code = code
        self.message = message
