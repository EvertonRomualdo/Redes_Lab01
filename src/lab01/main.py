
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from scipy import signal
import time

import  utilFunctions as util
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


test_bits = "11001"
print(f"Dados originais: {test_bits}\n")

# Testa cada modulação
print("1. NRZ:")
nrz_signal = util.encode_nrz(test_bits,debug=True)

print("\n3. Manchester:")
manchester_signal = util.encode_manchester(test_bits,debug=True)

#util.plot_signal(nrz_signal,'NRZ',len(test_bits))

sd.play(manchester_signal, SAMPLE_RATE)
sd.wait()

#sd.play(nrz_signal, SAMPLE_RATE)
#sd.wait()

