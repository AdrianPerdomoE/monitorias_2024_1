# Taller de Asignación de Responsabilidades

## Objetivos 🎯
- **Comprender** la importancia de la asignación de responsabilidades en la programación orientada a objetos.
- **Identificar** y **asignar** responsabilidades a las clases y objetos de manera efectiva.
- **Desarrollar** habilidades de documentación utilizando UML.
- **Github**: Aprender a clonar un repositorio.
- **Python**: Aprender a crear y activar un ambiente virtual, instalar dependencias y ejecutar pruebas.
- 
## Descripción 📝
En este taller, cada participante será asignado a un componente de un sistema de software simulado para la venta de vehículos. Tu tarea será definir las responsabilidades de tu componente, cómo interactúa con otros componentes y documentar el proceso utilizando UML y pseudocódigo.

## Sistema de Venta de Vehículos 🚗
## Contexto:
Don Camilo, el dueño de un concesionario de vehículos, ha decidido modernizar su sistema de ventas. El sistema actual es muy rudimentario y no permite a los clientes ver la información de los vehículos disponibles, ni realizar compras. Don Camilo ha decidido que el nuevo sistema debe permitir a los clientes ver los vehículos disponibles, realizar compras  y recibir la factura de la compra. El sistema también debe permitir a los empleados del concesionario administrar el inventario, calcular el precio final de venta y generar facturas para los clientes, para esto, ha decidido contratarte a ti, un desarrollador versado en python, para que implementes el sistema de su compañia.
### Modelo de Datos:

#### Clase: Vehiculo
- **Propiedades**:
  - `vehiculoId`: Identificador único del vehículo, generado automáticamente, se recomienda usar uuid.uuid4() una librería de python que genera identificadores únicos o tener una propiedad de clase que actue como contador y cada instancia de la clase tome el valor de este contador y se aumente por cada instancia creada.
  - `marca`: Marca del vehículo.
  - `modelo`: Modelo del vehículo.
  - `precio`: Precio base del vehículo.
  - `estado`: Estado actual del vehículo (disponible, vendido).

#### Clase: Factura
- **Propiedades**:
  - `facturaId`: Identificador único de la factura, generado automáticamente, se recomienda usar uuid.uuid4() una librería de python que genera identificadores únicos o tener una propiedad de clase que actue como contador y cada instancia de la clase tome el valor de este contador y se aumente por cada instancia creada.
  - `vehiculoId`: Identificador del vehículo que se está vendiendo.
  - `fecha`: Fecha en la que se realiza la venta.
  - `detalles`: Detalles de la venta, incluyendo descuento y tarifa aplicada.
  - `total`: Monto total a pagar por el cliente.

### Componente: Gestor de Inventario
- **Descripción**: Administra la información de los vehículos disponibles para la venta.
- **Responsabilidades**:
  - Añadir nuevos vehículos al inventario.
  - Actualizar el estado de los vehículos (disponible, vendido). 
  - Proporcionar información de cada vehículo.
- **Atributos**:
  - Lista de vehículos. (se llamará vehiculos)
- **Funciones**:
  - `agregarVehiculo(vehiculo)`: Añade un nuevo vehículo al inventario.
  - `actualizarEstado(vehiculoId, nuevoEstado)`: Actualiza el estado de un vehículo.
  - `obtenerInformacion(vehiculoId)`: Retorna la información detallada de un vehículo.

### Componente: Sistema de Facturación
- **Descripción**: Procesa las transacciones y genera facturas para los clientes.
- **Responsabilidades**:
  - Calcular el precio final de venta.
  - Generar la factura de la venta.
  - Registrar el pago del cliente.
- **Atributos**:
  -  impuesto (sera de 19% , osea 0.19).
  - Lista de facturas. (se llamará facturas)
- **Funciones**:
  - `calcularPrecioFinal(vehiculo, descuento)`: Calcula el precio final con descuento e impuesto. (el valor del impuesto se calcula con el precio del vehículo sin descuento)
  - `generarFactura(vehiculo, descuento)`: Crea una factura basada en la información de la venta.
  - `registrarFactura(factura)`: Registra la factura.
  - `obtenerInformacion(facturaId)`: Retorna la información detallada de una factura.

