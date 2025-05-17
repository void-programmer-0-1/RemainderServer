# Reminder App

A powerful and efficient To-Do and Event Reminder application built with **FastAPI** and **Python**. This app allows you to effortlessly manage your tasks and events with an intuitive API, providing seamless integration and reminders.

## Features

* 📅 **Event Reminders** — Never miss an important event again.
* ✅ **To-Do Management** — Keep track of your tasks efficiently.
* 🔄 **Recurring Reminders** — Set reminders to repeat daily, weekly, or monthly.
* 🔔 **Notifications Support** — Get notified ahead of time.
* 🔍 **Search and Filter** — Quickly find tasks and events.
* 🗄️ **Data Persistence** — Stores all reminders securely.

## Tech Stack

* **Backend:** FastAPI, Python
* **Database:** SQLite / MySQL (configurable)
* **Auth:** JWT-based authentication
* **Task Scheduling:** Celery (Optional)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/reminder-app.git
   cd reminder-app
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the app:**
   Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the Swagger UI.

## API Endpoints

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| GET    | `/todos`       | Fetch all To-Dos   |
| POST   | `/todos`       | Create a new To-Do |
| GET    | `/events`      | Fetch all Events   |
| POST   | `/events`      | Create a new Event |
| PUT    | `/todos/{id}`  | Update a To-Do     |
| DELETE | `/todos/{id}`  | Delete a To-Do     |
| PUT    | `/events/{id}` | Update an Event    |
| DELETE | `/events/{id}` | Delete an Event    |

## Folder Structure

```
reminder-app/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── utils.py
├── venv/
├── requirements.txt
└── README.md
```

## Contributing

Feel free to submit issues or pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

* **Email:** [your.email@example.com](mailto:your.email@example.com)
* **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourusername)

Happy Coding! 🚀
