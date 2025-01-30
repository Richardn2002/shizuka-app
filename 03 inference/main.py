from MoeGoe import Model

from scipy.io.wavfile import write
import os

model = Model(os.path.join(os.path.dirname(__file__), 'models/alpha'))

sample_rate, data = model.inference(0, '[JA]あなた, ごじぶんのことばかりですのね[JA]')

write('test.wav', sample_rate, data)

input('Audio has been generated and written to test.wav, press enter to exit and ignore the error messages, they are pyopenjtalk not cleaning up properly:')
