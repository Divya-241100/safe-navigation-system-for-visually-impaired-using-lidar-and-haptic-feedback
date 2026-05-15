# Safe Navigation System for Visually Impaired using LiDAR and Haptic Feedback (Raspberry Pi)

## 📌 Overview
This project is a real-time embedded assistive navigation system developed using Raspberry Pi and LiDAR sensor. It is designed to help visually impaired users detect obstacles and navigate safely using haptic (vibration) and audio feedback.

The system continuously scans the environment, processes distance data, and provides instant alerts when an obstacle is detected within a defined threshold.

---

## ⚙️ Features
- Real-time obstacle detection using LiDAR sensor  
- Distance measurement and environmental scanning  
- Haptic (vibration) feedback system  
- Audio buzzer alert system  
- Low-latency embedded processing  
- Portable assistive navigation design  

---

## 🧠 Technologies Used
- Raspberry Pi (3/4/Zero W)  
- LiDAR Sensor (UART-based)  
- Python  
- Embedded Linux  
- GPIO Interface  
- Serial Communication (pyserial)  
- RPi.GPIO library  

---

## 🏗️ System Architecture
- **Sensor Layer:** LiDAR collects distance data from surroundings  
- **Processing Layer:** Raspberry Pi processes real-time sensor data  
- **Output Layer:** Buzzer and vibration motor provide feedback to user  

---

## 🔄 Working Principle
1. LiDAR continuously scans the environment  
2. Raspberry Pi reads distance data via serial communication  
3. System checks obstacle proximity against threshold  
4. If obstacle is detected:
   - Vibration motor activates  
   - Buzzer provides audio alert  
5. User receives instant feedback for safe navigation  

---

## 🧾 File Structure
