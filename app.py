from IPython.display import Audio, display
from fonction import process_audio_local


audio_path = "C:/Users/bcisse/Downloads/Enregistrement (3).mp3"
generated_audio = process_audio_local(audio_path)
print("Audio généré :", generated_audio)


# Lecture de l'audio généré
display(Audio("response_audio.wav", autoplay=True))