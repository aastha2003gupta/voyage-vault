import streamlit as st
from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

st.title("Language Translator")

text_to_translate = st.text_area("Enter text to translate")

languages = {
    'Auto':'auto',
    'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy',
    'Assamese': 'as', 'Aymara': 'ay', 'Azerbaijani': 'az', 'Bambara': 'bm', 'Basque': 'eu',
    'Belarusian': 'be', 'Bengali': 'bn', 'Bhojpuri': 'bho', 'Bosnian': 'bs', 'Bulgarian': 'bg',
    'Catalan': 'ca', 'Cebuano': 'ceb', 'Chinese (Simplified)': 'zh-CN', 'Chinese (Traditional)': 'zh-TW',
    'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dhivehi': 'dv',
    'Dogri': 'doi', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et',
    'Ewe': 'ee', 'Filipino (Tagalog)': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy',
    'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Guarani': 'gn',
    'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he',
    'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig',
    'Ilocano': 'ilo', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja',
    'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw',
    'Konkani': 'gom', 'Korean': 'ko', 'Krio': 'kri', 'Kurdish': 'ku', 'Kurdish (Sorani)': 'ckb',
    'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lingala': 'ln',
    'Lithuanian': 'lt', 'Luganda': 'lg', 'Luxembourgish': 'lb', 'Macedonian': 'mk',
    'Maithili': 'mai', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt',
    'Maori': 'mi', 'Marathi': 'mr', 'Meiteilon (Manipuri)': 'mni-Mtei', 'Mizo': 'lus',
    'Mongolian': 'mn', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no',
    'Nyanja (Chichewa)': 'ny', 'Odia (Oriya)': 'or', 'Oromo': 'om', 'Pashto': 'ps',
    'Persian': 'fa', 'Polish': 'pl', 'Portuguese (Portugal, Brazil)': 'pt', 'Punjabi': 'pa',
    'Quechua': 'qu', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Sanskrit': 'sa',
    'Scots Gaelic': 'gd', 'Sepedi': 'nso', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn',
    'Sindhi': 'sd', 'Sinhala (Sinhalese)': 'si', 'Slovak': 'sk', 'Slovenian': 'sl',
    'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv',
    'Tagalog (Filipino)': 'tl', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te',
    'Thai': 'th', 'Tigrinya': 'ti', 'Tsonga': 'ts', 'Turkish': 'tr', 'Turkmen': 'tk',
    'Twi (Akan)': 'ak', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz',
    'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo',
    'Zulu': 'zu'
}

src_language = st.selectbox("Select source language", options=list(languages.keys()))  
dest_language = st.selectbox("Select destination language", options=list(languages.keys())) 
if st.button("Translate"):
    if text_to_translate:
        src_lang_code = languages[src_language]
        dest_lang_code = languages[dest_language]
        translated_text = translate_text(text_to_translate, src_lang_code, dest_lang_code)
        st.write(f"Translated text: {translated_text}")
    else:
        st.write("Please enter text to translate")
