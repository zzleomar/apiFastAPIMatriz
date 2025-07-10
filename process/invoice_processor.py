from typing import Dict, List, Optional
from adapters.data_adapter import DataAdapter
from entities.client import Client

class InvoiceProcessor:
    def __init__(self, dataAdapter: DataAdapter):
        self.dataAdapter = dataAdapter
    
    def createInvoice(self, clientId: Optional[int], clientData: Optional[Client], amount: float) -> Dict:
        client = self._resolveClient(clientId, clientData)
        
        invoiceData = {
            "id": None,
            "client": client,
            "amount": amount
        }
        
        return self.dataAdapter.saveInvoice(invoiceData)
    
    def getAllInvoices(self) -> List[Dict]:
        return self.dataAdapter.getInvoices()
    
    def _resolveClient(self, clientId: Optional[int], clientData: Optional[Client]) -> Dict:
        if clientId:
            client = self.dataAdapter.getClientById(clientId)
            if not client:
                raise ValueError(f"Cliente con id {clientId} no encontrado")
            return client
        
        if clientData:
            clientNew = {
                "id": None,
                "fullName": clientData.fullName,
                "document": clientData.document
            }
            return self.dataAdapter.saveClient(clientNew)
        
        raise ValueError("Debe proporcionar clientId o clientData")