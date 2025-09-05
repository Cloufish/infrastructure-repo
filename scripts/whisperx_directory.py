import os
import whisperx

# -------- Settings --------
input_dir = "/media/Emby/TV_Series/Jerks"
output_dir = input_dir
extensions = [".mp3", ".wav", ".m4a", ".mp4", ".flac", ".mkv"]
model_name = "large-v3"
device = "cuda"
language = "de"

# -------- Helpers --------
def format_timestamp(seconds: float) -> str:
    """Convert seconds to SRT timestamp format: HH:MM:SS,mmm"""
    milliseconds = int(seconds * 1000)
    hours = milliseconds // 3600000
    minutes = (milliseconds % 3600000) // 60000
    seconds = (milliseconds % 60000) // 1000
    ms = milliseconds % 1000
    return f"{hours:02}:{minutes:02}:{seconds:02},{ms:03}"

# -------- Setup --------
os.makedirs(output_dir, exist_ok=True)

# Load WhisperX model 
model = whisperx.load_model(model_name, device)

# -------- Process Files --------
for root, _, files in os.walk(input_dir):
    files.sort()
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            filepath = os.path.join(root, file)
            relpath = os.path.relpath(filepath, input_dir)
            base_name = os.path.splitext(relpath)[0]
            out_path = os.path.join(output_dir, base_name + ".srt")
            os.makedirs(os.path.dirname(out_path), exist_ok=True)

            print(f"🔊 Transcribing: {filepath}")
            audio = whisperx.load_audio(filepath)
            result = model.transcribe(audio)

            # (Optional) align
            model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
            result_aligned = whisperx.align(result["segments"], model_a, metadata, audio, device)

            # Save SRT
            with open(out_path, "w", encoding="utf-8") as f:
                for i, seg in enumerate(result_aligned["segments"], start=1):
                    start_time = format_timestamp(seg["start"])
                    end_time = format_timestamp(seg["end"])
                    text = seg["text"].strip()
                    f.write(f"{i}\n{start_time} --> {end_time}\n{text}\n\n")

            print(f"✅ Saved: {out_path}")

