from typing import List, Any


class MatrixProcessor:
    @staticmethod
    def processMatrices(matrix1: List[List[float]], matrix2: List[List[str]], i: int, j: int) -> dict:
        return { "data": MatrixProcessor.getatrixInfo(matrix1, matrix2, i , j), "message": "matrices leidas" }
    
    @staticmethod
    def getatrixInfo(matrix1: List[List[float]], matrix2: List[List[str]], i: int, j: int) -> dict:
        matrix3 = MatrixProcessor.calculateMatrix3(matrix1, matrix2)
       # key = f"K{i}{j}" para key dinamicos
        return {
            "matrix1": matrix1,
            "matrix2": matrix2,
            "matrix3": matrix3,
            "Kij": matrix3[i-1][j-1]
        }

    @staticmethod
    def calculateMatrix3(matrix1: List[List[float]], matrix2: List[List[str]]) -> List[List[Any]]:
        k = [[None,None,None],[None,None,None],[None,None,None]]
        for i in range(3):
            for j in range(3):
                b = matrix2[i][j]
                k[i][j] = MatrixProcessor.calculateK(b, matrix1)
        return k

    @staticmethod
    def calculateK(b: str, matrix1: List[List[float]]) -> List[dict]:
        kValue = [[None,None,None],[None,None,None],[None,None,None]]
        for i in range(3):
            for j in range(3):
                kValue[i][j] = {
                    "B": b,
                    "A": matrix1[i][j],
                }
        return kValue
    