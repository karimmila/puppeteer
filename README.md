# Patient Registration Application

This is a FastAPI-based patient registration application that allows users to register by providing their name, email, phone number, and a photo of a document. The application validates the data, stores it in a Postgres database, and sends a confirmation email asynchronously.

## Features

- **Patient Registration:** Register with name, email, phone, and document photo.
- **Data Validation:** Uses Pydantic for validating user input.
- **Database Integration:** Stores patient data in a Postgres database using SQLAlchemy.
- **Asynchronous Email:** Sends confirmation emails in the background using FastAPI’s BackgroundTasks.
- **Dockerized Environment:** Fully containerized using Docker and Docker Compose.
- **Future-Ready:** Designed with future SMS notification integration in mind.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed.

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Add .env with the variables**

   ```
   DATABASE_URL=postgresql://postgres:password@db:5432/postgres
   MAIL_SERVER=sandbox.smtp.mailtrap.io
   MAIL_PORT=2525
   MAIL_USERNAME=<your_mailtrap_username>
   MAIL_PASSWORD=<your_mailtrap_password>
   MAIL_FROM=<your_email@example.com>
   ENABLE_SMS=True
   ```

3. **Build and Run the application with docker**

   ```
   docker compose up --build
   ```

4. **Access the FastAPI Documentation**
   ```
   http://localhost:8000/docs
   ```
