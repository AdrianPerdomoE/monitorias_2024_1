# test_sistema_ventas.py
import pytest
from sistema_ventas_vehiculos.modelo.sistema_ventas import GestorDeInventario, SistemaDeFacturacion, Vehiculo,Factura
# test_sistema_ventas.py

# Pruebas para verificar la existencia de métodos y atributos en Gestor de Inventario
class TestGestorDeInventarioExistencia:
    def test_metodos_existen(self):
        gestor = GestorDeInventario()
        assert hasattr(gestor, 'agregarVehiculo'), "El método 'añadirVehiculo' no existe"
        assert hasattr(gestor, 'actualizarEstado'), "El método 'actualizarEstado' no existe"
        assert hasattr(gestor, 'obtenerInformacion'), "El método 'obtenerInformacion' no existe"

    def test_atributos_existen(self):
        gestor = GestorDeInventario()
        assert hasattr(gestor, 'vehiculos'), "El atributo 'lista_vehiculos' no existe"


# Pruebas para verificar la existencia de métodos y atributos en Sistema de Facturación
class TestSistemaDeFacturacionExistencia:
    def test_metodos_existen(self):
        facturacion = SistemaDeFacturacion()
        assert hasattr(facturacion, 'calcularPrecioFinal'), "El método 'calcularPrecioFinal' no existe"
        assert hasattr(facturacion, 'generarFactura'), "El método 'generarFactura' no existe"
        assert hasattr(facturacion, 'registrarFactura'), "El método 'registrarFactura' no existe"
        assert hasattr(facturacion, 'obtenerInformacion'), "El método 'obtenerInformacion' no existe"

    def test_atributos_existen(self):
        facturacion = SistemaDeFacturacion()
        assert hasattr(facturacion, 'impuesto'), "El atributo 'impuesto' no existe"
        assert hasattr(facturacion, 'facturas'), "El atributo 'facturas' no existe"



# Pruebas para el Gestor de Inventario
class TestGestorDeInventario:
    @pytest.fixture
    def gestor(self):
        return GestorDeInventario()

    def test_agregar_vehiculo(self, gestor):
        vehiculo = Vehiculo('Toyota', 'Corolla',5000, 'Disponible')
        gestor.añadirVehiculo(vehiculo)
        assert gestor.vehiculos[0] == vehiculo

    def test_actualizar_estado(self, gestor):
        gestor.vehiculos.append(Vehiculo('Toyota', 'Corolla',5000, 'Disponible'))
        id = gestor.vehiculos[0].vehiculoId
        gestor.actualizarEstado(id, 'vendido')
        assert gestor.gestor.vehiculos[0].estado == 'vendido'

# Pruebas para el Sistema de Facturación
class TestSistemaDeFacturacion:
    @pytest.fixture
    def facturacion(self):
        return SistemaDeFacturacion()

    def test_calcular_precio_final(self, facturacion):
        precio_base = 20000
        descuento = 1000
        vehiculo = Vehiculo('Toyota', 'Corolla',precio_base, 'Disponible')

        precio_final = facturacion.calcularPrecioFinal(vehiculo, descuento)
        assert precio_final == precio_base + (precio_base*0.19) - descuento

    def test_generar_factura(self, facturacion):
        precio_base = 20000
        descuento = 1000
        vehiculo = Vehiculo('Toyota', 'Corolla', precio_base, 'Disponible')
        factura = facturacion.generarFactura(vehiculo, descuento)
        assert factura.vehiculoId == vehiculo.vehiculoId
        assert factura.total == precio_base + (precio_base*0.19) - descuento



