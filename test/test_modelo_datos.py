# test_modelos.py
import pytest


from sistema_ventas_vehiculos.modelo.sistema_ventas import Vehiculo, Factura

def test_clase_vehiculo_existe():
    assert 'Vehiculo' in globals(), "La clase Vehiculo no está definida."

def test_clase_factura_existe():
    assert 'Factura' in globals(), "La clase Factura no está definida."

def test_propiedades_vehiculo():
    propiedades_vehiculo = ['vehiculoId', 'marca', 'modelo', 'precio', 'estado']
    vehiculo = Vehiculo()
    for propiedad in propiedades_vehiculo:
        assert hasattr(vehiculo, propiedad), f"La propiedad {propiedad} no está definida en Vehiculo."

def test_propiedades_factura():
    propiedades_factura = ['facturaId', 'vehiculoId','fecha', 'detalles', 'total']
    factura = Factura()
    for propiedad in propiedades_factura:
        assert hasattr(factura, propiedad), f"La propiedad {propiedad} no está definida en Factura."
