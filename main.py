from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI() #Só com esse comando a api já está criada

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa", "preco_unitario": 7, "quantidade": 5},
    3: {"item": "celular", "preco_unitario": 2500, "quantidade": 5},
    4: {"item": "pc", "preco_unitario": 5000, "quantidade": 5},
}

class ItemForSale(BaseModel):
    name_item: str
    preco_unitario: float
    quantidade: int

@app.get("/") #@ = decorator
async def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
async def get_sale(id_venda: int): # recebendo parâmetro e passando sua tipagem
    if id_venda in vendas:
         return vendas[id_venda]
    else:
        return {"Erro": "ID da venda inexistente!"}

@app.put("/update/{id_venda}")
async def update_Item(id_venda: int, item: ItemForSale):
    return {"Name_item": item.name_item, "Preco_unitario": item.preco_unitario, "Quantidade": item.quantidade}
   
   
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)



