import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, AutoModelForCausalLM

# 🔧 Chargement des modèles
asr = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
tts = pipeline("text-to-speech", model="suno/bark")

# Chargement de BERT pour les intentions bancaires
model_name_intent = "bert-base-uncased"
tokenizer_intent = AutoTokenizer.from_pretrained(model_name_intent)
model_intent = AutoModelForSequenceClassification.from_pretrained(model_name_intent)

# Chargement de GPT pour la génération de texte
tokenizer_gpt = AutoTokenizer.from_pretrained("gpt2")
model_gpt = AutoModelForCausalLM.from_pretrained("gpt2")