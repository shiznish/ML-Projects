# .NET Core C# Coding Standards

## ✅ Naming Conventions
- Use `PascalCase` for classes, methods, and properties.
- Use `camelCase` for local variables and method parameters.
- Prefix interfaces with `I` (e.g., `IRepository`).
- Async methods should end with `Async`.

## 🔍 Code Structure
- Keep each class in its own file.
- Group related classes into appropriate namespaces.
- Use regions to logically group code only when helpful.

## 💡 Best Practices
- Always use `var` when the type is obvious.
- Avoid using `dynamic`, unless absolutely required.
- Use null-coalescing (`??`) and null-conditional (`?.`) operators to simplify null checks.
- Use `string interpolation` (`$"{name}"`) instead of `string.Format`.

## ⚙️ Exception Handling
- Catch specific exceptions, not general `Exception`.
- Use `try-catch` only where needed.
- Always log exceptions with context.

## 📦 Dependency Injection
- Use constructor injection for services and configurations.
- Avoid service locator pattern.
- Register interfaces and their implementations using scoped/lifetime appropriately.

## 🧪 Unit Testing
- Test method names should follow `MethodName_ExpectedBehavior_Scenario`.
- Use mocking frameworks like Moq.
- Avoid testing private methods directly.

## 🚀 Performance & Security
- Use `async/await` for I/O-bound operations.
- Validate all external inputs.
- Avoid exposing sensitive data in logs or errors.

## ✅ Code Style
- Use consistent indentation (4 spaces).
- Use braces `{}` for all `if`, `else`, `while`, and `for` blocks.
- Keep methods short and focused.

## 🧹 Clean Code
- Remove unused code and `using` directives.
- Follow SOLID principles.
- Prefer composition over inheritance.

