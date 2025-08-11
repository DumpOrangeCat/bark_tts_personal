#!/usr/bin/env python3
"""
preload_bark.py
Tải và cache model Bark TTS trên CPU để lần sau chạy nhanh hơn.
"""

from bark import preload_models

if __name__ == "__main__":
    print("📥 Đang preload model Bark TTS (CPU)...")
    preload_models(device="cpu")
    print("✅ Hoàn tất preload. Model đã lưu ở ~/.cache/suno")
