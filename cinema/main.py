from sala import Sala
from cliente import Cliente

#ao inicar é instaciando as classes, onde a sala é criada e o filme é sorteado
# a sala é criada com 5 poltronas, cada uma com uma cor diferente
sala1 = Sala(1)
sala2 = Sala(2)

clientes = [
    Cliente(nome="Fulano", cpf="300.224.660-37", sala=sala1),
    Cliente(nome="Beltrano", cpf="255.709.820-51", sala=sala1),
    Cliente(nome="Cicrano", cpf="542.159.460-26", sala=sala2),
    Cliente(nome="Alano", cpf="013.394.290-20", sala=sala1),
    Cliente(nome="Zutano", cpf="544.410.090-89", sala=sala2)
]

for cliente in clientes:
    cliente.escolher_poltrona(clientes)

for cliente in clientes:
    print(f"{cliente.nome} (CPF: {cliente.cpf}) está na Sala {cliente.sala.numero}, "
          f"assistindo '{cliente.sala.filme}' e sentado na poltrona {cliente.poltrona.codigo} ({cliente.poltrona.cor}).")
