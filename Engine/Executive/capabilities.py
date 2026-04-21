import os
import json

def save_to_output(filename: str, content: str) -> str:
    """
    Saves the generated content to the Engine/Outputs directory.
    """
    outputs_dir = os.path.join(os.path.dirname(__file__), "..", "Outputs")
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        
    filepath = os.path.join(outputs_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    return f"Successfully saved to {filepath}"

# Tool schema for Anthropic API
SAVE_TO_OUTPUT_TOOL = {
    "name": "save_to_output",
    "description": "Saves a generated draft or finished copy to the Outputs directory so the user can review it. Use this anytime you are asked to generate copy.",
    "input_schema": {
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "The name of the markdown file to save, e.g. 'kirkland-buzz-blog.md'."
            },
            "content": {
                "type": "string",
                "description": "The absolute raw markdown copy/text you generated."
            }
        },
        "required": ["filename", "content"]
    }
}
