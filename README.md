# Bark TTS (CPU) - Project Cá Nhân

## Giới thiệu
Dự án cá nhân sử dụng **Bark** để tạo giọng nói từ văn bản.
- Chạy hoàn toàn trên CPU.
- Hỗ trợ delay giữa các đoạn đọc.
- Đọc văn bản trực tiếp hoặc từ file `.txt`.

## Yêu cầu
- Python >= 3.8
- Linux hoặc GitHub Codespaces
- Mạng ổn định (lần đầu tải model ~2–3 GB)

## Cài đặt
```bash
# Vào thư mục project
cd bark_tts_personal

# Tạo môi trường ảo
python3 -m venv venv
source venv/bin/activate  # Linux/Codespaces

# Cài thư viện
pip install -r requirements.txt
