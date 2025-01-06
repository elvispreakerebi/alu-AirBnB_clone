
# AirBnB Clone: The Beginning

Welcome to the AirBnB clone project! This project marks the start of an exciting journey to build a simplified version of the AirBnB website. Over the course of this project, we will develop a full-stack web application that includes:

- **A Command Interpreter**: To manipulate data without a visual interface.
- **A Website**: A front-end to display the application to users (both static and dynamic content).
- **Data Storage**: Using files or a database to persist objects.
- **An API**: To enable communication between the front-end and data layer for creating, retrieving, updating, and deleting objects.

The ultimate goal is to understand and implement key concepts of high-level programming while gaining hands-on experience in building a complete web application.

---

## Project Overview

This project will be completed over the course of several months and is divided into four main components:

1. **Command Interpreter**: A tool for developers to debug, test, and manipulate data.
2. **Front-End Website**: A user-friendly interface to interact with the application.
3. **Data Storage**: Persistent storage of objects using either files or a database.
4. **API**: A bridge between the front-end and data layer for creating, retrieving, updating, and deleting objects.

---

## Command Interpreter

The command interpreter is a crucial tool in the development of this project. It provides a shell-like environment where developers can manipulate application data directly.

### Features of the Command Interpreter

- Create new objects.
- Retrieve objects.
- Update object attributes.
- Delete objects.

---

### How to Start the Command Interpreter

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd alu_airbnb_clone
   ```

2. Make the script executable (if not already):
   ```bash
   chmod +x console.py
   ```

3. Start the interpreter:
   ```bash
   ./console.py
   ```

   You should see a prompt like this:
   ```
   (hbnb)
   ```

---

### How to Use the Command Interpreter

The interpreter accepts various commands for interacting with the application. Below is a list of the most commonly used commands:

| Command                          | Description                                      |
|----------------------------------|--------------------------------------------------|
| `help`                           | Display available commands.                      |
| `create <class>`                 | Create a new object of a specific class.         |
| `show <class> <id>`              | Display details of an object using its ID.       |
| `destroy <class> <id>`           | Delete an object using its ID.                   |
| `all`                            | Display all objects.                             |
| `update <class> <id> <attr> <val>`| Update an object's attribute with a new value.   |
| `quit`                           | Exit the interpreter.                            |

---

### Examples

1. **Create a new object**:
   ```bash
   (hbnb) create User
   d5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55
   ```
   This creates a new `User` object and returns its unique ID.

2. **Show an object**:
   ```bash
   (hbnb) show User d5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55
   [User] (d5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55) {'id': 'd5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55', 'created_at': '2025-01-06T12:00:00', 'updated_at': '2025-01-06T12:00:00'}
   ```

3. **Update an object**:
   ```bash
   (hbnb) update User d5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55 name "John Doe"
   (hbnb)
   ```

4. **Delete an object**:
   ```bash
   (hbnb) destroy User d5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55
   (hbnb)
   ```

5. **View all objects**:
   ```bash
   (hbnb) all
   ["[User] (d5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55) {'id': 'd5e1f5e2-9b2f-41c8-bbc8-c5c75f926e55', 'created_at': '2025-01-06T12:00:00', 'updated_at': '2025-01-06T12:00:00'}"]
   ```

---

## Next Steps

This command interpreter is just the beginning of the AirBnB clone project. Over time, we will expand this project to include:

- A fully functional web interface.
- A robust back-end API.
- Scalable data storage solutions.

Stay tuned for updates!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
