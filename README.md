# 🎙️ Podcast Q&A Bot with Smart Video-Timestamp Redirection

An intelligent, context-aware Retrieval-Augmented Generation (RAG) system built completely from scratch.

This application downloads full-length podcast media, transcribes and indexes conversations with highly accurate timestamp mappings using AI, and allows users to query the content naturally.

The bot not only generates analytical answers using **Puter AI's Serverless Inference Framework (`gpt-4o-mini`)**, but also automatically launches the user's browser directly at the **exact second** where the topic was discussed in the video.

---

# 🏗️ Technical Architecture Workflow

The system follows a modular 3-phase pipeline architecture:

```text
┌────────────────────┐
│ 1. AUDIO EXTRACTION │
│      (yt-dlp)       │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ 2. AI TRANSCRIPTION │
│      (Whisper)      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ 3. CONTEXTUAL Q&A   │
│   (Puter AI LLM)    │
└────────────────────┘
```

### Workflow Breakdown

### 1️⃣ Audio Extraction

Automated extraction of high-quality podcast audio streams directly from YouTube using `yt-dlp`.

### 2️⃣ Temporal Transcription

The downloaded audio is processed locally using OpenAI's Whisper neural network to generate highly accurate timestamped transcript segments.

The structured transcript is stored as:

```bash
transcript_segments.json
```

### 3️⃣ Retrieval & AI Synthesis

Custom retrieval logic scans transcript chunks, identifies relevant context windows, and forwards them into **Puter AI's `gpt-4o-mini` model** for response synthesis.

### 4️⃣ Browser Timestamp Redirection

The application computes the exact timeline offset and automatically launches the browser with YouTube timestamp parameters:

```bash
?t=<seconds>
```

This instantly redirects the user to the exact moment where the discussion occurred.

---

# ⚙️ Why FFmpeg is Required

## What is FFmpeg?

**FFmpeg** is an industry-standard multimedia framework used for:

* Audio decoding
* Video processing
* Media conversion
* Stream extraction
* Encoding & transcoding

---

## Why does this project need FFmpeg?

When `yt-dlp` downloads media from YouTube, the content often arrives as fragmented audio/video streams.

FFmpeg acts as the backend processor that:

* Combines fragmented streams
* Extracts clean audio
* Converts media into usable formats like `.mp3`
* Ensures Whisper receives valid audio input

Without FFmpeg installed and configured in the system PATH, the pipeline will fail before transcription begins.

---

# 🛠️ Installation & Setup Guide

# 1️⃣ Install FFmpeg

Choose the installation method according to your operating system.

---

## 🪟 Windows

1. Download FFmpeg builds from:
   https://www.gyan.dev/ffmpeg/builds/

2. Extract the downloaded archive.

3. Rename the extracted folder to:

```text
ffmpeg
```

4. Move it to:

```text
C:\ffmpeg
```

5. Open:

```text
Edit the system environment variables
```

6. Edit the `Path` system variable and add:

```text
C:\ffmpeg\bin
```

7. Restart your terminal or IDE.

---

## 🍏 macOS

Install using Homebrew:

```bash
brew install ffmpeg
```

---

## 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg -y
```

---

# 2️⃣ Python Environment Setup

Clone the repository and create a virtual environment.

```bash
# Clone repository
git clone https://github.com/rehan1608/podcast-qa-bot.git

# Move into project
cd podcast-qa-bot

# Create virtual environment
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## Install Required Dependencies

```bash
pip install yt-dlp openai-whisper requests
```

---

# 🚀 Execution Pipeline

Run the project sequentially through the following steps.

---

## Step 1️⃣ Download Podcast Audio

```bash
python download.py
```

This downloads and extracts the podcast audio locally.

---

## Step 2️⃣ Generate Timestamped Transcripts

```bash
python transcribe.py
```

Whisper processes the audio and creates structured timestamp segments.

---

## Step 3️⃣ Launch the Q&A Engine

```bash
python bot.py
```

The bot will:

* Accept user questions
* Retrieve relevant transcript chunks
* Generate contextual AI answers
* Automatically open the browser at the exact discussion timestamp

---

# 🔬 Engineering Resilience & Fault Tolerance

## ✅ Serverless AI Architecture

The project leverages Puter AI's serverless inference infrastructure, eliminating:

* API key management
* Billing complexity
* Traditional rate-limit barriers

---

## ✅ Graceful Failure Handling

Custom exception handling ensures resilience against:

* API downtime
* Network interruptions
* Unexpected response structures
* Remote inference failures

If the LLM becomes unavailable, the system gracefully falls back to local transcript context retrieval while still preserving timestamp-based browser redirection.

---

# 📂 Project Structure

```text
podcast-qa-bot/
│
├── download.py
├── transcribe.py
├── bot.py
├── transcript_segments.json
├── requirements.txt
└── README.md
```

---

# 🧠 Technologies Used

* Python
* OpenAI Whisper
* yt-dlp
* FFmpeg
* Puter AI
* JSON-based Retrieval Pipeline

---

# 🌟 Key Features

✅ AI-powered podcast question answering
✅ Accurate timestamp extraction
✅ Automatic browser timestamp launching
✅ Local Whisper transcription
✅ Context-aware retrieval pipeline
✅ Serverless LLM integration
✅ Fault-tolerant architecture
✅ Lightweight and modular design

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

Developed with passion for AI systems, retrieval engineering, and intelligent automation.
