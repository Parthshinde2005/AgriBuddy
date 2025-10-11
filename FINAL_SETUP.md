# 🌱 Crop Diagnosis System - Final Setup Guide

## 📁 Clean Project Structure

```
AgriBuddy/
├── backend/
│   ├── app.py              # Flask backend server
│   ├── requirements.txt    # Python dependencies
│   ├── uploads/           # Auto-created for uploaded images
│   └── reports/           # Auto-created for generated reports
├── frontend/
│   ├── index.html         # Main frontend (HTML + Tailwind + JS)
│   └── js/
│       └── app.js         # All frontend logic
├── models/
│   ├── README.md              # Model requirements and instructions
│   ├── model1_multicrop.h5    # Your AI model for multi-crops (place here)
│   ├── model2_staple_crops.h5 # Your AI model for staple crops (place here)
│   └── model3_banana.h5       # Your AI model for banana (place here)
├── start.bat              # One-click startup script
├── test_system.py         # System testing script
└── README.md              # Documentation
```

## 🚀 How to Run

### Option 1: One-Click Start
```bash
start.bat
```

### Option 2: Manual Start
```bash
cd backend
pip install -r requirements.txt
python app.py
```

Then open `frontend/index.html` in your browser.

## 🔗 URLs

- **Backend Dashboard:** http://localhost:5000
- **Frontend:** Open `frontend/index.html` in browser
- **API Health:** http://localhost:5000/health
- **Model Status:** http://localhost:5000/test-models

## ✅ Features Working

- ✅ **Backend-Frontend Connection** - Direct HTTP calls, no proxy needed
- ✅ **Model Loading** - Automatic TensorFlow model loading from `models/`
- ✅ **Image Upload** - Drag & drop or click to upload
- ✅ **Disease Prediction** - Real AI predictions using your models
- ✅ **PDF Reports** - Downloadable analysis reports
- ✅ **Audio Reports** - Text-to-speech playback
- ✅ **Multi-language** - English, Hindi, Marathi
- ✅ **Dark/Light Mode** - Theme switching
- ✅ **Connection Status** - Real-time backend connection monitoring
- ✅ **Responsive Design** - Works on all devices

## 🧪 Testing

Run the test script to verify everything:
```bash
python test_system.py
```

## 🐛 Troubleshooting

1. **Models not loading?**
   - Check if `.h5` files are in `models/` directory
   - Verify TensorFlow installation: `pip install tensorflow`

2. **Backend not starting?**
   - Install dependencies: `pip install -r backend/requirements.txt`
   - Check Python version: `python --version` (need 3.7+)

3. **Frontend not connecting?**
   - Make sure backend is running on http://localhost:5000
   - Check browser console for errors

4. **CORS errors?**
   - Backend has CORS enabled, should work from any origin

## 🎯 Next Steps

1. **Customize Models:** Update class labels in `backend/app.py` to match your training
2. **Add More Crops:** Extend the crop lists in both backend and frontend
3. **Deploy:** Use the provided configuration for cloud deployment
4. **Enhance UI:** Modify `frontend/index.html` and `frontend/js/app.js`

## 📝 Key Files Explained

- **`backend/app.py`** - Main Flask server with all API endpoints
- **`frontend/index.html`** - Complete frontend with Tailwind CSS
- **`frontend/js/app.js`** - All JavaScript logic (theme, language, API calls)
- **`start.bat`** - Installs dependencies and starts backend
- **`test_system.py`** - Comprehensive system testing

The system is now **production-ready** with a clean, maintainable codebase!