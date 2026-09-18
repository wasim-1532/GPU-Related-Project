# 🚗 Smart GPU-Based Parking Gateway

> **An Asynchronous, Non-Blocking Load-Balanced System for Real-Time Parking Slot Allocation**

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0%2B-009688.svg)
![Deployment](https://img.shields.io/badge/Deployed%20on-Render-informational.svg)

---

## 📌 Overview

The **Smart GPU-Based Parking Gateway** is an asynchronous architecture designed to eliminate bottlenecks in high-concurrency automated parking systems. By using a **Least-Connection Gateway Router**, incoming vehicle camera feeds and booking requests are dynamically assigned to the least-loaded simulated GPU node (`GPU-1`, `GPU-2`, `GPU-3`). 

Users receive an **Instant Token/Job ID** (0ms blocking time), while heavy vision processing tasks execute asynchronously in the background.

---

## ⚡ Key Features

* 🚀 **Non-Blocking Architecture**: Instant HTTP response generation using FastAPI `BackgroundTasks`.
* ⚖️ **Least-Connection Load Balancer**: Dynamically routes traffic based on active requests and free slot availability.
* 🛡️ **Hard GPU Throttling**: Limits concurrent requests to **Max 4 requests per GPU** to prevent node saturation.
* 📊 **Real-Time Visual Dashboard**: Live UI displaying parking capacities, active requests, and statuses (🟢 AVAILABLE / 🔴 FULL).
* 🔄 **System State Reset**: Built-in state clearing mechanism to easily reset all parking zones and memory logs.

---

## 🏗️ Project Architecture & Folder Structure

```text
smart_parking_system/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI Server & API Routes
│   ├── load_balancer.py     # Gateway Least-Load Routing Logic
│   └── gpu_workers.py       # Simulated GPU Nodes & Parking Capacity
│
├── static/
│   └── index.html           # Live Interactive UI Dashboard
│
├── requirements.txt         # Project Dependencies
└── README.md                # Documentation
