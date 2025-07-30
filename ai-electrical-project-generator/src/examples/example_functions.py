# example_functions.py

def example_generate_project():
    """
    Example function to demonstrate how to generate an electrical project
    based on a natural language prompt.
    """
    prompt = "Create a lighting circuit for a small office."
    structured_data = parse_prompt(prompt)
    project_data = generate_project(structured_data)
    print("Generated Project Data:", project_data)

def example_draw_diagram():
    """
    Example function to demonstrate how to draw a project diagram.
    """
    project_data = {
        'name': 'Office Lighting Circuit',
        'components': ['Light Fixture', 'Switch', 'Wiring'],
        'layout': 'Basic layout for an office lighting circuit.'
    }
    draw_diagram(project_data, file_format='DXF')
    print("Diagram drawn successfully.")

def example_validate_project():
    """
    Example function to demonstrate project validation against standards.
    """
    project_data = {
        'name': 'Office Lighting Circuit',
        'components': ['Light Fixture', 'Switch', 'Wiring']
    }
    is_valid = validate_project(project_data)
    print("Is the project valid according to NBR 5410?", is_valid)