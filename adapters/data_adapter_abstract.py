from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class DataAdapter(ABC):
    @abstractmethod
    def getClients(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def getInvoices(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def saveClient(self, client: Dict) -> Dict:
        pass
    
    @abstractmethod
    def saveInvoice(self, invoice: Dict) -> Dict:
        pass
    
    @abstractmethod
    def getClientById(self, clientId: int) -> Optional[Dict]:
        pass
    
    @abstractmethod
    def getInvoiceById(self, invoiceId: int) -> Optional[Dict]:
        pass
    
    @abstractmethod
    def getNextClientId(self) -> int:
        pass
    
    @abstractmethod
    def getNextInvoiceId(self) -> int:
        pass