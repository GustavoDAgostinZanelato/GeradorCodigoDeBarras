from barcode import EAN13
from barcode.writer import ImageWriter
import random


def codigoBarrasEAN13():
    id = str(random.randint(100000000000, 999999999999))
    codigoBarras = EAN13(id, writer=ImageWriter())
    localArquivo = f"Codigos de Barras/cd_{id}"
    codigoBarras.save(localArquivo)

codigoBarrasEAN13()
