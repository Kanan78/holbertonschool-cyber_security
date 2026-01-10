# Wireshark Basics Project

## 📌 Description
This project introduces **Wireshark**, a powerful network protocol analyzer, and demonstrates how to use **Wireshark display filters** to analyze captured network packets.  
The goal is to understand packet structures, protocols, and traffic behavior without relying on external resources.

---

## 🎯 Learning Objectives
By completing this project, you should be able to explain **without using Google**:

- What Wireshark is and why it is used
- How to use Wireshark display filters
- How to analyze a captured packet using Wireshark
- How to read and interpret packets (IP, TCP, UDP, ICMP)

---

## 📚 Resources
Read or watch the following:

- TCP/IP Packet Formats and Ports  
- Wireshark Filters  
- Working With Captured Packets  
- Examine a Captured Packet Using Wireshark  
- How to Read Packets in Wireshark  

---

## 🛠 Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All scripts are tested on **Kali Linux**
- A `README.md` file is mandatory at the root of the project
- You are free to choose any IP address for testing
- All filters must be written in **`.txt` format**
- All files must:
  - Contain **at least two lines**
  - End with a **new line**

---

## ⚙️ Installation

If Wireshark is not installed, use the following commands:

```bash
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark
sudo usermod -aG wireshark $USER

