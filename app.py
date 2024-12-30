import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')

def info_page():
    st.title("How to Use the App")
    st.write("""
        This app generates a caption for an uploaded image.
        
        **Steps**:
        1. Navigate to the **Caption Generator** page via the sidebar.
        2. Upload an image using the **Browse files** button.
        3. The caption will be generated and displayed.
    """)

def generate_page():
    img_path = st.file_uploader(label='Image', type=['png', 'jpg', 'jpeg'])

    if img_path is not None:
        st.image(img_path, caption='Uploaded Image')
        image = Image.open(img_path).convert('RGB')

        inputs = processor(image, return_tensors='pt')
        outputs = model.generate(**inputs)

        caption = processor.decode(outputs[0], skip_special_tokens=True)

        st.write(caption)

def main():
    info = st.Page(info_page, title='Home', icon=':material/home:')
    generate = st.Page(generate_page, title='Generate', icon='📃')
    pages = st.navigation([info, generate])
    pages.run()
    
if __name__ == '__main__':
    main()