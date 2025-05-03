from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from langdetect import detect

# Load Spam Classifier Model
checkpoint_path = "../Outputs/roberta_detector_outputs/checkpoint-7660"  # Adjust if different
tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint_path)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Language to Translation Model Mapping
language_model_map = {
    'es': "Helsinki-NLP/opus-mt-es-en",  # Spanish → English
    'fr': "Helsinki-NLP/opus-mt-fr-en",  # French → English
    'de': "Helsinki-NLP/opus-mt-de-en",  # German → English
    'it': "Helsinki-NLP/opus-mt-it-en",  # Italian → English
    'pt': "Helsinki-NLP/opus-mt-pt-en",  # Portuguese → English
}

# Cache translators so you don't re-load every time
translators_cache = {}

def get_translator_for_lang(lang_code):
    if lang_code not in translators_cache:
        model_name = language_model_map.get(lang_code)
        if model_name:
            translators_cache[lang_code] = pipeline("translation", model=model_name)
        else:
            translators_cache[lang_code] = None  # No translator available
    return translators_cache[lang_code]

# Set up Flask app
app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def reply():
    incoming_msg = request.form.get('Body')

    # Detect language
    try:
        lang = detect(incoming_msg)
        print(f"🌐 Detected language: {lang}")
    except Exception as e:
        print(f"Language detection failed: {e}")
        lang = "en"  # Assume English if unknown

    # If not English and supported, translate
    if lang != "en" and lang in language_model_map:
        translator = get_translator_for_lang(lang)
        if translator:
            try:
                translated_text = translator(incoming_msg, max_length=400)[0]['translation_text']
                print(f"📝 Original: {incoming_msg}")
                print(f"🔄 Translated: {translated_text}")
            except Exception as e:
                print(f"Translation failed: {e}")
                translated_text = incoming_msg  # fallback to original
        else:
            translated_text = incoming_msg
    else:
        translated_text = incoming_msg

    # Classify the (translated) message
    result = classifier(translated_text)[0]
    label = result['label']
    score = result['score']

    # Interpret label
    is_spam = label.lower() in ['label_1', 'spam']

    # Confidence calculation
    confidence_pct = int(score * 100)
    rounded_conf = confidence_pct - (confidence_pct % 5)
    if rounded_conf > 95 and confidence_pct < 100:
        rounded_conf = 95
    if confidence_pct == 100:
        rounded_conf = 100

    # Build response
    if is_spam:
        flags = "🚩" * (1 if rounded_conf < 90 else 2 if rounded_conf == 95 else 3)
        response_text = f"This message is most likely **spam**.\nConfidence level: {rounded_conf}%. {flags}"
    else:
        response_text = f"This message is most likely **safe**.\nConfidence level: {rounded_conf}%. ✅"

    print(f"🔍 Processed message: '{incoming_msg}' -> {response_text}")

    # Send WhatsApp response
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run()
