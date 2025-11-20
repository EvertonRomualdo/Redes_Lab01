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
'''

# Dados de teste
test_data = "1010100000001111110000010101010111000"

print(f"Criando arquivos de teste para: {test_data}")

# NRZ
nrz_signal = util.encode_nrz(test_data)
sf.write('teste_nrz.wav', nrz_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_nrz.wav criado")

# Manchester
manchester_signal = util.encode_manchester(test_data)
sf.write('teste_manchester.wav', manchester_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_manchester.wav criado")

original_data = test_data

print(f"\nDados originais: {original_data}")
print(f"Número de bits: {len(original_data)}\n")

# Testa decodificação NRZ
print("1. Decodificando NRZ:")
nrz_audio, _ = sf.read('teste_nrz.wav')
decoded_nrz = util.decode_nrz(nrz_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_nrz}")
print(f"Correto: {original_data == decoded_nrz}\n")

# Testa decodificação Manchester
print("3. Decodificando Manchester:")
manchester_audio, _ = sf.read('teste_manchester.wav')
decoded_manchester = util.decode_manchester(manchester_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_manchester}")
print(f"Correto: {original_data == decoded_manchester}")

'''

#------Meus testes dos labs-------

#Como eu sei quantos bits tem?:
    # Tem n bits por segundo. então em uma arquivo com n segundos tem n bits.
#Como sei que tipo de decodificação foi usada?
    #1)Foi usado manchester porque a alteração de frequencia no meio do bit
    #2)O codigo retorna "?" quando não indifica a transição 
#Como sei se o dado ta correto???
    #Se a quantidade de bits é 16 e o sample rate é padrão, não a ruido então o algoritmo não deve falhar


num_bits = 16
print("\n1. Decodificando NRZ dados_123110292:")
nrz_audio, _ = sf.read('dados_123110292_44100hz.wav')
decoded_nrz = util.decode_nrz(nrz_audio, num_bits)
print(f"Decodificado: {decoded_nrz}")

print("\n3. Decodificando Manchester dados_123110292:")
manchester_audio, _ = sf.read('dados_123110292_44100hz.wav')
#quero ver se ele indica falha ou bit desconhecido, debug = true;
decoded_manchester = util.decode_manchester(manchester_audio, num_bits,SAMPLE_RATE,True)
print(f"Decodificado: {decoded_manchester}")

#O grafico comfirma que é manchester devido as 2 picos em 1 segundo
util.plot_signal(manchester_audio, 'Sinal de audio Manchester', num_bits)

DECODED_RESULT = decoded_manchester
print("\no sinal decodificado é:", decoded_manchester)

#valores encontrados
#0010101110101100
#0010101110101100

