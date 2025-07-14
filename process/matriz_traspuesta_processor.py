from typing import List, Any


class MatrizOPerationProcess:
    @staticmethod
    def processMatrices(matriz: List[List[Any]]) -> dict:
        i = len(matriz)
        j = len(matriz[0])
        result = MatrizOPerationProcess.initMatriz(i,j)
        for row in range(j):
            for col in range(i):
                result[row][col] = matriz[col][row]
        return { "data": result, "message": "matrices leidas" }
    
    @staticmethod
    def initMatriz(i: int, j: int) -> List[List[Any]]:
        matrizInit = []
        for row in range(j):
            init = []
            for col in range(i):
                init.append(None)
            matrizInit.append(init)
        return matrizInit
        