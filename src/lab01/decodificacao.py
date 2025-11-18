#--Configurações
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from scipy import signal
import time

import utilFunctions as util
output_device = 5
input_device = 1
sd.default.device = (input_device, output_device) # pyright: ignore[reportAttributeAccessIssue]

##
## Configurações globais do exercio
##
SAMPLE_RATE = 44100  # Taxa de amostragem do audio
BIT_DURATION = 1.0   # 1 segundo por bit
FREQ_LOW = 440       # bit '0' (Lá)
FREQ_HIGH = 880      # bit '1' (Lá oitava)

#-------------Codigo do notebook ----------------

# Dados de teste
test_data = "1010100000001111110000010101010111000"

print(f"Criando arquivos de teste para: {test_data}")

# NRZ
nrz_signal = util.encode_nrz(test_data)
sf.write('Redes_Lab01/teste_nrz.wav', nrz_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_nrz.wav criado")

# Manchester
manchester_signal = util.encode_manchester(test_data)
sf.write('Redes_Lab01/teste_manchester.wav', manchester_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_manchester.wav criado")

original_data = test_data

print(f"\nDados originais: {original_data}")
print(f"Número de bits: {len(original_data)}\n")

# Testa decodificação NRZ
print("1. Decodificando NRZ:")
nrz_audio, _ = sf.read('Redes_Lab01/teste_nrz.wav')
decoded_nrz = util.decode_nrz(nrz_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_nrz}")
print(f"Correto: {original_data == decoded_nrz}\n")

# Testa decodificação Manchester
print("3. Decodificando Manchester:")
manchester_audio, _ = sf.read('Redes_Lab01/teste_manchester.wav')
decoded_manchester = util.decode_manchester(manchester_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_manchester}")
print(f"Correto: {original_data == decoded_manchester}")

#------Meus testes dos labs-------

#Como eu sei quantos bits tem?
#Como sei que tipo de decodificação foi usada?
#Como sei se o dado ta correto???


print("\n1. Decodificando NRZ dados_123110292:")
nrz_audio, _ = sf.read('Redes_Lab01/dados_123110292_44100hz.wav')
decoded_nrz = util.decode_nrz(nrz_audio, len(original_data))
print(f"Decodificado: {decoded_nrz}")

print("\n3. Decodificando Manchester dados_123110292:")
manchester_audio, _ = sf.read('Redes_Lab01/dados_123110292_44100hz.wav')
decoded_manchester = util.decode_manchester(manchester_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_manchester}")
print(f"Correto: {original_data == decoded_manchester}")

