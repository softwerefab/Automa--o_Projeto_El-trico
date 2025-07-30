# This file contains the project builder logic for generating electrical projects based on structured data.

def generate_project(data: dict) -> dict:
    """
    Generates an electrical project based on the provided structured data.
    
    Args:
        data (dict): Structured data containing project specifications.
        
    Returns:
        dict: A dictionary representing the generated electrical project.
    """
    project = {
        "name": data.get("name", "Untitled Project"),
        "components": [],
        "layout": {},
        "standards": ["NBR 5410"]
    }
    
    # Example of adding components based on the input data
    if "components" in data:
        for component in data["components"]:
            project["components"].append({
                "type": component.get("type", "Unknown"),
                "specifications": component.get("specifications", {})
            })
    
    # Example of defining a layout (this would be more complex in a real application)
    project["layout"] = {
        "rooms": data.get("rooms", []),
        "wiring": data.get("wiring", {})
    }
    
    return project