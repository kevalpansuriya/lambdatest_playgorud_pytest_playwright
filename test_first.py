from playwright.sync_api import Page, expect

LAMBDATEST_PLAYGROUD_URL = "https://www.lambdatest.com/selenium-playground/"


def navigate_to_lambdatest_base_url(page):
    """
    Navigate to lambda test playground
    :param page:
    :return: None
    """
    page.goto(LAMBDATEST_PLAYGROUD_URL)
    page.wait_for_url(LAMBDATEST_PLAYGROUD_URL)


def test_verify_simple_form_demo(page: Page):
    """
    navigating to selenium-playground
        > click on the simple Form Demo
        > entering a msg
        > click on Get Checked Value button
        > verify a msg
    :param page:
    :return:
    """
    navigate_to_lambdatest_base_url(page)
    page.locator("a:has-text('Simple Form Demo')").click()
    page.wait_for_url(f"{LAMBDATEST_PLAYGROUD_URL}simple-form-demo")
    msg = "Welcome to LambdaTest."
    page.locator("input[placeholder='Please enter your Message']").fill(msg)
    page.locator("button:has-text('Get Checked Value')").click()
    expect(page.locator("[id='message']")).to_have_text(msg)


def test_verify_drag_drop_range_sliders_demo(page: Page):
    """
    navigating to selenium-playground
        > click on the drag-drop-range-sliders-demo
        > clicking on a slider
        > press ArrowRight key until slider value become 95
    :param page:
    :return:
    """
    navigate_to_lambdatest_base_url(page)
    page.locator("a:has-text('Drag & Drop Sliders')").click()
    page.wait_for_url(f"{LAMBDATEST_PLAYGROUD_URL}drag-drop-range-sliders-demo")
    slider = page.locator('input[value="15"]')
    slider.click()
    value = page.locator('input[value="15"] + output').inner_text()
    print(value)
    while value != "95":
        page.keyboard.press('ArrowRight')
        value = page.locator('input[value="15"] + output').inner_text()


def test_verify_input_form_submit(page: Page):
    """
    navigating to selenium-playground
        > click on the Input Form Submit
        > filling the form detail
        > click on submit button
        > verify success msg.
    :param page:
    :return:
    """
    navigate_to_lambdatest_base_url(page)
    page.locator("a:has-text('Input Form Submit')").click()
    page.wait_for_url(f"{LAMBDATEST_PLAYGROUD_URL}input-form-demo")
    page.locator("button:has-text('Submit')").click()
    # error_msg = 'Please fill out this field.'
    # expect(page.locator(f":has-text('{error_msg}')")).to_have_text(error_msg)
    page.locator('[id="name"]').fill("keval")
    page.locator('[id="inputEmail4"]').fill("kevalpansuriya@gmail.com")
    page.locator('[id="inputPassword4"]').fill("passwordtest")
    page.locator('[id="company"]').fill("lambda test")
    page.locator('[id="websitename"]').fill("https://www.lambdatest.com/")
    page.locator('select[name="country"]').select_option("United States")
    page.locator('[id="inputCity"]').fill("rajkot")
    page.locator('[id="inputAddress1"]').fill("om khodal chock")
    page.locator('[id="inputAddress2"]').fill("80 ft road mavdi")
    page.locator('[id="inputState"]').fill("gujarat")
    page.locator('[id="inputZip"]').fill("361160")
    page.locator("button:has-text('Submit')").click()
    sucess_msg = 'Thanks for contacting us, we will get back to you shortly.'
    expect(page.locator('p[class="success-msg hidden"]')).to_have_text(sucess_msg)
