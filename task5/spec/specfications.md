# Goal
To provide a student-focused Personal Knowledge Management System (PKMS) tool for organizing and tracking school assignments, rich notes, and the relationships between academic tasks.

# 1  Core Assignment Management (CRUD)

Capture & Create :The system must allow users to create a new assignment with: Title, Course Name (e.g., CS 101), Due Date, and Priority (using number 1-5)

Rich-Text Notes :The system must provide an input area for detailed, rich-text notes stored in Markdown format.

Listing :The default view must display all assignments, primarily sorted by Due Date (soonest first).

Status Update :Users must be able to mark an assignment's status as 'Complete' via a single action.  and when said complete it should separate it 

Deletion: Users must be able to permanently delete an assignment.

# 2. PKMS Interlinking and Retrieval

Interlinking :The system must allow users to link one assignment to any other existing assignment (e.g., linking a 'Draft' to a 'Final Paper'). 

Link Display :When viewing an assignment's details, the system must display the titles of all assignments linked to it as clickable references.

Filtering: The assignment list must be filterable by Course Name, Priority, and Status (Pending/Complete)
