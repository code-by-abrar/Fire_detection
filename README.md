# 🔥 Real-Time Fire & Smoke Hazard Detection System (YOLOv8)

<div align="center">

[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blue.svg?style=for-the-badge)](https://ultralytics.com)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C.svg?style=for-the-badge&logo=pytorch)](https://pytorch.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg?style=for-the-badge)](https://opencv.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**An early-warning disaster prevention model identifying active fire flames and smoke plumes in video surveillance streams with near-zero false alarms.**

</div>

---

## 📌 Project Overview

Early detection is paramount to mitigating devastating fire outbreaks. This computer vision system leverages fine-tuned **YOLOv8** to monitor CCTV video feeds in industrial plants, residential complexes, and forests, generating instant alerts when flame or smoke signatures appear.

---

## 🎯 Classes & Detection Performance

- 🔥 **Fire / Flame**: Localizes active flame pockets even in small early-stage clusters.
- 💨 **Smoke**: Detects expanding smoke plumes in open air and indoor settings.

---

## ⚡ Features

- **⚡ Low-Latency Inference**: Operates in real-time on standard GPU/CPU hardware.
- **🎥 Stream Processing**: Tested on full-length hazard videos (`fire_pro.mp4`).
- **🏋️ Complete Training Pipeline**: Includes `train.py` for retraining on customized environmental datasets.

---

## 🛠️ Usage

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Real-Time Detection**:
   ```bash
   python detect.py --weights model/best.pt --source fire_pro.mp4
   ```

3. **Train Custom Model**:
   ```bash
   python train.py
   ```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
