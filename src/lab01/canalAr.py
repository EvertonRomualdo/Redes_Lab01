import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from scipy import signal
import time

import utilFunctions as util

print(sd.query_devices())
output_device = 5
input_device = 3
sd.default.device = (input_device, output_device) # pyright: ignore[reportAttributeAccessIssue]

##
## Configurações globais do exercio
##
SAMPLE_RATE = 44100  # Taxa de amostragem do audio
BIT_DURATION = 1.0   # 1 segundo por bit
FREQ_LOW = 440       # bit '0' (Lá)
FREQ_HIGH = 880      # bit '1' (Lá oitava)


# test_data = "10110"
# Captura áudio


duracao = 5 * BIT_DURATION + 1  # +1 segundo de margem

#executar essas linhas substituira o arquivo capturado

#audio_capturado = util.capturar_do_microfone(duracao)
#sf.write('captura_microfone.wav', audio_capturado, SAMPLE_RATE)

#use o audio direto:
audio_capturado, _ = sf.read('captura_microfone.wav')


# Tenta decodificar
print("\nTentando decodificar...")
decoded = util.decode_manchester(audio_capturado, 5)
manchester_audio, _ = sf.read('dados_ar.wav')
decoded_manchester = util.decode_manchester(manchester_audio, 5)

print(f"Original: {decoded_manchester}")
print(f"Capturado: {decoded}")
print("acertou: ", decoded_manchester == decoded)   


#Contador de tentativas: 92
