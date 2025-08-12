from bark import save_as_prompt
import soundfile as sf

def get_voice_prompt(wav_path):
    audio, sr = sf.read(wav_path)
    if sr != 24000:
        raise ValueError("Sampling rate phải là 24000Hz")
    save_as_prompt(audio, "voice_prompt.npz")
    return "voice_prompt.npz"
