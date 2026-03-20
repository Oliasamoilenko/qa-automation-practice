# QA Automation Practice Project

Tools:

- Python
- Selenium
- PyTest
- Jira

Automated scenarios:

- TC-001 Successful login
- TC-002 Negative login
- TC-003 Add item to cart

Manual test cases were created in Jira and automated using Selenium.

Screenshots are captured automatically on test failures and can be attached as evidence.

## Continuous Integration

This project uses GitHub Actions to run the automated test suite on every push and pull request.

If tests fail, screenshots are uploaded as workflow artifacts.

## Additional Modern Tooling

This repository also includes a simple Playwright example to demonstrate exposure to a
modern browser automation framework.
