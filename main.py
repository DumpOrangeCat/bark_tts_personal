from bark import generate_audio, preload_models    
import soundfile as sf    
import os    
    
def main():    
    # 1. Load model Bark    
    print("🔄 Loading Bark models...")    
    preload_models()    
    print("✅ Models loaded!")    
    
    # 2. Đọc văn bản từ text.txt    
    text_file = "text.txt"    
    if not os.path.exists(text_file):    
        raise FileNotFoundError(f"❌ Không tìm thấy file {text_file}")    
    
    with open(text_file, "r", encoding="utf-8") as f:    
        text_prompt = f.read().strip()    
    
    if not text_prompt:    
        raise ValueError("❌ text.txt rỗng, hãy thêm văn bản để đọc.")    
    
    # 3. Sinh audio từ văn bản    
    print("🎤 Generating speech...")    
    try:    
        audio_array = generate_audio(text_prompt)    
    except Exception as e:    
        raise RuntimeError(f"❌ Lỗi khi sinh audio: {e}")    
    
    # 4. Lưu file    
    output_path = "output.wav"    
    sf.write(output_path, audio_array, samplerate=24000)    
    print(f"✅ Done! Audio saved to {output_path}")    
    
if __name__ == "__main__":    
    main()
