# Agentic Presentation Deck Generator

This application uses a team of AI agents to generate professional PowerPoint presentations from a simple topic or description.

## Features

- **Outline Agent**: Generates a structured outline for the presentation.
- **Content Agent**: Expands the outline into detailed slide content.
- **Critic Agent**: Reviews and refines the content for quality and flow.
- **PPTX Generator**: Creates a formatted `.pptx` file.

## Prerequisites

- Python 3.8+
- A Google Cloud Project with the Gemini API enabled.
- An API Key for Google Gemini.

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**:
    Create a `.env` file in the root directory and add your Google API Key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage

Run the application using `main.py`:

```bash
python main.py --topic "Your Presentation Topic" --output "filename.pptx"
```

### Arguments

- `--topic`: (Required) The topic or brief description of the presentation.
- `--output`: (Optional) Output filename. Defaults to `presentation.pptx`.
- `--audience`: (Optional) Target audience (e.g., "Executives", "Students"). Defaults to "General".
- `--tone`: (Optional) Presentation tone (e.g., "Professional", "Inspiring"). Defaults to "Professional".
- `--slides`: (Optional) Desired number of slides.
- `--context_file`: (Optional) Path to a text file containing additional context.
- `--images`: (Optional) Enable AI image generation for slides.

### Examples

**Basic:**
```bash
python main.py --topic "The Future of AI"
```

**Enterprise:**
```bash
python main.py --topic "Cybersecurity Strategy" --audience "Board of Directors" --tone "Urgent and Strategic" --slides 5 --images
```

## Project Structure

- `main.py`: Entry point.
- `src/agents/`: AI agents (Outline, Content, Critic, Image).
- `src/utils/`: Utilities (PPTX Generator).
- `requirements.txt`: Dependencies.

