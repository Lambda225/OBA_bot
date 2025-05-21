# Importation des librairies nécessaire
from model import asr, tts, detect_intention
#model_intent, tokenizer_intent, intent_labels, 
import torch
import soundfile as sf



# Fonction de traitement complet 1
def process_audio_local(audio_path):
    # 1. Transcription (ASR - Whisper)
    result = asr(audio_path, return_timestamps=True)
    audio_text = result["text"]
    print("Texte reçu :", audio_text)

    # 2. Détection de l'Intention (BERT)
    inputs = detect_intention(audio_text, return_tensors="pt")
    #outputs = model_intent(**inputs)
    #predicted_label = torch.argmax(outputs.logits, dim=1).item()
    #detected_intent = intent_labels[predicted_label]
    print("Intention détectée :", inputs["labels"][0])
    detected_intent = inputs["labels"][0]

    # 3. Génération de Réponse (GPT)
    response_text = f"Vous avez demandé : {detected_intent}."
    print("Réponse générée :", response_text)

     # 4. Synthèse Vocale (TTS - Suno/Bark)
    audio_output = tts(response_text)
    print("Structure de l'audio_output:", audio_output)

    # Extraction des données audio
    audio_data = audio_output["audio"]
    sf.write("response_audio.wav", audio_data[0], 24000)  # 24000 Hz, selon la structure de sortie de Suno/Bark

    print("Audio généré : response_audio.wav")

    return "response_audio.wav"