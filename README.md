# Smart Crop Diagnosis System.

AI-powered crop disease detection system with automatic model selection, PDF reports, and audio features.

## 🚀 Quick Start

1. **Run the system:**
   ```bash
   start.bat
   ```

2. **Open frontend:**
   - Open `frontend/index.html` in your browser
   - Or visit: `file:///path/to/frontend/index.html`

3. **Backend will be running at:**
   - http://localhost:5000

## 📁 Project Structure

```
AgriBuddy/
├── backend/
│   ├── app.py              # Flask backend server
│   ├── requirements.txt    # Python dependencies
│   ├── uploads/           # Uploaded images
│   └── reports/           # Generated reports
├── frontend/
│   ├── index.html         # Main frontend page
│   └── js/
│       └── app.js         # Frontend JavaScript
├── models/
│   ├── model1_multicrop.h5    # Multi-crop AI model
│   ├── model2_staple_crops.h5 # Staple crops AI model
│   └── model3_banana.h5       # Banana AI model
└── start.bat              # One-click startup script
```

## ✨ Features

- 🤖 **Automatic Model Selection** - Chooses the right AI model based on crop type
- 📸 **Image Upload** - Drag & drop or click to upload crop images
- 🔍 **Disease Detection** - Real-time AI-powered disease prediction
- 📄 **PDF Reports** - Downloadable analysis reports
- 🔊 **Audio Reports** - Text-to-speech report playback
- 🌍 **Multi-language** - English, Hindi, Marathi support
- 🌙 **Dark/Light Mode** - Theme switching
- 📱 **Responsive Design** - Works on all devices

## 🌾 Supported Crops

**Multi-Crop Model:** Apple, Cherry, Corn, Grapes, Peach, Orange, Pepper, Potato, Soybean, Raspberry, Strawberry, Tomato

**Staple Crop Model:** Wheat, Maize, Cotton, Sugarcane, Rice

**Banana Model:** Banana

## 🛠️ Tech Stack

- **Backend:** Flask + TensorFlow + Python
- **Frontend:** HTML + CSS (Tailwind) + JavaScript
- **AI Models:** TensorFlow/Keras (.h5 format)
- **Reports:** ReportLab (PDF) + gTTS (Audio)

## 📋 Requirements

- Python 3.7+
- TensorFlow 2.10+
- Modern web browser
- AI model files in `models/` directory
