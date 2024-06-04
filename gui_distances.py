import gradio as gr
from ubicacion_interface import ubicacion_interface
from ubicacion_api import ubicacion_api
from ubicacion_csv import ubicacion_csv
from ubicacion_mock import ubicacion_mock


from math import sin, cos, sqrt, atan2, radians

def calc_distance(city_1, country_1, city_2, country_2, service):
    if service == "csv":
        ubicacion_1 = ubicacion_csv()
        ubicacion_2 = ubicacion_csv()
    elif service == "mock":
        ubicacion_1 = ubicacion_mock()
        ubicacion_2 = ubicacion_mock()
    elif service == "api":
        ubicacion_1 = ubicacion_api()
        ubicacion_2 = ubicacion_api()

    ubicacion_1.get_location(city_1, country_1)
    latitud_1 = float(ubicacion_1.get_latitud())
    longitud_1 = float(ubicacion_1.get_longitud()) 

    ubicacion_2.get_location(city_2, country_2)
    latitud_2 = float(ubicacion_2.get_latitud())
    longitud_2 = float(ubicacion_2.get_longitud())

    # Convertir las coordenadas de grados a radianes
    lat1, lon1 = radians(latitud_1), radians(longitud_1)
    lat2, lon2 = radians(latitud_2), radians(longitud_2)

    # Fórmula del haversine para calcular la distancia entre dos puntos en la Tierra
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371  # Radio de la Tierra en kilómetros
    dist = r * c

    return f"{dist:.2f} km"

with gr.Blocks() as demo:
    gr.Markdown("# App para calcular la distancia entre dos ciudades")
    gr.Markdown("Si se usa csv el pais, escribir el nombre en ingles")
    inp = gr.Textbox(label="Ciudad 1", placeholder="Introduce la primera ciudad")
    inp2 = gr.Textbox(label="País 1", placeholder="Introduce el país de la primera ciudad")
    inp3 = gr.Textbox(label="Ciudad 2", placeholder="Introduce la segunda ciudad")
    inp4 = gr.Textbox(label="País 2", placeholder="Introduce el país de la segunda ciudad")
    inp5 = gr.Radio(["csv", "mock", "api"], label="Servicio")
    out = gr.Label(label="Distancia")
    button = gr.Button(value="Calcular")
    
    # Conectar el botón a la función calc_distance
    button.click(calc_distance, inputs=[inp, inp2, inp3, inp4, inp5], outputs=out)

if __name__ == "__main__":
    demo.launch()
