#--Configurações
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from scipy import signal
import time
import decodificacao as dc

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

#----------Meu codigo------------


# -------------------------Teste manual de limites de falha do ruido -------------------------
print("\nEtapa 3 - Ruido na comunicação")

bits_originais = dc.DECODED_RESULT

snr_NRZ=-3
snr_Manchester=-3

#decodifico a original da matricula para cada modulação
clean_signal_NRZ = util.encode_nrz(bits_originais)
clean_signal_Manchester = util.encode_manchester(bits_originais)

#gero o ruido nos 2 sinais
noisy_signal_NRZ = util.adicionar_ruido(clean_signal_NRZ, snr_NRZ)
noisy_signal_Manchester = util.adicionar_ruido(clean_signal_Manchester, snr_Manchester)

#decodifico a mensagem com ruido
decoded_NRZ = util.decode_nrz(noisy_signal_NRZ, len(bits_originais))
decoded_Manchester = util.decode_manchester(noisy_signal_Manchester, len(bits_originais))

#Relatorio geral
print(f"\nBits Originais: {bits_originais}")

print(f"\nDecodificado_NRZ: {decoded_NRZ}\nDecodificado_Manchester: {decoded_Manchester}")

print(f"\nCorreto_NRZ: {bits_originais == decoded_NRZ}\nCorreto_Manchester {bits_originais == decoded_Manchester}")

#-----------------------------<>--------------------------------------


#------------teste exaustivo e plote do grafico-------------------------
print(f"Testando com {len(bits_originais)} bits: {bits_originais}")

sig_nrz = util.encode_nrz(bits_originais)
sig_man = util.encode_manchester(bits_originais)

# Listas para guardar os resultados do gráfico
valores_snr = range(0, -100, -1)
erros_nrz = []
erros_man = []

#Varia o SNR e testa
for snr in valores_snr:
    #
    nrz_ruidoso = util.adicionar_ruido(sig_nrz, snr)
    man_ruidoso = util.adicionar_ruido(sig_man, snr)
    
    
    rec_nrz = util.decode_nrz(nrz_ruidoso, len(bits_originais))
    rec_man = util.decode_manchester(man_ruidoso, len(bits_originais))
    
    #compara bit a bit com o original
    qtd_erro_nrz = sum(1 for a, b in zip(bits_originais, rec_nrz) if a != b)
    qtd_erro_man = sum(1 for a, b in zip(bits_originais, rec_man) if a != b)
    
    erros_nrz.append(qtd_erro_nrz)
    erros_man.append(qtd_erro_man)

def achar_falhas(nome, lista_erros):
    #Pega o primeiro índice onde erros > 0
    idx_inicio = next((i for i, x in enumerate(lista_erros) if x > 0), -1)
    #Pega o primeiro índice onde erros > 30%
    idx_total = next((i for i, x in enumerate(lista_erros) if x > len(bits_originais)*0.3), -1)
    
    snr_inicio = valores_snr[idx_inicio] if idx_inicio != -1 else "N/A"
    snr_total = valores_snr[idx_total] if idx_total != -1 else "N/A"
    
    print(f"[{nome}] Começa a falhar em: {snr_inicio}dB | Colapso total em: {snr_total}dB")

#relatorio
print("-" * 40)
achar_falhas("NRZ", erros_nrz)
achar_falhas("Manchester", erros_man)
print("-" * 40)

#Plota o grafico
plt.figure(figsize=(10, 5))
plt.plot(valores_snr, erros_nrz, 'b-o', label='NRZ')
plt.plot(valores_snr, erros_man, 'r-s', label='Manchester')

plt.title("Comparação de Erros por Nível de Ruído (SNR)")
plt.xlabel("SNR (dB) - Quanto menor, mais ruído")
plt.ylabel("Número de Erros")
plt.legend()
plt.grid(True)
plt.gca().invert_xaxis()
plt.show()