class Producto:

    contador_productos = 0

    def __init__(self, nombre, precio) :
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self) -> str:
        return f'ID producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    
    producto1 = Producto('Camisa',100.000)
    print(producto1)
    producto2 = Producto('Pantalón', 80.000)
    print(producto2)