import gradio as gr
from module_name import BackendClass

backend = BackendClass()

def action_one():
    result = backend.method_one()
    return result

def action_two():
    result = backend.method_two()
    return result

def action_three():
    result = backend.method_three()
    return result

with gr.Blocks() as demo:
    output = gr.Textbox()
    with gr.Row():
        btn1 = gr.Button("Action One")
        btn1.click(action_one, outputs=output)
        btn2 = gr.Button("Action Two")
        btn2.click(action_two, outputs=output)
        btn3 = gr.Button("Action Three")
        btn3.click(action_three, outputs=output)

demo.launch()