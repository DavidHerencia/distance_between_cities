import gradio as gr
from city_distance import calc_distance
from min_city_distance import min_distance


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
    
    gr.Markdown("# Ciudades con la menor distancia entre ellas (3 ciudades)")
    
    inp6 = gr.Textbox(label="Ciudad 1", placeholder="Introduce la primera ciudad")
    inp7 = gr.Textbox(label="País 1", placeholder="Introduce el país de la primera ciudad")
    inp8 = gr.Textbox(label="Ciudad 2", placeholder="Introduce la segunda ciudad")
    inp9 = gr.Textbox(label="País 2", placeholder="Introduce el país de la segunda ciudad")
    inp10 = gr.Textbox(label="Ciudad 3", placeholder="Introduce la tercera ciudad")
    inp11 = gr.Textbox(label="País 3", placeholder="Introduce el país de la tercera ciudad")
    inp12 = gr.Radio(["csv", "mock", "api"], label="Servicio")
    out2 = gr.Label(label = "Ciudades con la menor distancia entre ellas")
    button2 = gr.Button(value="Calcular")
    
    # Conectar el botón a la función calc_distance
    button.click(calc_distance, inputs=[inp, inp2, inp3, inp4, inp5], outputs=out)
    button2.click(min_distance, inputs=[inp6, inp7, inp8, inp9, inp10, inp11, inp12], outputs=out2)

if __name__ == "__main__":
    demo.launch()
