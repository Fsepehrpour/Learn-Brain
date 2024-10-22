import os
import streamlit as st


def main():
    st.title('LearnBrain')

    # Create a mapping of options to filenames
    options = [
        "LF.jpg",
        "LF1.jpg",
        "RF.jpg",
        "RF1.jpg",
    ]

    # Create a selection box for the user to choose an image
    user_input = st.radio("Choose one of the tasks below:", options)

    # Get the selected image filename
    image_file = user_input

    # Create a full path to the image
    sub_directory = "images"
    image_path = os.path.join(os.getcwd(), sub_directory, image_file)

    # Check if the image file exists
    if os.path.exists(image_path):
        # Load and display the image
        image = Image.open(image_path)
        st.image(image, caption=image_file)
    else:
        st.error(f"Error: The file '{image_file}' does not exist in the directory '{image_path}'.")

if __name__ == "__main__":
    main()
    
