# Contratos Back-Front HU S1-01-M
 
## => Flujo backoffice costos lista productos
## 1. ListarProductos
### URL:
```
/productos/  
```
### METHOD:
#### GET
### PARAMS:
```
?busqueda=str&costo_min=float&costo_max=float
````
ningún param es obligatorio, el param de busqueda requiere recibir como minimo 4 caracteres para devolver resultados, en caso contrario devolverá [].
 
para el param de costo_min se requiere cerrar el rango con el param de costo_max, los dos permiten flotantes solamente
 
### BODY:
```
null
````
 
### RESPONSE:
```
{
    count: 1,
    next: http://next.page,
    previous: null,
    results:
        [
            {  
                name: string,
                sku: string,
                type: string,
                cost: float,
                price: float,
                active: bool
            },
            {  
                name: string,
                sku: string,
                type: string,
                cost: float,
                price: float,
                active: bool
            },
            {  
                name: string,
                sku: string,
                type: string,
                cost: float,
                price: float,
                active: bool
            },
            …
        ]
}
```
