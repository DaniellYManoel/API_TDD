class BaseException(Exception):
    message: str = "Internal Server Error"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message

        
class NotFoundException(BaseException):
    message ="Not Found"


# Resumo

# BaseException é uma exceção personalizada com uma mensagem padrão "Internal Server Error". Você pode fornecer uma mensagem personalizada ao instanciar a exceção. 
# NotFoundException é uma exceção específica que herda de BaseException e tem uma mensagem padrão "Not Found". Ela também permite uma mensagem personalizada ao ser instanciada.