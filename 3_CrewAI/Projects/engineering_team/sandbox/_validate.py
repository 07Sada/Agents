from app import app

# Validate that the Gradio app constructs without errors
try:
    app
    print("Gradio UI constructed successfully.")
except Exception as e:
    print(f"Error while constructing Gradio UI: {e}")