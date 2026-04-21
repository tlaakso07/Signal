import os
import sys
import anthropic

# Add standard API key fallback
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
try:
    from API.keys import ANTHROPIC_API_KEY
except ImportError:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

from capabilities import SAVE_TO_OUTPUT_TOOL, save_to_output

class ExecutiveAgent:
    """
    The SDK-Native Executive Agent.
    Role: Read Identity File, generate content, enforce brand compliance, and save output.
    """
    
    def __init__(self, identity_file_path: str):
        self.api_key = os.getenv("ANTHROPIC_API_KEY", ANTHROPIC_API_KEY)
        if not self.api_key:
            raise ValueError("No ANTHROPIC_API_KEY found. Please add to API/keys.py or set via ENV.")
            
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.identity_file_path = identity_file_path
        self.system_prompt = self._load_identity_file()
        
    def _load_identity_file(self) -> str:
        """Loads the Identity File to be used as the permanent system prompt."""
        if not os.path.exists(self.identity_file_path):
            raise FileNotFoundError(f"Identity file not found at: {self.identity_file_path}")
            
        with open(self.identity_file_path, "r", encoding="utf-8") as f:
            identity_content = f.read()
            
        prompt = (
            "You are the Executive Agent for the following brand.\n"
            "Your sole purpose is to act as the autonomous Brand Enforcer and Content Generator. "
            "You will NEVER deviate from the voice, tone, and positioning defined below.\n\n"
            "=== BRAND IDENTITY FILE ===\n"
            f"{identity_content}\n"
            "===========================\n\n"
            "When responding to tasks, embody the persona described perfectly. "
            "Always use the save_to_output tool to save your final drafted content."
        )
        return prompt
        
    def execute_task(self, task_description: str):
        """
        Executes a content generation or auditing task using Claude.
        """
        print(f"[*] Executive Agent Received Task: {task_description}")
        print("[*] Processing with Claude...")
        
        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4000,
            system=self.system_prompt,
            tools=[SAVE_TO_OUTPUT_TOOL],
            messages=[
                {"role": "user", "content": task_description}
            ]
        )
        
        # Check if Claude decided to use a tool
        final_text = ""
        for block in response.content:
            if block.type == "text":
                final_text += block.text + "\n"
                print("\n" + block.text)
            elif block.type == "tool_use":
                if block.name == "save_to_output":
                    filename = block.input["filename"]
                    content = block.input["content"]
                    print(f"\n[*] Tool Call: Saving draft to {filename}...")
                    result = save_to_output(filename, content)
                    print(f"[*] {result}")
                    final_text += f"\n[Saved to {filename}]"
        
        return final_text

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run the Executive Agent natively.")
    parser.add_argument("--task", type=str, required=True, help="The task for the agent to execute.")
    parser.add_argument("--identity", type=str, 
                        default="../../The Brain/CLIENTS/BORED-N-BUZZED-IDENTITY.md",
                        help="Path to the Identity File.")
    
    args = parser.parse_args()
    
    try:
        agent = ExecutiveAgent(identity_file_path=args.identity)
        agent.execute_task(args.task)
    except Exception as e:
        print(f"[-] Error: {e}")
