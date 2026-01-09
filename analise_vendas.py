import json

with open('vendas.json', 'r', encoding='utf-8') as arquivo:
    vendas = json.load(arquivo)

contador = 1
soma_total = 0
media_venda = 0
vendas_com_meta = 0
vendas_por_vendedor = {}

for venda in vendas:

    vendedor = venda["vendedor"]

    if vendedor in vendas_por_vendedor:
        vendas_por_vendedor[vendedor] += 1
    else:
        vendas_por_vendedor[vendedor] = 1

    if venda["meta_atingida"] == True:
        texto_meta = "Meta atingida"
        vendas_com_meta += 1
    else:
        texto_meta = "Meta não atingida"

# Imprimir a lista de vendas

    print(f"Venda nº {contador} | Vendedor: {venda["vendedor"]} | Produto: {venda["produto"]} | Valor: {venda["valor"]:.2f} | Quantidade: {venda["quantidade"]} | {texto_meta}\n")
    
    contador +=1

# Cálculo para soma total das vendas

    valor_total_venda = venda["valor"]*venda["quantidade"]
    soma_total += valor_total_venda

print(f"Soma total das vendas: R$ {soma_total:.2f}")

# Cálculo da média das vendas

media_vendas = soma_total/len(vendas)

print(f"Média das vendas: R$ {media_vendas}")

# Cálculo da quantidade de vendas que atingiram a meta e percentual em relação ao total de vendas

print(f"Quantidade de vendas com meta atingidas: {vendas_com_meta}")
print(f"Porcentagem de vendas com meta atingidas em relação ao total de vendas: {vendas_com_meta/len(vendas)*100:.2f}%")

# Quantidade de vendas por vendedor

for vendedor in vendas_por_vendedor:
    quantidade = vendas_por_vendedor[vendedor]
    print(vendedor + ": " + str(quantidade) + " venda(s)")
