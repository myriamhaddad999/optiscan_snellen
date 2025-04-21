# optiscan_snellen
<h1 align="center">👁️ OptiScan Snellen</h1>
<p align="center">
  A calibrated vision screening app using the Snellen chart and machine learning 🧠
</p>

---

## 📝 Overview

**OptiScan Snellen** is a screen-calibrated web application that simulates a standard Snellen eye chart. Users sit 50 cm away from the screen, read letters, input results, and receive a diagnosis prediction (e.g., **Myopia**, **Hyperopia**, **Presbyopia**, or **Normal**) powered by a trained machine learning model.

✅ Built with Flask  
✅ Responsive HTML/CSS interface  
✅ Docker-ready  
✅ Inspired by real optometrist workflows

---

## 🧠 Key Features

- 📐 **Screen Calibration** via credit card fitting for accurate letter scaling
- 🔡 **Snellen Letter Chart** displayed based on actual size for 50 cm distance
- 📊 **ML Model Prediction** using `line_read`, `mistakes`, and `age`
- 🐳 **Fully Dockerized**: run with just two commands

---

## 🧪 Live Demo (Local)

> Make sure Docker is installed on your system

```bash
git clone https://github.com/myriamhaddad999/optiscan_snellen.git
cd optiscan_snellen
docker build -t snellen-app .
docker run -p 5000:5000 snellen-app
