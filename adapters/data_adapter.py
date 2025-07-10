import json
from typing import List, Dict, Optional
from adapters.data_adapter_abstract import DataAdapter

class JsonDataAdapter(DataAdapter):
    def __init__(self, clientsFile: str = "data/clients.json", invoicesFile: str = "data/invoices.json"):
        self.clientsFile = clientsFile
        self.invoicesFile = invoicesFile
    
    def _readJsonFile(self, file_path: str) -> List[Dict]:
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def _writeJsonFile(self, file_path: str, data: List[Dict]):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    
    def _getNextId(self, data: List[Dict]) -> int:
        if not data:
            return 1
        return max(item['id'] for item in data) + 1
    
    def getClients(self) -> List[Dict]:
        return self._readJsonFile(self.clientsFile)
    
    def getInvoices(self) -> List[Dict]:
        return self._readJsonFile(self.invoicesFile)
    
    def saveClient(self, client: Dict) -> Dict:
        clients = self.getClients()
        if 'id' not in client or client['id'] is None:
            client['id'] = self.getNextClientId()
        clients.append(client)
        self._writeJsonFile(self.clientsFile, clients)
        return client
    
    def saveInvoice(self, invoice: Dict) -> Dict:
        invoices = self.getInvoices()
        if 'id' not in invoice or invoice['id'] is None:
            invoice['id'] = self.getNextInvoiceId()
        invoices.append(invoice)
        self._writeJsonFile(self.invoicesFile, invoices)
        return invoice
    
    def getClientById(self, clientId: int) -> Optional[Dict]:
        clients = self.getClients()
        return next((c for c in clients if c['id'] == clientId), None)
    
    def getInvoiceById(self, invoiceId: int) -> Optional[Dict]:
        invoices = self.getInvoices()
        return next((c for c in invoices if c['id'] == invoiceId), None)
    
    def getNextClientId(self) -> int:
        clients = self.getClients()
        return self._getNextId(clients)
    
    def getNextInvoiceId(self) -> int:
        invoices = self.getInvoices()
        return self._getNextId(invoices)