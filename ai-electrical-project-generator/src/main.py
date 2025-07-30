# This file serves as the entry point of the application. It imports necessary modules and contains a function that demonstrates how to use the project to generate an electrical project based on a natural language prompt.

from ai.generator import generate_project
from prompt_parser import parse_prompt
from normas import validate_project
from cad_drawer import draw_diagram
from utils import log_message, save_to_file

def main():
    # Example natural language prompt
    prompt = "Generate a lighting project for a small office with 10 LED lights."
    
    # Parse the prompt to structured data
    project_data = parse_prompt(prompt)
    
    # Generate the electrical project based on the structured data
    generated_project = generate_project(project_data)
    
    # Validate the generated project against standards
    if validate_project(generated_project):
        log_message("Project validated successfully.")
        
        # Draw the project diagram and save it
        draw_diagram(generated_project, file_format='DXF')
        save_to_file(generated_project, 'project_output.json')
    else:
        log_message("Project validation failed.")

if __name__ == "__main__":
    main()