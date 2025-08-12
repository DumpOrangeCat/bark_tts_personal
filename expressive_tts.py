import numpy as np

def apply_expression(audio, speed=1.0):
    # Thay đổi tốc độ phát audio (đơn giản)
    from scipy.signal import resample
    n_samples = int(len(audio) / speed)
    return resample(audio, n_samples)
