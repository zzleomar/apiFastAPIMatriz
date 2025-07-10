from fastapi import APIRouter, HTTPException
from entities.requestModel import InvoiceRequest
from validators.invoice_validator import InvoiceValidator
from process.invoice_processor import InvoiceProcessor
from adapters.data_adapter import JsonDataAdapter

router = APIRouter(prefix="/invoice", tags=["invoices"])

dataAdapter = JsonDataAdapter()
invoiceValidator = InvoiceValidator()
invoiceProcess = InvoiceProcessor(dataAdapter)

# registro de facturas
@router.post("/")
async def createInvoice(request: InvoiceRequest):
    isValid, message = invoiceValidator.validateInvoiceRequest(
        request.clientId, request.clientData, request.amount
    )
    
    if not isValid:
        raise HTTPException(status_code=400, detail={"message": message, "status": False})
    
    try:
        invoiceData = invoiceProcess.createInvoice(
            request.clientId, request.clientData, request.amount
        )
        return {"message": "Factura creada exitosamente", "invoice": invoiceData, "status": True}
    except ValueError as e:
        raise HTTPException(status_code=404, detail={"message": str(e), "status": False})

# listado de facturas
@router.get("/list")
async def getInvoices():
    invoicesData = invoiceProcess.getAllInvoices()
    return {"invoices": invoicesData, "status": True}