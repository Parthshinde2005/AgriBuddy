@echo off
echo ========================================
echo  Smart Crop Diagnosis System
echo ========================================
echo.

echo 1. Checking system requirements...
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
    echo ❌ Multi-crop model not found
)

if exist "models\model2_staple_crops.h5" (
    echo ✅ Staple crop model found
    set /a MODEL_COUNT+=1
) else (
    echo ❌ Staple crop model not found
)

if exist "models\model3_banana.h5" (
    echo ✅ Banana model found
    set /a MODEL_COUNT+=1
) else (
    echo ❌ Banana model not found
)

echo Found %MODEL_COUNT%/3 model files

echo.
echo 3. Installing/checking dependencies...
cd backend
pip install -q Flask Flask-CORS Pillow reportlab gtts requests numpy==1.24.3 tensorflow==2.13.0

echo.
echo 4. Starting backend server...
echo.
echo ✅ Backend will be available at: http://localhost:5000
echo ✅ Frontend pages available at:
echo    - Main page: frontend/index.html
echo    - Multi-crop: frontend/multicrop.html
echo    - Staple crops: frontend/staple.html
echo    - Banana: frontend/banana.html
echo.
echo 📊 Backend dashboard: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py