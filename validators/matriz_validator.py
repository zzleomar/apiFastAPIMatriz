from typing import List, Any, Tuple


class MatrizValidator:
    @staticmethod
    def validateMatrizStructure(matriz: Any, type: str) -> Tuple[bool, str]:
        typeMap = {
            'Number': int,
            'String': str
        }
        if not isinstance(matriz, list):
            return False, "La matriz debe ser una lista"
        
        if len(matriz) != 3:
            return False, "La matriz debe tener exactamente 3 filas"
        
        for i, row in enumerate(matriz): # iterador por filas
            if not isinstance(row, list):
                return False, f"La fila {i} debe ser una lista"
            
            if len(row) != 3:
                return False, f"La fila {i} debe tener exactamente 3 columnas"
            
            for j, value in enumerate(row): # iterador por valor de cada item de la fila
                if not isinstance(value, typeMap[type]):
                    return False, f"El elemento en la posición [{i}][{j}] debe ser un {type}"
        
        return True, "La estructura de la matriz es válida"
    
    @staticmethod
    def validateMatricesInput(matriz1: Any, matriz2: Any, i: int, j: int) -> Tuple[bool, str]:
        is_Valid1, message1 = MatrizValidator.validateMatrizStructure(matriz1, 'Number')
        if not is_Valid1:
            return False, f"Error en Matriz 1: {message1}"
        
        isValid2, message2 = MatrizValidator.validateMatrizStructure(matriz2, 'String')
        if not isValid2:
            return False, f"Error en Matriz 2: {message2}"

        if not (0 < i <= 3) or not (0 < j <= 3):
            return False, "Los índices i y j deben estar entre 1 y 3"
        
        return True, "Ambas matrices son válidas"