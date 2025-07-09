from typing import List, Any, Tuple


class MatrixValidator:
    @staticmethod
    def validateMatrixStructure(matrix: Any, type: str) -> Tuple[bool, str]:
        typeMap = {
            'Number': int,
            'String': str
        }
        if not isinstance(matrix, list):
            return False, "La matriz debe ser una lista"
        
        if len(matrix) != 3:
            return False, "La matriz debe tener exactamente 3 filas"
        
        for i, row in enumerate(matrix): # iterador por filas
            if not isinstance(row, list):
                return False, f"La fila {i} debe ser una lista"
            
            if len(row) != 3:
                return False, f"La fila {i} debe tener exactamente 3 columnas"
            
            for j, value in enumerate(row): # iterador por valor de cada item de la fila
                if not isinstance(value, typeMap[type]):
                    return False, f"El elemento en la posición [{i}][{j}] debe ser un {type}"
        
        return True, "La estructura de la matriz es válida"
    
    @staticmethod
    def validateMatricesInput(matrix1: Any, matrix2: Any, i: int, j: int) -> Tuple[bool, str]:
        is_Valid1, message1 = MatrixValidator.validateMatrixStructure(matrix1, 'Number')
        if not is_Valid1:
            return False, f"Error en Matriz 1: {message1}"
        
        isValid2, message2 = MatrixValidator.validateMatrixStructure(matrix2, 'String')
        if not isValid2:
            return False, f"Error en Matriz 2: {message2}"

        if not (0 < i <= 3) or not (0 < j <= 3):
            return False, "Los índices i y j deben estar entre 1 y 3"
        
        return True, "Ambas matrices son válidas"