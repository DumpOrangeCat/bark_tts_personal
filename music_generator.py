import numpy as np

def create_background_music(duration_seconds):
    # Tạo âm thanh nhạc nền đơn giản (tone sóng sine)
    sr = 24000
    t = np.linspace(0, duration_seconds, int(sr * duration_seconds), False)
    freq = 440  # A note
    music = 0.1 * np.sin(2 * np.pi * freq * t)
    return music.astype(np.float32)
