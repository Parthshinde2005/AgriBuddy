@echo off
echo ========================================
echo  Crop Diagnosis System - Complete Setup
echo ========================================
echo.

echo 1. Checking Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python first.
    pause
    exit /b 1
)

echo.
echo 2. Checking model files...
set MODEL_COUNT=0

if exist "models\model1_multicrop.h5" (
    echo ✅ Multi-crop model found
    set /a MODEL_COUNT+=1
) else (
    echo ❌ Multi-crop model not found at models\model1_multicrop.h5
)

if exist "models\model2_staple_crops.h5" (
    echo ✅ Staple crop model found
    set /a MODEL_COUNT+=1
) else (
    echo ❌ Staple crop model not found at models\model2_staple_crops.h5
)

if exist "models\model3_banana.h5" (
    echo ✅ Banana model found
    set /a MODEL_COUNT+=1
) else (
    echo ❌ Banana model not found at models\model3_banana.h5
)

echo Found %MODEL_COUNT%/3 model files

if %MODEL_COUNT%==0 (
    echo.
    echo ⚠️  WARNING: No model files found!
    echo    Please place your trained .h5 model files in the models/ directory
    echo    The system will still start but predictions will not work until models are added.
    echo.
    pause
)

echo.
echo 3. Installing backend dependencies...
cd backend
pip install Flask Flask-CORS Pillow reportlab gtts requests python-dotenv tensorflow numpy

echo.
echo 4. Starting backend server...
echo.
echo ✅ Backend will be available at: http://localhost:5000
echo ✅ Frontend will be available at: frontend/index.html
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py