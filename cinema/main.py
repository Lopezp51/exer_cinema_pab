from sala import Sala
from cliente import Cliente

sala1 = Sala(1)
sala2 = Sala(2)

clientes = [
    Cliente("Fulano", "300.224.660-37", sala1),
    Cliente("Beltrano", "255.709.820-51", sala1),
    Cliente("Cicrano", "542.159.460-26", sala2),
    Cliente("Alano", "013.394.290-20", sala1),
    Cliente("Zutano", "544.410.090-89", sala2)
]

for cliente in clientes:
    cliente.escolher_poltrona(clientes)

for cliente in clientes:
    print(f"{cliente.nome} (CPF: {cliente.cpf}) está na Sala {cliente.sala.numero}, "
          f"assistindo '{cliente.sala.filme}' e sentado na poltrona {cliente.poltrona.codigo} ({cliente.poltrona.cor}).")
