from bark import generate_audio, preload_models
import soundfile as sf

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def main():
    print("Loading Bark models...")
    preload_models()  # load model

    text = read_text_file("text.txt")
    if not text:
        raise ValueError("File text.txt rỗng!")

    print("Generating speech...")
    audio = generate_audio(text)

    output_path = "output.wav"
    sf.write(output_path, audio, samplerate=24000)
    print(f"Done! Audio saved to {output_path}")

if __name__ == "__main__":
    main()
