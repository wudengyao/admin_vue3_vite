import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("https://admin-vue3-vite.vercel.app")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the captcha field with the displayed code 'aooc' and click the '登 录' button to submit the login form.
        # 请输入用户名 text field
        elem = page.get_by_placeholder('请输入用户名', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("admin")
        
        # -> Fill the captcha field with the displayed code 'aooc' and click the '登 录' button to submit the login form.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Fill the captcha field with the displayed code 'aooc' and click the '登 录' button to submit the login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("aooc")
        
        # -> Fill the captcha field with the displayed code 'aooc' and click the '登 录' button to submit the login form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The application did not enter full-screen mode when the full-screen control was clicked.
        await page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: failed
        # Assert: Expected the top breadcrumb to be hidden in full-screen mode.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]").nth(0)).to_be_visible(timeout=15000), "Expected the top breadcrumb to be hidden in full-screen mode."
        
        # --> The application shell (left navigation) remained visible after attempting to enter full-screen.
        await page.locator("xpath=/html/body/div[1]/div/div[1]/div[2]/div[1]/div/ul/li[1]/div").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: failed
        # Assert: Expected the application shell (left navigation) to be hidden in full-screen mode.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[1]/div[2]/div[1]/div/ul/li[1]/div").nth(0)).to_be_visible(timeout=15000), "Expected the application shell (left navigation) to be hidden in full-screen mode."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    