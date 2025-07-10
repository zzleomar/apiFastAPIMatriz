from typing import Tuple, Optional
from entities.client import Client

class InvoiceValidator:
    def validateInvoiceRequest(self, clientId: Optional[int], clientData: Optional[Client], amount: float) -> Tuple[bool, str]:
        if not self._validateClientInput(clientId, clientData):
            return False, "Debe proporcionar clientId o clientData"
        
        if not self._validateAmount(amount):
            return False, "El monto debe ser mayor a 0"
        
        if clientData and not self._validateClientData(clientData):
            return False, "Los datos del cliente son inválidos: fullName y document son requeridos"
        
        return True, "Solicitud de factura válida"
    
    def _validateClientInput(self, clientId: Optional[int], clientData: Optional[Client]) -> bool:
        return clientId is not None or clientData is not None
    
    def _validateAmount(self, amount: float) -> bool:
        return amount > 0
    
    def _validateClientData(self, clientData: Client) -> bool:
        return (
            clientData.fullName is not None and 
            clientData.fullName.strip() != "" and
            clientData.document is not None and 
            clientData.document.strip() != ""
        )