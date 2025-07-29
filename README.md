🚀 Prompt-to-Website Generator
Generate and preview custom websites (HTML, CSS, JS) from natural language prompts using Google's Gemini Flash 1.5 model. Built with Python and Streamlit.

🖼️ Features
🧠 AI-Powered Code Generation (HTML, CSS, JS) via Gemini Flash 1.5

🌐 Live Preview of Generated Website

💾 Download HTML, CSS, JS Files Individually

📦 Download Entire Website as ZIP

⚡ Streamlit UI for easy interaction

🔐 .env file support for secure API key usage

📁 Project Structure
prompt-to-website/
│
├── app.py # Main Streamlit app
├── templates/
│ ├── gemini_utils.py # Gemini API logic + response parsing
│ ├── file_utils.py # Save/load HTML/CSS/JS files
│ └── download_zip.py # Create ZIP for website download
├── generated_sites/ # Stores generated files temporarily
├── .env # Your Gemini API key
└── README.md

🔧 Setup Instructions

1. Clone the Repo
   git clone
   cd prompt-to-website
2. Install Dependencies
   pip install -r requirements.txt
3. Create .env File
   GEMINI_API_KEY=your_gemini_api_key_here

▶️ Run the App
streamlit run app.py
