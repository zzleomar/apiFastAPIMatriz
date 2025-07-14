from typing import Any, Tuple


class MatrizTraspuestaValidator:
    def validateMatrizStructure(matriz: Any) -> Tuple[bool, str]:
        if not isinstance(matriz, list):
            return False, "La matriz debe ser una lista"
        
        return True, "La estructura de la matriz es válida"
    
    @staticmethod
    def validateMatricesInput(matriz: Any) -> Tuple[bool, str]:
        is_Valid1, message1 = MatrizTraspuestaValidator.validateMatrizStructure(matriz)
        if not is_Valid1:
            return False, f"Error en Matriz: {message1}"
        
        return True, "Matriz es váĺida"