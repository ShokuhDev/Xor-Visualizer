<div align="center">

# 🔐 XOR Visualizer

### A colorful Python CLI tool for XOR encryption/decryption with step-by-step binary visualization

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-CLI-black?style=for-the-badge&logo=gnubash)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## ✨ Overview

**XOR Visualizer** is a simple but educational command-line tool built with **Python** that lets you:

- 🔒 Encrypt text using XOR
- 🔓 Decrypt text using the same key
- 👀 Watch each XOR operation in **binary**
- 🎨 Enjoy a colorful terminal interface
- 🧠 Learn how XOR works step by step

This project is perfect for beginners who want to understand **bitwise operations**, **binary logic**, and basic **CLI app design**.

---

## 🚀 Features

- ✅ XOR encryption
- ✅ XOR decryption
- ✅ Step-by-step binary visualization
- ✅ HEX-based encrypted output for safe display
- ✅ Supports keys from `0` to `255`
- ✅ Colorful terminal UI
- ✅ Beginner-friendly code structure

---

## 🖼️ Preview
```text
╔══════════════════════════════════════════════╗
║                                              ║
║                 XOR TOOL                     ║
║                                              ║
╚══════════════════════════════════════════════╝

### Example Output

text
Input text: HelloWorld
Key: 255
Encrypted HEX: 92908c9d9a8d
Decrypted text: HelloWorld

---

## 🧠 How XOR Works

XOR is a bitwise operation:

text
A ⊕ K = B
B ⊕ K = A

That means:

- if you encrypt data with a key,
- and then apply XOR again using the **same key**,
- you recover the original data.

### Binary Example

text
01101101   (m)
11111111   (255)
────────
10010010

Apply XOR with `255` again:

text
10010010
11111111
────────
01101101   (m)

---

## 📦 Installation

Clone the repository:

bash
git clone https://github.com/your-username/xor-visualizer.git
cd xor-visualizer

Run the program:

bash
python xor.py

> Make sure **Python 3** is installed on your system.

---

## 🖥️ Usage

When you start the tool, you’ll see:

text
1. Encrypt
2. Decrypt
3. Exit

### 🔒 Encrypt
- Enter plain text
- Choose a key from `0` to `255`
- Receive encrypted output in **HEX**

### 🔓 Decrypt
- Enter encrypted HEX
- Enter the same key
- Get the original text back

---

## 🧪 Demo

### Encrypting
text
Text: HelloWorld
Key: 255

### Result
text
Encrypted HEX: 92908c9d9a8d

### Decrypting
text
HEX: 92908c9d9a8d
Key: 255

### Output
text
HelloWorld

---

## 📚 Why This Project?

This project is useful for:

- 🎓 Learning XOR encryption
- 🧮 Understanding binary operations
- 🐍 Practicing Python
- 🖥️ Building terminal-based tools
- 🔍 Visualizing bit-level transformations

---

## ⚠️ Disclaimer

This project is made for **educational purposes** and **demonstration**.

Using a single fixed XOR key is **not secure for real-world encryption**.  
It is great for learning, but not for protecting sensitive data.

---

## 🛠️ Tech Stack

- **Python 3**
- `os`
- `time`

---

## 📌 Project Structure

bash
xor-visualizer/
│
├── xor.py
└── README.md

---

## 🌟 Future Improvements

- [ ] File encryption/decryption
- [ ] Base64 output support
- [ ] Adjustable animation speed
- [ ] Better terminal UI
- [ ] Multi-byte key support
- [ ] Export encrypted results to file

---

## 🤝 Contributing

Contributions are welcome!

If you have ideas, improvements, or fixes:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Made with ❤️ by **Your Name**

- GitHub: [@your-username](https://github.com/your-username)

---

<div align="center">

## ⭐ If you like this project, give it a star!

</div>
