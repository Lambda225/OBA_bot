import torch
from transformers import pipeline,AutoTokenizer,AutoModelForSequenceClassification
# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, AutoModelForCausalLM

# # 🔧 Chargement des modèles
# asr = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
# tts = pipeline("text-to-speech", model="suno/bark")

# # Chargement de BERT pour les intentions bancaires
# model_name_intent = "bert-base-uncased"
# tokenizer_intent = AutoTokenizer.from_pretrained(model_name_intent)
# model_intent = AutoModelForSequenceClassification.from_pretrained(model_name_intent)

# # Chargement de GPT pour la génération de texte
# tokenizer_gpt = AutoTokenizer.from_pretrained("gpt2")
# model_gpt = AutoModelForCausalLM.from_pretrained("gpt2")

# intent_labels =[
#     'salutation','Demande de sold',"Virement","Ouverture de compte","Fermeture de compte",
# ]

def detect_intention(input_text):
    classifier = pipeline("zero-shot-classification",
                      model="joeddav/xlm-roberta-large-xnli")
    intent_labels =['salutation','Demande de sold',"Virement","Ouverture de compte","Fermeture de compte",]
    print(classifier(input_text, intent_labels))

detect_intention('Bonjour mon ami')

