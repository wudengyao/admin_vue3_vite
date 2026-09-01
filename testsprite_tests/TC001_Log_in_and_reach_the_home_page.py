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
        
        # -> Open the site's Login page by navigating to '/login' (https://admin-vue3-vite.vercel.app/login).
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the password field with '123456', enter the captcha value 'k97m' into the captcha input, then click the '登 录' (Login) button.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Fill the password field with '123456', enter the captcha value 'k97m' into the captcha input, then click the '登 录' (Login) button.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("k97m")
        
        # -> Fill the password field with '123456', enter the captcha value 'k97m' into the captcha input, then click the '登 录' (Login) button.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The user arrived on the home route after login.
        # Assert-outcome: passed
        # Assert: URL contains the '#/home' fragment indicating the home route.
        await expect(page).to_have_url(re.compile("\\#/home"), timeout=15000), "URL contains the '#/home' fragment indicating the home route."
        
        # --> The authenticated application shell is visible (header shown).
        # Assert-outcome: passed
        # Assert: The application header displays 'Vue3后台系统', indicating the authenticated shell is rendered.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[1]/div[1]/span").nth(0)).to_contain_text("Vue3\u540e\u53f0\u7cfb\u7edf", timeout=15000), "The application header displays 'Vue3\u540e\u53f0\u7cfb\u7edf', indicating the authenticated shell is rendered."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    