import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script: [{file_name}], "
        f"line number: [{exc_tb.tb_lineno}], error message: [{str(error)}]"
    )
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception that provides detailed error messages.
        """
        # Generate a detailed error message
        self.error_message = error_message_detail(error_message, error_detail)
        # Initialize the base Exception class with a basic error message
        super().__init__(self.error_message)
        
        
    def __str__(self):
        return self.error_message
    

