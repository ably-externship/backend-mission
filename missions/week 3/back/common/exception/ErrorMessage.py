from enum import Enum


class ErrorMessage(Enum):
    PRODUCT_001 = ("PRODUCT_001",  "Product Not Found")



    def __init__(self, code, message):
        self.code = code
        self.message = message
