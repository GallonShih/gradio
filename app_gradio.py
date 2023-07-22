import gradio as gr

max_textboxes = 10

css = """
.imageItem {
height: 100px;
min-width: 400px !important;
max-width: 400px !important;
}
"""

def variable_outputs(k):
    k = int(k)
    return [gr.ImageMask.update(visible=True)]*k + [gr.ImageMask.update(visible=False)]*(max_textboxes-k)

with gr.Blocks(css=css) as demo:
    s = gr.Slider(1, max_textboxes, value=max_textboxes, step=1, label="How many imagesboxes to show:")
    imagesboxes = []
    with gr.Row():
        for i in range(max_textboxes):
            t = gr.ImageMask(label=f"Image {i}", show_label=True, elem_classes='imageItem').style(height=256, width=256)
            imagesboxes.append(t)

    s.change(variable_outputs, s, imagesboxes)

demo.launch()