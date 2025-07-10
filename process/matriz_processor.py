from typing import List, Any


class MatrizProcessor:
    @staticmethod
    def processMatrices(matriz1: List[List[float]], matriz2: List[List[str]], i: int, j: int) -> dict:
        return { "data": MatrizProcessor.getMatrizInfo(matriz1, matriz2, i , j), "message": "matrices leidas" }
    
    @staticmethod
    def getMatrizInfo(matriz1: List[List[float]], matriz2: List[List[str]], i: int, j: int) -> dict:
        matriz3 = MatrizProcessor.calculateMatriz3(matriz1, matriz2)
       # key = f"K{i}{j}" para key dinamicos
        return {
            "matriz1": matriz1,
            "matriz2": matriz2,
            "matriz3": matriz3,
            "Kij": matriz3[i-1][j-1]
        }

    @staticmethod
    def calculateMatriz3(matriz1: List[List[float]], matriz2: List[List[str]]) -> List[List[Any]]:
        k = [[None,None,None],[None,None,None],[None,None,None]]
        for i in range(3):
            for j in range(3):
                b = matriz2[i][j]
                k[i][j] = MatrizProcessor.calculateK(b, matriz1)
        return k

    @staticmethod
    def calculateK(b: str, matriz1: List[List[float]]) -> List[dict]:
        kValue = [[None,None,None],[None,None,None],[None,None,None]]
        for i in range(3):
            for j in range(3):
                kValue[i][j] = {
                    "B": b,
                    "A": matriz1[i][j],
                }
        return kValue
    