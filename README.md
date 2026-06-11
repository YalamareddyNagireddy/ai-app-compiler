# 🧠 AI App Compiler

An AI-powered system that converts natural language application ideas into structured application blueprints.

## 🌐 Live Demo

### Frontend

https://ai-app-compiler-mocha-psi.vercel.app

### Backend API

https://ai-app-compiler-j6t2.onrender.com

### API Documentation

https://ai-app-compiler-j6t2.onrender.com/docs

## Features

* Intent Extraction
* Design Generation
* Schema Generation
* Validation Engine
* Consistency Checking
* Runtime Simulation
* Evaluation Framework

## Tech Stack

* Python
* FastAPI
* HTML
* CSS
* JavaScript
* GitHub
* Render
* Vercel


## 🚀 Overview

AI App Compiler is a full-stack AI system that converts natural language application ideas into structured system architecture.

It uses a **multi-stage pipeline architecture** to transform a simple user prompt into:

- Application intent
- System design
- UI + API schema
- Validation checks
- Runtime simulation output

This project demonstrates how real-world AI engineering systems are built using modular pipelines instead of a single model call.

---

## 🎯 Problem Statement

When users describe an app idea, they often need:

- system structure
- database design
- API endpoints
- UI flow

This project automates that transformation using an AI pipeline approach.

---

## ⚙️ System Architecture

User Prompt  
↓  
Intent Extraction  
↓  
System Design Generator  
↓  
Schema Generator (UI + API + DB)  
↓  
Validation Engine  
↓  
Consistency Checker  
↓  
Runtime Simulator  
↓  
Final Output

---

## 🧠 Core Features

### 🔹 AI Pipeline Engine
- Converts natural language into structured system design
- Multi-stage processing instead of single LLM call

### 🔹 Intent Extraction
- Detects app type, features, and requirements

### 🔹 System Design Generator
- Generates pages, roles, and entities

### 🔹 Schema Generator
- Produces:
  - UI schema
  - API endpoints
  - Database tables

### 🔹 Validation Engine
- Ensures schema correctness

### 🔹 Runtime Simulation
- Simulates system execution behavior

### 🔹 Metrics Tracking
- Logs success rate and latency

### 🔹 Frontend Dashboard
- Interactive UI for generating and visualizing output

---

## 🛠 Tech Stack

**Backend**
- Python
- FastAPI

**Frontend**
- HTML
- CSS
- JavaScript

**Architecture**
- Modular AI pipeline system
- REST API communication

---

## 📦 API Endpoints

### POST `/generate`

Generates full system architecture from a prompt.

**Request:**
```json
{
  "prompt": "Build a CRM with login and dashboard"
}