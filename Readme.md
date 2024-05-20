# Event Sourcing & CQRS Learning Repository

Welcome to the Event Sourcing and CQRS learning repository in Python! This repository is designed to help you understand and implement the principles of Event Sourcing and Command Query Responsibility Segregation (CQRS) from scratch.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Event Sourcing is a powerful pattern for building applications with a reliable event log of all state changes. CQRS, on the other hand, separates the write and read models, allowing for optimized operations on each side. Together, they provide a robust architecture for complex applications.

This repository aims to provide a hands-on learning experience by implementing a simple event-sourced and CQRS-based system in Python.

## Usage

To run the application, execute the following command:

```
python itemMain.py
```

This will start the application and allow you to interact with the event-sourced CQRS system.

## Roadmap

To ensure a well-functioning event-sourced CQRS system, follow this roadmap:

- [ ] **Domain Model**

  - [ ] Define aggregate roots and entities.
  - [ ] Implement value objects.

- [ ] **Event Sourcing**

  - [x] Create event classes.
  - [x] Implement event store
    - [x] in-memory
    - [ ] postgres
  - [ ] Handle event replay and state reconstruction.

- [ ] **Command Handling**

  - [x] Define command classes.
  - [ ] Implement command handlers.

- [ ] **Read Model (Query Side)**

  - [x] Create read models.
  - [ ] Implement read model updaters.

- [ ] **Infrastructure**

  - [ ] Set up database connections.
  - [ ] Configure messaging/dispatching system.
  - [ ] Implement API endpoints.

- [ ] **Testing**

  - [ ] Write unit tests for domain logic.
  - [ ] Write integration tests for event sourcing.
  - [ ] Write end-to-end tests for CQRS flow.

- [ ] **Documentation**
  - [ ] Document all major components.
  - [ ] Provide examples and usage guides.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Happy learning and coding!
