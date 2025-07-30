# AI Electrical Project Generator

## Overview
The AI Electrical Project Generator is an application designed to automatically generate electrical projects based on natural language prompts. By leveraging artificial intelligence, this tool interprets user input and produces structured electrical project data, adhering to relevant standards.

## Project Structure
```
ai-electrical-project-generator
├── src
│   ├── main.py
│   ├── ai
│   │   ├── __init__.py
│   │   └── generator.py
│   ├── electrical
│   │   ├── __init__.py
│   │   └── project_builder.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── examples
│       └── example_functions.py
├── requirements.txt
├── README.md
└── setup.py
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd ai-electrical-project-generator
pip install -r requirements.txt
```

## Usage
To generate an electrical project, run the main application:

```bash
python src/main.py
```

### Example Functionality
1. **Natural Language Prompt Parsing**: The application can interpret prompts like "Create a lighting project for a 1000 sq ft office" and convert them into structured data.
2. **Project Generation**: Based on the parsed data, the application generates a complete electrical project, including diagrams and compliance checks.
3. **Diagram Drawing**: The generated project can be visualized in DXF or SVG formats.

## Modules
- **ai**: Contains the logic for interpreting prompts and generating projects.
- **electrical**: Handles the specifics of electrical project creation and validation.
- **utils**: Provides utility functions for logging and file operations.
- **examples**: Contains example functions demonstrating the usage of the application.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.