# Copilot Instructions for Personal Backend API

## Overview
This project is a personal backend API built using Python. It serves as a foundation for various applications and is designed to be modular and extensible.

## Architecture
- **Main Components**: The core functionality is encapsulated in the `app` directory, with `main.py` serving as the entry point.
- **Service Boundaries**: Each service or module should be clearly defined, with well-documented interfaces for communication.
- **Data Flow**: Understand how data is passed between components, especially in the context of API requests and responses.

## Developer Workflows
- **Running the Application**: Use the command `uvicorn app.main:app --reload` to start the server in development mode.
- **Testing**: Ensure to run tests regularly. Use `pytest` for running tests, and check the `tests` directory for test cases.
- **Debugging**: Utilize logging effectively. Check the logs for any errors or warnings that can guide debugging efforts.

## Project Conventions
- **Code Structure**: Follow the structure laid out in the `app` directory. Each module should have its own directory if it contains multiple files.
- **Naming Conventions**: Use snake_case for variable and function names, and PascalCase for class names.

## Integration Points
- **External Dependencies**: Check `requirements.txt` for all external libraries. Ensure to install them in your virtual environment using `pip install -r requirements.txt`.
- **Cross-Component Communication**: Use RESTful principles for API communication. Ensure that endpoints are well-defined and documented.

## Examples
- **Creating a New Endpoint**: When adding a new endpoint, ensure to document its purpose, expected inputs, and outputs in the code comments.
- **Handling Errors**: Implement error handling consistently across the application. Use custom exceptions where necessary to provide clear feedback to API consumers.

## Conclusion
These instructions should help AI agents understand the structure and workflows of the Personal Backend API project. For any unclear sections, please provide feedback for further refinement.