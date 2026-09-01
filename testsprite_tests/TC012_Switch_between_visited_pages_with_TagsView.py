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
        
        # -> Open the 'Login' page by navigating to the /login path.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the password field with '123456', enter the captcha text '0ule' into the captcha input, then click the '登 录' button to submit the login form.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Fill the password field with '123456', enter the captcha text '0ule' into the captcha input, then click the '登 录' button to submit the login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("0ule")
        
        # -> Fill the password field with '123456', enter the captcha text '0ule' into the captcha input, then click the '登 录' button to submit the login form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the '权限管理' page from the sidebar, then open the '三方库' page from the sidebar, then click the '首页' tag in the tags area to switch back to that previously visited page.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the '权限管理' page from the sidebar, then open the '三方库' page from the sidebar, then click the '首页' tag in the tags area to switch back to that previously visited page.
        # 三方库
        elem = page.get_by_text('三方库', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the '权限管理' page from the sidebar, then open the '三方库' page from the sidebar, then click the '首页' tag in the tags area to switch back to that previously visited page.
        # 首页
        elem = page.locator('xpath=/html/body/div/div/div[2]/div/div/div[2]/span/span/span')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The Home page is active and shows the breadcrumb '首页'.
        # Assert-outcome: passed
        # Assert: The breadcrumb displays '首页', indicating the Home page is active.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/span/span[1]/span").nth(0)).to_have_text("\u9996\u9875", timeout=15000), "The breadcrumb displays '\u9996\u9875', indicating the Home page is active."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    