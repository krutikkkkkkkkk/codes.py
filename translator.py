# pip install googletrans==3.1.0a0
while True:
    from googletrans import Translator
    translator = Translator()
    text = input("\nEnter Text: ")
    lang = input("From Detected Language To: ")
    translation = translator.translate(text, dest=lang)
    translated = translation.text
    print(translated)
