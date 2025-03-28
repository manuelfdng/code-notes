### 🔍 Code Quality & Maintainability
| Purpose | Prompt |
|---------|--------|
| **Code Review** | Please provide a comprehensive code review of the code above. Focus on readability, maintainability, performance, and adherence to best practices. Highlight potential bugs, suggest improvements, and provide examples where necessary. |
| **Code Design Pattern Refactor Suggestions** | Analyze this code and suggest appropriate design patterns for refactoring. Explain why each pattern is suitable, how it improves the code, and any potential trade-offs or downsides of applying it. |
| **Break Down Complex Logic into Smaller Functions** | Improve code clarity by breaking down complex logic into smaller, well-defined helper functions. Make sure the output you give is a working version and not just an illustrative example. |
| **Force Code Outputs to be Functional** | I need a complete and functional code implementation, not just a conceptual or illustrative example. The code should be executable and include all necessary components to work as intended. |
| **Refactor for DRY Principles** | Review the codebase and identify areas where the "Don't Repeat Yourself" (DRY) principle is violated. Refactor to reduce duplication. |
| **Suggest Consistent Naming Conventions** | Review variable, function, and class names. Recommend naming conventions that enhance readability and consistency. |
| **Improve Inline Documentation** | Review the code for comments and docstrings. Suggest improvements or generate them if missing. |
| **Modularization Recommendations** | Recommend how to break this monolithic codebase into more modular, reusable components or services. |

---

### 🚀 Performance & Scalability
| Purpose | Prompt |
|---------|--------|
| **Performance Bottleneck Analysis** | Analyze the code for potential performance bottlenecks. Recommend optimizations and provide before-and-after examples when possible. |
| **Memory and Resource Optimization** | Are there opportunities in this codebase to reduce memory usage or improve resource management? Suggest concrete changes. |
| **Scalability Assessment** | Is this codebase scalable? If not, suggest architectural or structural changes that would support scale. |
| **Evaluate Caching Opportunities** | Are there parts of this codebase where caching could significantly improve performance? Suggest caching strategies or libraries. |

---

### 🧪 Testing & Validation
| Purpose | Prompt |
|---------|--------|
| **Testability Review** | Assess how easy this code is to test. Suggest improvements to increase testability, such as dependency injection or modularization. |
| **Generate Unit Tests** | Generate a complete suite of unit tests for the code, using appropriate frameworks and mocking libraries. Include assertions and edge cases. |
| **Edge Case Identification** | Identify possible edge cases that this codebase may not currently handle. Recommend improvements. |

---

### 🔐 Security & Risk
| Purpose | Prompt |
|---------|--------|
| **Security Vulnerability Review** | Analyze this code for potential security risks or vulnerabilities. Suggest mitigations or safer coding practices. |
| **Injection & Input Validation Check** | Review the code for input validation, sanitization, and protections against injection attacks (SQL, command, etc.). Recommend best practices. |

---

### 🧱 Architecture & Dependencies
| Purpose | Prompt |
|---------|--------|
| **Dependency Health Check** | Review the codebase’s dependencies for outdated, insecure, or bloated packages. Suggest actions for improving dependency hygiene. |
| **Reduce Technical Debt** | How can I reduce technical debt for this codebase? Provide specific, actionable recommendations, such as refactoring strategies, testing improvements, dependency management, documentation enhancements, and architectural adjustments. |
| **Production Readiness Check** | Is this codebase production-ready? Evaluate the code for stability, scalability, performance, security, and completeness. Suggest any changes required to meet production standards. |

---

### 📄 Documentation & Developer Experience
| Purpose | Prompt |
|---------|--------|
| **README.md generation** | Generate a README.md file for this code that includes an overview of the application, describing its purpose and functionality, along with a description of the key files and their roles within the project. Do not include contributing guidelines or license information. |
| **Generate CONTRIBUTING.md** | Generate a CONTRIBUTING.md file with guidelines on how to contribute to this codebase (branch naming, PR process, code style, etc.). |
| **Environment Setup Instructions** | Create a step-by-step guide for setting up the development environment from scratch. |

---

### 🧠 System Prompt: Flask Best Practices to Follow

When working with Flask, follow these foundational best practices to ensure scalability, maintainability, and clean architecture from the beginning:

- **Use Flask-Celery** immediately instead of relying on threads for background tasks. This ensures proper task management, reliability, and async scalability.
- **Separate CSS and JS** into static files right away. Avoid inline styles or scripts to maintain cleaner templates and enable better caching and reuse.
- **Adopt Flask-SQLAlchemy and Flask-Migrate** from the start for database modeling and migrations. This ensures consistent schema management and easier collaboration.
- **Keep the project modular** using Flask blueprints. Group blueprints into separate folders by domain to improve code organization and scalability.
- **Use centralized error handling** via a structured system of:
  - Predefined **custom exception classes** (e.g., `AppError`, `NotFoundError`, `ValidationError`, etc.) located in a shared `exceptions.py` module.
  - Global **Flask error handlers** registered using `@app.errorhandler()` decorators, which return standardized JSON responses with appropriate HTTP status codes.
  - All unhandled exceptions must return a 500 Internal Server Error with a generic message, while being fully logged (stack trace included) using the **Python `logging` module**, configured app-wide in `logging_config.py`.
  - No inline `try/except` unless absolutely necessary for localized flow control — error handling must propagate to the centralized system.
  - Every error response must follow a consistent schema: `{ "error": "Message", "code": 400 }`.

These practices should be assumed as defaults when building or reviewing any Flask-based application.

