# Task Manager API
The Task Manager API is an application developed in Python with Django that offers a RESTful interface for managing tasks (todo list). With this API, users can create, view, update and delete tasks, organize tasks into lists, add comments and categorize their tasks for better organization.

## Features
- **User Registration:** Users can register on the platform to start managing their tasks.
- **Task Creation:** Users can create new tasks by providing details such as title, description, due date, and priority.
- **Organization in Lists:** Tasks can be grouped into lists for better organization and management.
- **Task Categorization:** Users can categorize their tasks, allowing filtering and viewing by category.
- **Adding Comments:** Users can add comments to tasks to provide more context or related discussions.
- **Activity History:** All important activities like task creation, marking task as completed, etc. are recorded for tracking and auditing purposes.

## API Structure
The API is structured in a modular way, with dedicated endpoints for each resource (users, tasks, lists, etc.). Each endpoint follows RESTful principles and responds to standard HTTP requests such as GET, POST, PUT and DELETE.

## Structure
```plaintext
task_manager_api/
│
├── task_manager_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
│
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

## Entities
- **User:** A class to represent the users of your application.
- **Task:** A class to represent the tasks to be performed, with fields such as title, description, creation date, completion date, priority, etc.
- **TaskList:** A class for representing task lists, allowing users to group related tasks together.
- **Category:** A class for categorizing tasks if you want to allow users to organize their tasks by categories.
- **Comment:** A class to allow users to add comments to tasks.
- **Auditable:** A class for recording important activities such as task creation, marking task as completed, etc. for auditing and tracking purposes.

## Prerequisites

To configure and run this project, you will need to have installed in your environment:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

## Installation and Use

Follow these instructions to configure and run the project in your local environment:

1. Clone this repository:

```bash
git clone https://github.com/MarcioJCarvalho/task_manager_api.git
```

2. Navigate to the project directory:

```bash
cd task-manager-api
```

3. Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the database migrations:

```bash
python main.py migrate
```

6. Start the development server:

```bash
python main.py runserver
```

7. Access the API in your browser or in a tool like Postman:

```bash
http://localhost:5000/
```

Now you're ready to start using the API!

## Contribution

Contributions are welcome! Feel free to open an issue or send a pull request with improvements, bug fixes or new features.

## Technologies Used
- [Python](https://www.python.org/)
- [Django](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django)
- [Django REST Framework](https://www.django-rest-framework.org/)

## License

This project is licensed under the [MIT License](LICENSE).

**Love Task Manager API? Give our repo a star :star: :arrow_up:.**

Made with :blue_heart: by MÁRCIO :wave: [See my LinkedIn](https://www.linkedin.com/in/marciojcarvalho/)


