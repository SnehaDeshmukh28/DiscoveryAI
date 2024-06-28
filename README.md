# DiscoveryAI - AI-Powered Research and Writing Agents

Unlock the power of AI to discover groundbreaking technologies and craft compelling tech stories. Our agents use Google's Gemini language models to deliver insightful research and engaging content.

## Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/SnehaDeshmukh28/DiscoveryAI.git
   cd DiscoveryAI
   ```

2. **Set up your environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Add your API key:**
   - Create a `.env` file with:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key
     SERPER_API_KEY=your_serper_api_key
     ```

4. **Run the script:**
   ```bash
   python crew.py
   ```

## Meet the Agents

### Senior Researcher
- **Mission**: Uncover the next big trend in tech.
- **Output**: Detailed reports on cutting-edge innovations.
- **Attributes**: Curious, innovative, allows delegation.

### Writer
- **Mission**: Craft engaging articles on tech trends.
- **Output**: Easy-to-read, captivating tech stories.
- **Attributes**: Simplifies complex topics, no delegation.

## How It Works

- **Research Task**: Identifies tech trends and assesses their impact.
- **Writing Task**: Produces insightful articles formatted in markdown.

## Environment Setup

Add your Google API key in a `.env` file:

```plaintext
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_serper_api_key
```

## Contact

For questions or suggestions, feel free to contact us at [deshmusn@gmail.com](mailto:deshmusn@gmail.com).
