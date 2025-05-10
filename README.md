# Gemini AI Terminal

Talk to Google's Gemini 2.0 Flash model directly from your terminal.
Lightweight, easy to use, and works on any device with Python installed.


# Features

Chat with Gemini 2.0 Flash instantly.

No browser required — pure terminal experience.

Works on any system with Python 3.8+ installed.

Minimal setup — ready in minutes.


# Requirements

1. Python 3.8 or higher

2. A Gemini API key from Google (https://aistudio.google.com/app/apikey)

3. Internet connection


# Setup

1. Clone the repository
```
git clone https://github.com/JPDeerenberg/Gemini-AI-Terminal
cd Gemini-AI-Terminal
```

3. Install the required packages
```
pip install -r requirements.txt
```
This installs the google-genai package.


3. Set your API key

Set your Gemini API key as an environment variable:
```
export GOOGLE_API_KEY="your-api-key-here"
```
Replace your-api-key-here with your actual API key.

Tip: Add this line to your shell configuration file (such as .bashrc or .zshrc) to load it automatically.


4. Run the AI Terminal
```
python3 Gemini-cli.py
```
Start chatting right away!


# Example

== Gemini AI Terminal ==
```
Say 'exit' to close.
> Hello!
Hi there! How can I assist you today?
> Tell me a fun fact.
Did you know that honey never spoils? Archaeologists have found 3,000-year-old honey in ancient tombs!
> exit
Bye!
```

# License

This project is licensed under MIT; see the file for details.  Feel free to improve, fork, or share it; it's free!

# Notes

Should work on any Linux, macOS, or Windows system with Python installed, but you might need a different approach for Windows with the API key.

Very lightweight — no heavy libraries or frameworks needed.

I am currently working on more features, such as being able to choose more Gemini models, better markup, command history, and a better API system.

# Credits

Made by JPDeerenberg
Powered by Google's Gemini 2.0 Flash model.
