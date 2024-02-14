
# Playwright python lambda test playground

This document showcases three automated use cases within the LambdaTest Playground using Playwright:

Case 1: Simple Form Interaction

    Navigate to the Selenium Playground (https://www.lambdatest.com/selenium-playground/).
    Click on the "Simple Form Demo" section.
    Enter a message into the text field.
    Click the "Get Checked Value" button.
    Verify that the displayed message matches the entered text.
    Case 2: Drag-and-Drop Slider Manipulation

Case 2: Drag-and-Drop Range Sliders Demo

    Navigate to the Selenium Playground.
    Click on the "Drag-and-Drop Range Sliders Demo" section.
    Click on any of the sliders available.
    Continuously press the "Arrow Right" key on your keyboard until the slider value reaches 95.
    Verify that the slider's numerical value displays "95".
    Case 3: Input Form Submission

Case 3: Input Form Submit Demo

    Navigate to the Selenium Playground.
    Click on the "Input Form Submit" section.
    Fill out the form fields with required details.
    Click the "Submit" button.
    Verify that a success message is displayed after submission.

    
Technical Implementation (using Python and Playwright):
## Authors

- [@kevalpansuriya](https://github.com/kevalpansuriya)


## Run Locally

Clone the project

```bash
  https://github.com/kevalpansuriya/playwright_test.git
```

Go to the project directory

```bash
  cd playwright_test 
```

Install dependencies

```bash
  pip install pytest-playwright
```

run test case

```bash
  pytest --headed

```

