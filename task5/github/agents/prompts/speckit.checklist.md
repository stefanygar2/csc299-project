
# TaskManager Feature & Quality Checklist

Use this checklist to validate that TaskManager meets its requirements and delivers a reliable assignment management experience.

## Core Features
- [ ] Can add assignments with title, course, due date, priority, and notes
- [ ] Validates priority (must be between 1 and 5)
- [ ] Persists assignments to `assignments.json`
- [ ] Can mark assignments as complete
- [ ] Can delete assignments and clean up links
- [ ] Can link assignments (source → target)
- [ ] Prevents self-linking and duplicate links
- [ ] Lists assignments sorted by due date
- [ ] Retrieves linked assignment titles and IDs
- [ ] Handles persistence across instances (reloads data, maintains next_id)
- [ ] Provides clear error messages for invalid operations
- [ ] All changes are automatically saved
- [ ] Includes thorough unit tests for all major functions

## Quality & Validation
- [ ] All required fields are present and validated
- [ ] Data integrity is maintained after add, update, delete, and link operations
- [ ] Error handling is robust and user-friendly
- [ ] Code is documented and easy to maintain
- [ ] Tests cover edge cases and typical workflows

## Optional (Advanced)
- [ ] Supports markdown notes for assignments
- [ ] Can export or import assignments
- [ ] Integrates with other tools or agents
- [ ] Checklist is updated after major changes

---

_If you want this checklist expanded or tailored to a specific workflow, let me know and I’ll update the file._
