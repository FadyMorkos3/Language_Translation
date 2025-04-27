from googletrans import Translator

def translate_text():
    # Initialize the Translator object
    translator = Translator()
    
    # Get user input for text and target language
    text = input("Enter text to translate: ")
    dest_language = input("Enter destination language (e.g., 'fr' for French, 'es' for Spanish): ")

    # Perform translation
    translation = translator.translate(text, dest=dest_language)

    # Output the result
    print(f"Translated text: {translation.text}")

# Run the function
if __name__ == "__main__":
    translate_text()
