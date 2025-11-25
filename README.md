# Agentic Presentation Deck Generator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![API](https://img.shields.io/badge/Gemini-API-orange)
![License](https://img.shields.io/badge/license-MIT-green)

An AI-powered system that creates professional PowerPoint presentations from a simple topic or description. This project uses a team of specialized AI agents to plan, write, critique, and generate polished `.pptx` slide decks automatically.

---

1.  **User Input:** You provide a topic (and optional context).
2.  **Planning:** The *Outline Agent* drafts the deck structure.
3.  **Drafting:** The *Content Agent* writes the text for each slide.
4.  **Refinement:** The *Critic Agent* polishes the text.
5.  **Assembly:** The *PPTX Generator* builds the final `.pptx` file.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following:

* **Python 3.8+** installed.
* A **Google Cloud Project** with the [Gemini API enabled](https://ai.google.dev/).
* A valid **Google Gemini API Key**.

---

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/agentic-presentation-generator.git](https://github.com/yourusername/agentic-presentation-generator.git)
    cd agentic-presentation-generator
    ```

2.  **Set up a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory and add your API key:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

---

## 💻 Usage

Run the `main.py` script from the command line.

### Basic Usage
```bash
python main.py --topic "The Future of AI in Healthcare"

### Advanced Usage
```bash
python main.py --topic "Remote Work Culture" --slides 4 --instructions "Include a slide specifically about 'Zoom Fatigue' and use a humorous tone."

### Optional Arguments
--topic: (Required) The subject matter of the presentation.
--audience: (Optional) The target audience (default: General).
--tone: (Optional) The desired tone (default: Professional).
--slides: (Optional) Number of slides (default: 8).
--instructions: (Optional) Custom instructions for the Content Agent.
--images: (Optional) Generate images for the slides.
--output: (Optional) Filename for the saved PPTX (defaults to presentation.pptx).

### Project Structure
├── src/
│   ├── agents/          # Logic for Outline, Content, and Critic agents
│   └── utils/           # PPTX generation utilities
├── main.py              # Entry point of the application
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed to version control)
└── README.md            # Project documentation