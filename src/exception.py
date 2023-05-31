import sys
import logging

def error_message_detail(error, exc_info):
    _, _, exc_tb = exc_info
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message[{error}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, exc_info):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exc_info)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try: 
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        exc_info = sys.exc_info()
        raise CustomException(e, exc_info)
