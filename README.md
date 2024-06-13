# City distance Service
 Servicio que permite calcular la distancia entre dos ciudades basado en 


# Integrantes
- Marcelo Chincha

- David Herencia


| Test Case | Precondition | Tests Steps  | Test Data | Expected Result |
|-|-|-|-|-|
| Verificar la busqueda de ubicación con ciudades válidas (api, csv, mock) | a) Api que usa el servicio sea pública.  <br> b) Acceso al csv con la información.<br> c) Tener el mock seteado a las ciudades de Lima y Las Vegas. | 1. Instanciar los servicios de ubicación (api, csv, mock). <br> 2. Ingresar una ciudad y país válidos. <br> 3. Ejecutar función de test. | Ciudad: Lima  <br> País: Perú  | Coordenadas de Lima: (lat) -12.04318, (long) -77.02824 |
| Verificar la búsqueda de ubicación con ciudades inválidas (api, csv, mock) | a) Api que usa el servicio sea pública.  <br> b) Acceso al csv con la información.<br> c) Tener el mock seteado a las ciudades de Lima y Las Vegas. | 1. Instanciar los servicios de ubicación (api, csv, mock). <br> 2. Ingresar una ciudad y país inválidos. <br> 3. Ejecutar función de test. | Ciudad: St marmero  <br> País: Antegria | Coordenadas: None |
| Verificar el cálculo de las distancias con coordenadas válidas | Tener acceso a la función que calcula la distancia. | 1. Definir las coordenadas válidas (latitud y longitud). <br> 2. Llamar a la función y ingresar las coordenadas como parámetro.  | Coordenadas: <br> Coor 1: (lat1) -12.04318, (long1) -77.02824. <br> Coor 2: (lat2) 36.114647, (long2) -115.172813 | Distancia calculada entre las coordenadas dadas |
| Verificar el cálculo de las distancias con coordenadas inválidas | Tener acceso a la función que calcula la distancia. | 1. Definir las coordenadas inválidas. <br> 2. Llamar a la función y ingresar las coordenadas como parámetro. | Coordenadas: <br> Coor a: (lat1) -12.04318, (long1) -77.02824. <br> Coor b: (lat2) -200, (long2) -200 | Error o mensaje de coordenadas inválidas |
| Verificar obtener 2 ciudades con distancia mínima entre 3 ciudades válidas (api, csv, mock) | a) Api que usa el servicio sea pública. <br> b) Acceso al csv con la información.<br> c) Tener el mock seteado a las ciudades de Lima, Las Vegas y Nueva York. | 1. Instanciar los servicios de ubicación (api, csv, mock). <br> 2. Ingresar tres ciudades y países válidos. <br> 3. Ejecutar función de test. | Ciudades: <br> 1. Lima, Perú. <br> 2. Las Vegas, Estados Unidos <br> 3. Buenos aires, Argentina | Pareja de ciudades con menor distancia: Lima - Buenos aires |
| Verificar obtener 2 ciudades con distancia mínima entre 3 ciudades inválidas (api, csv, mock) | a) Api que usa el servicio sea pública. <br> b) Acceso al csv con la información.<br> c) Tener el mock seteado a las ciudades de St marmero, Ghotar y Elden. | 1. Instanciar los servicios de ubicación (api, csv, mock). <br> 2. Ingresar tres ciudades y países inválidos o la misma ciudad 2 veces. <br> 3. Ejecutar función de test. | Ciudades: <br> 1. Lima, Perú. <br> 2. Las Vegas, Estados Unidos <br> 3. Lima, Perú | Ciudades más cercanas: Lima - Las Vegas |