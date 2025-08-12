from bark import generate_audio, preload_models, save_as_prompt
import soundfile as sf
from music_generator import create_background_music
from expressive_tts import apply_expression
from voice_cloning import get_voice_prompt
from utils import read_text_file

def main():
    print("Loading Bark models...")
    preload_models()

    text = read_text_file("text.txt")
    if not text:
        raise ValueError("File text.txt rỗng!")

    # Giả sử có mẫu giọng trong voice_prompt.wav
    voice_prompt = get_voice_prompt("voice_prompt.wav")  # Tạo semantic voice prompt

    print("Generating expressive speech...")
    audio = generate_audio(text, history_prompt=voice_prompt)

    audio = apply_expression(audio, speed=1.1)  # Tăng tốc độ 10%

    print("Adding background music...")
    music = create_background_music(duration_seconds=len(audio)/24000)
    mixed_audio = audio + music * 0.3  # Trộn nhạc nền với âm thanh chính

    output_path = "output.wav"
    sf.write(output_path, mixed_audio, 24000)
    print(f"Done! Audio saved to {output_path}")

if __name__ == "__main__":
    main()
