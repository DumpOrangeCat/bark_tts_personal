#!/usr/bin/env python3
"""
generate_tts.py

Tạo giọng nói từ văn bản bằng Bark (CPU).
Hỗ trợ:
- Delay giữa các đoạn đọc
- Đọc từ file .txt hoặc prompt trực tiếp
"""

import argparse
import soundfile as sf
from bark import SAMPLE_RATE, generate_audio

def main():
    parser = argparse.ArgumentParser(description="Bark TTS (CPU) cá nhân")
    parser.add_argument("--prompt", type=str, help="Văn bản cần đọc")
    parser.add_argument("--input_file", type=str, help="Đường dẫn file .txt")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay (giây) trước khi đọc")
    parser.add_argument("--output", type=str, default="output.wav", help="Tên file .wav xuất")
    args = parser.parse_args()

    # Lấy nội dung
    if args.input_file:
        with open(args.input_file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    elif args.prompt:
        text = args.prompt.strip()
    else:
        parser.error("Phải truyền --prompt hoặc --input_file")

    # Thêm delay nếu cần
    if args.delay > 0:
        text = f"[delay]{args.delay} {text}"

    print(f"🗣  Generating audio (delay={args.delay}s)...")
    audio = generate_audio(prompt=text, device="cpu")
    print("✅ Audio generated.")

    sf.write(args.output, audio, SAMPLE_RATE)
    print(f"💾 File đã lưu: {args.output}")

if __name__ == "__main__":
    main()