### Componente: Menu por consola para el usuario
**Este componente no es una clase, sino una interfaz de usuario que permite la interacción del usuario con el sistema.**, por lo tanto no es necesario tenerlo en cuenta en el diagrama UML y tampoco es necesario implementar una clase para este componente, sin embargo, es importante tener en cuenta las responsabilidades de este componente para asignar las responsabilidades a las clases y métodos de los otros componentes, si lo desean, lo pueden implementar en el main, para asegurarse de que el sistema funcione correctamente.
- **Descripción**: Permite la interacción del usuario con el sistema.
- **Responsabilidades**:
  - Recibir entradas del usuario.
  - interactuar con el sistema de ventas y el sistema de facturación.
  - Mostrar vehículos disponibles.
  - Mostrar facturas registradas
- **Atributos**:
  - Sistema de facturación.
  - Sistema de inventario.
- **Funciones**: (estas son las funciones que se recomiendan, sin embargo, usted puede implementar las funciones que considere necesarias para que el sistema funcione correctamente)
  - `mostrarVehiculosDisponibles()`: Muestra la lista de vehículos disponibles.
  - `recibirEntradaUsuario()`: Procesa la entrada del usuario por consola.
  - `mostrarFacturas()`: Muestra las facturas registradas.
  - `detallesFactura(id)`: Muestra los datos de una factura.
  - `detallesVehiculo(id)`: Muestra los datos de un vehiculo.
  - `realizarCompra(id, descuento)`: Realiza la compra de un vehículo.
  - `calcularPrecioFinal(id, descuento)`: Calcula el precio final de un vehículo con descuento.
  - `añadirVehiculo()`: Añade un vehículo al inventario.
  - `actualizarEstado(id, nuevoEstado)`: Actualiza el estado de un vehículo.

## Actividades 🛠️
1. **Análisis de Responsabilidades**: Define las responsabilidades de los componentes.
2. **Asignación de Responsabilidades**: Asigna las responsabilidades a las clases y métodos de cada componente.
3. **Implementación**: Implementa las clases y métodos en el archivo sistema_ventas.py.
4. **Documentación**: Utiliza UML para visualizar las relaciones.

## Solución 📌
 En la carpeta solución podrá encontrar el diagrama UML de la solucion propuesta para el problema planteado y el código implementando, si embargo, recuerde que la solución propuesta es solo una guía, usted puede implementar el código de la manera que considere más adecuada, siempre y cuando cumpla con los requisitos planteados en el enunciado del taller y se aconseja que realice su propio diagrama UML para visualizar las relaciones entre las clases y métodos y que le sirva como guía para la implementación del código, se recomienda encarecidamente que antes de ver la solución haya realizado el ejercicio por su cuenta.
## Entrega 📬
 Presentarse en horario de monitoria con uno de los monitores para revisar el ejercicio.

### Qué se espera de la entrega
- Implementación de las clases y métodos en el archivo sistema_ventas.py
- Diagrama UML
- opcional: documento con la asignación de responsabilidades.


Este taller es un material de estudio opcional diseñado para reforzar tu comprensión de la asignación de responsabilidades en la programación orientada a objetos.

¡Esperamos que este ejercicio te ayude a aplicar estos conceptos de manera práctica y efectiva!

# IMPORTANTE 🚨
Para realizar la actividad puedes clonar este repositorio e implementar el código en la ruta sistema_ventas_vehiculos/modelo/ en el archivo sistema_ventas.py. Debes implementar las clases y métodos que se encuentran explicadas en el enunciado del taller.


Una vez clones el repositorio, debes crear y activar el ambiente virtual. Si sabes como hacerlo en PyCharm o VSCode, hazlo. Si no, ejecuta los siguientes comandos en la consola de Windows:

* `python -m venv venv`
* `venv/Scripts/activate`
* `pip install -r requirements.txt`

Si te sale un mensaje de error diciendo que no tienes permisos para ejecutar scripts, ejecuta el siguiente comando:

* `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Tenga en cuenta lo siguiente para el desarrollo del ejercicio 🚨 
* El proyecto incluye un conjunto de pruebas que puedes utilizar para verificar el cumplimiento de los 
requisitos establecidos. Para ejecutar las pruebas, debes instalar la dependencia pytest.
* Para que las pruebas funcionen adecuadamente debes implementar el código respetando los nombres y la 
definición de las clases y los métodos que se presentan en el diagrama.
* Este taller se asemeja a la estructura de los trimestrales de la asignatura, laa evaluación del ejercicio se hará con base en el cumplimiento de los requisitos que arrojen las 
pruebas. Por lo tanto, cualquier fallo en las pruebas debido a nombres mal escritos o que no concuerden con el modelo dado se considerará como un requisito no cumplido, afectando la calificación del examen, utilice sabiamente los recursos que se le brindan para realizar el ejercicio.
* Si tienes dudas sobre el enunciado del taller, puedes preguntarle a tu monitor en el horario de monitorias.