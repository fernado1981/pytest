<a name='top'></a>
[Utilidades](cheat_sheet/READMEPROJECT.md)

# pytest
### Librerías necesarias:
    pip3 install pytest
    pip3 install selenium

### descargar los drivers necesarios para el navegador en este caso chromedriver:
https://chromedriver.chromium.org/downloads

### ¿Qué es pytest?
pytest es un framework para Python que ofrece la recolección automática de los tests, aserciones simples, soporte para fixtures, debugeo,...

### Escribiendo nuestros tests
* Para escribir las pruebas es necesario escribir funciones que comiencen con el prefijo test_. 
* Debemos llamarlo así dado que al momento de ejecutar pytest especificaremos un directorio raíz, desde el cual pytest leerá todas las funciones que comiencen con test_. 

### como Ejecurtar pytest
* desde el directorio raiz:

        MacBook-Pro-de-xxxx:pytest$ pytest
        
* indicando un fichero en particular:

        MacBook-Pro-de-xxxx:pytest$ pytest [path/file_a_ejecutar]
        
[Subir](#top)
