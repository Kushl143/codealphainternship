from googletrans import Translator

# Create a Translator object
translator = Translator()

# Take user input
text = input("Enter text to translate: ")
target_lang = input("Enter target language (e.g., 'es' for Spanish, 'fr' for French): ")

# Perform translation
translated_text = translator.translate(text, dest=target_lang)

# Show result
print(f"Translated text ({target_lang}): {translated_text.text}")
