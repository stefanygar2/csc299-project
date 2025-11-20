# TaskManager Actionable Tasks

This file lists the key development, validation, and maintenance tasks for TaskManager. Use these to guide implementation and ensure all requirements are met.

## Development Tasks
- [ ] Design the Assignment data model (title, course, due date, priority, notes)
- [ ] Implement add_assignment function
- [ ] Implement priority validation (1–5)
- [ ] Implement persistence to `assignments.json`
- [ ] Implement complete_assignment function
- [ ] Implement delete_assignment with link cleanup
- [ ] Implement add_link and prevent self-linking/duplicates
- [ ] Implement list_assignments sorted by due date
- [ ] Implement get_linked_titles and IDs
- [ ] Ensure persistence across instances (reload and next_id)
- [ ] Implement error handling for invalid operations
- [ ] Auto-save changes after every operation

## Validation & Testing Tasks
- [ ] Write unit tests for all major functions
- [ ] Test edge cases (invalid priority, missing fields, circular links)
- [ ] Test data integrity after add, update, delete, and link operations
- [ ] Test error messages and user feedback
- [ ] Test markdown notes support

## Maintenance & Advanced Tasks
- [ ] Document all functions and usage
- [ ] Add support for export/import of assignments
- [ ] Integrate with other tools or agents if needed
- [ ] Update checklist and tasks after major changes
