<a name='top'></a>
[Utilidades](cheat_sheet/READMEPROJECT.md)

# pytest
### Librerías necesarias:
    pip3 install pytest
    pip3 install selenium


### Descargar los drivers necesarios para el navegador en este caso chromedriver:
https://chromedriver.chromium.org/downloads

### Referencias:

- **selenium:** <https://www.selenium.dev/documentation/es/>
- **pytest:** <https://docs.pytest.org/en/stable/contents.html#toc>


### descargar los drivers necesarios para el navegador en este caso chromedriver:
https://chromedriver.chromium.org/downloads


### ¿Qué es pytest?
pytest es un marco que facilita la creación de pruebas simples y escalables. Las pruebas son expresivas y legibles, no se requiere un código estándar. Comience en minutos con una prueba de unidad pequeña o una prueba funcional compleja para su aplicación o biblioteca.

### Escribiendo nuestros tests
* Para escribir las pruebas es necesario escribir funciones que comiencen con el prefijo test_. 
* Debemos llamarlo así dado que al momento de ejecutar pytest especificaremos un directorio raíz, desde el cual pytest leerá todas las funciones que comiencen con test_. 

### como Ejecurtar pytest
* desde el directorio raiz:

        MacBook-Pro-de-xxxx:pytest$ pytest
        
* indicando un fichero en particular:

        MacBook-Pro-de-xxxx:pytest$ pytest [path/file_a_ejecutar]
        
[Subir](#top)
