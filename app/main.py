import gradio as gr

def diagnosticar(codigos_dtc, modelo, año):
    return f"Diagnóstico para {modelo} {año} con DTC: {codigos_dtc}"

interfaz = gr.Interface(
    fn=diagnosticar,
    inputs=[
        gr.Textbox(label="Códigos DTC (ej: P0300, P0171)"),
        gr.Textbox(label="Modelo del vehículo"),
        gr.Number(label="Año del vehículo")
    ],
    outputs="text",
    title="VantyxAuto – Diagnóstico con IA",
    description="Ingresa los códigos DTC, modelo y año del vehículo para recibir un informe técnico generado por inteligencia artificial."
)

if __name__ == "__main__":
    interfaz.launch()