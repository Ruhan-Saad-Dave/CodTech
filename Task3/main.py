import gradio as gr
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# --- Model and Preprocessing ---

# Load the pre-trained model from TF Hub (loaded only once)
try:
    model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    print("TensorFlow Hub model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    # Create a dummy model to allow the UI to load without crashing
    model = None

def preprocess_image(image_np):
    """
    Takes a NumPy image, converts it to a TensorFlow tensor,
    and preprocesses it for the model.
    """
    # Gradio provides a uint8 numpy array, convert it to float32 and normalize
    img = tf.convert_to_tensor(image_np, dtype=tf.float32)
    img = img / 255.0

    # The model expects a 4D tensor (batch_size, height, width, channels)
    # Add a batch dimension
    img = img[tf.newaxis, :]
    return img

def stylize_image(content_image_np, style_image_np):
    """
    Applies style transfer to the content image using the style image.
    """
    if model is None:
        # Return a black image with an error message if the model failed to load
        error_img = np.zeros_like(content_image_np)
        print("Model is not available. Returning a black image.")
        return error_img 

    # Preprocess both images
    content_tensor = preprocess_image(content_image_np)
    style_tensor = preprocess_image(style_image_np)

    # Apply the style transfer model
    outputs = model(content_tensor, style_tensor)
    stylized_image = outputs[0]

    # The output is a tensor with a batch dimension. Squeeze it and return as a NumPy array.
    # The values are already in the [0, 1] range, which Gradio handles correctly.
    return np.squeeze(stylized_image)

# --- Gradio Interface ---

description = """
Upload a **Content Image** and a **Style Image**. The model will then combine them,
applying the artistic style of the Style Image to the content of the Content Image.
The generated image will appear in the output box below, and you can download it from there.
"""

demo = gr.Interface(
    fn=stylize_image,
    inputs=[
        gr.Image(label="Content Image", type="numpy"),
        gr.Image(label="Style Image", type="numpy")
    ],
    outputs=gr.Image(label="Stylized Image", type="numpy"),
    title="Neural Style Transfer",
    description=description,
    examples=[
        ["dice.png", "potato.png"]
    ]
)

if __name__ == "__main__":
    demo.launch()
