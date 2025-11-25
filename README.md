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

- `--topic`: (Required) The topic or brief description of the presentation you want to generate.
- `--output`: (Optional) The filename for the generated PowerPoint file. Defaults to `presentation.pptx`.

### Example

```bash
python main.py --topic "The Future of Artificial Intelligence in Healthcare" --output "ai_healthcare.pptx"
```

## Project Structure

- `main.py`: Entry point of the application.
- `src/agents/`: Contains the AI agent implementations (Outline, Content, Critic).
- `src/utils/`: Contains utility scripts like the PPTX generator.
- `requirements.txt`: List of Python dependencies.
