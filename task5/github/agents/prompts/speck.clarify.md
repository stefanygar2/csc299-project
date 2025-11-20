AssignmentsManager: Clarified
============================

This document summarizes and explains the AssignmentsManager class in simple terms. For full details, see the source code in `task5/src/tasks_manager.py` and related tests.

---

**What is AssignmentsManager?**
- A Python class that helps you manage assignments (tasks) for courses or projects.
- It stores assignments in a JSON file, lets you add, complete, delete, and link assignments, and keeps everything organized.

**Key Features**
- Add new assignments with title, course, due date, priority, and notes.
- Mark assignments as complete.
- Delete assignments (removes them and cleans up any links).
- Link assignments together (for prerequisites or related tasks).
- List assignments sorted by due date.
- Validate assignment priority (must be 1–5).
- Save all changes to a file so nothing is lost.

**How do I use it?**
1. Create an instance: `am = AssignmentsManager()`
2. Add assignments: `am.add_assignment("Title", "Course", "YYYY-MM-DD", priority, "Notes")`
3. Complete assignments: `am.complete_assignment(assignment_id)`
4. Delete assignments: `am.delete_assignment(assignment_id)`
5. Link assignments: `am.add_link(source_id, target_id)`
6. List assignments: `am.list_assignments()`
7. Get linked assignments: `am.get_linked_titles(assignment_id)`

**Where is the data stored?**
- In `task5/data/assignments.json`. All changes are saved automatically.

**What is a link?**
- A way to connect one assignment to another (for example, "Task B depends on Task A").
- Linked assignments are tracked by their IDs.

**What happens if I delete an assignment that others link to?**
- The manager automatically removes those links from other assignments.

**What if I set an invalid priority?**
- The Assignment model will raise an error if priority is not between 1 and 5.

---

**FAQ**

Q: Can I add assignments with custom fields?
A: The main fields are title, course, due date, priority, and notes. You can add notes in markdown format.

Q: How do I find an assignment by ID?
A: Use `am.get_assignment(assignment_id)`.

Q: Can I link an assignment to itself?
A: No, the manager prevents self-linking.

Q: What happens if I add the same link twice?
A: Duplicate links are ignored; each link is unique.

Q: How do I see all assignments sorted by due date?
A: Use `am.list_assignments()`; it returns them earliest first.

Q: How do I persist changes?
A: All changes are saved automatically to the JSON file.

Q: Where do I find the full code and tests?
A: See `task5/src/tasks_manager.py` for the class and `task5/tests/test_tasks_manager.py` for examples.

---

If you want more details, code examples, or a step-by-step tutorial, let me know and I’ll expand this file.
