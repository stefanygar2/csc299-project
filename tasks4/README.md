# HOW TO RUN 
cd tasks4/

uv run python __main__.py

# Disclamer 
I dont know if I understood the prompt for tasks4 but it works and used openAI

# DISCUSSION HAD 
Create a robust Python class that enables a student to manage separate school and work schedules, supporting adding, removing, and displaying schedule items for both. Ensure clarity, high code quality (function structure, comments, variable names), and include a loop (such as an interactive menu or repeated processing). The implementation must be readily testable (as with uv test) and not require extraneous user input during testing.

## Key Details & Requirements
- **Class Design**: One Python class managing both school and work schedules, each as a separate list or data structure.
- **Functionality**:
  - `add_item`: Add a schedule item (identify target: "school" or "work").
  - `remove_item`: Remove an item from either schedule by index or other identifier.
  - `display_schedule`: List all items for either or both schedules.
  - Support a loop in some form (interactive menu or iterate over items).
- **Code Quality**:
  - Clear, descriptive variable and function names.
  - Proper and consistent use of function definitions.
  - Sufficient inline comments explaining major parts of the code.
- **Testing/uv test compatibility**:
  - Logic should be easily testable: avoid embedded infinite loops, input() prompts, or print/output that blocks testing frameworks.
  - Any menu or loop for interactive use should be clearly separable from core logic.
- **Output**: Provide a single, clean Python code file containing the class with all required methods, and (optionally) a brief demo or example of use that is easily excluded or commented out for tests.

## Output Format
- Output the result as one continuous Python script (not in a code block), no additional text.
- Code should be sufficiently commented and self-contained.
- If demonstrations or interactive menus are included, make it clear how they can be bypassed or commented for `uv test` compatibility.

## Example (Abbreviated, placeholder names and logic)
Example input:
[none—code-only task]

Example output:
[Python script containing the class, functions/methods, and (optional) main usage TINY demo. Example demo code should be minimal and is not expected to be comprehensive for real test cases—the full logic should be accessible via clean class methods.]

---

**Important:**  
- Produce a single, self-contained, well-commented Python script with the class, methods, and any minimal demos made easy to remove or bypass for automated tests.
- Prioritize code clarity, proper structuring, and comments.
- A loop (such as a menu or process repeatedly over schedule items) must be shown in some part of the code.  
- NO extraneous wrapping text; output ONLY the script.
