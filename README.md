# CollabTask- A Flask based Project Management App
## Overview

The Task Manager Application is a web-based platform designed to streamline task assignment, tracking, and management. It allows users to assign tasks to others, update task statuses, and manage projects collaboratively.

---

## Features

- **Task Assignment**: Assign tasks to individuals with a due date.
- **Role-Based Permissions**:
  - Task creators can edit or delete their tasks.
  - Assigned users can mark tasks as "Done" or "In Progress."
- **Task Status Tracking**: Visualize task statuses as **Active**, **In Progress**, or **Done**.
- **Sorted Views**: Tasks can be sorted by date or title for better organization.
- **Collaborative Dashboard**:
  - View tasks assigned to you.
  - View tasks assigned by you.

---

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Database**: SQLite (or your choice of database)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager

2. **Install Dependencies**: Ensure Python and pip are installed on your system. Then run:
    ```bash
    pip install -r requirements.txt

3. **Populate the Database(Optional)**: Add few Sample users to test out the features
    ```bash
    python users.py

4. **Run the Application**: Start the Flask development server:
    ```bash
    flask run

The application will be available at http://127.0.0.1:5000/.

## Usage

### Add a Task
1. Navigate to the homepage.
2. Fill in the task title, due date, and assignee.
3. Click **"Add Task"** to save it.

### View Tasks
- **Tasks Assigned To You**: View tasks where you are the assignee under the **"Tasks Assigned To You"** section.
- **Tasks Assigned By You**: View tasks you have assigned to others under the **"Tasks Assigned By You"** section.

### Update Task Status
- Users assigned a task can update its status to **"Done"** or **"In Progress"** directly from the actions column in the **Tasks Assigned To You** table.

### Edit or Delete Tasks
- Only the task creator has the permissions to edit or delete tasks in the **Tasks Assigned By You** section.

---

## Tables Overview

### **Tasks Assigned To You**
| Date       | Title              | Assigned By | Status  | Actions                    |
|------------|--------------------|-------------|---------|----------------------------|
| 2024-12-22 | Setup Permissions  | Alice       | Active  | Mark as Done/In Progress   |

### **Tasks Assigned By You**
| Date       | Title               | Assigned To | Status   | Actions        |
|------------|---------------------|-------------|----------|----------------|
| 2024-12-21 | Design Landing Page | Bob         | Active   | Edit/Delete    |

---

## Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests.

---

## Contact

For queries or support, please contact:

- **Name**: Vaibhav Dhumale  
- **GitHub**: [imvbh](https://github.com/imvbh)

---