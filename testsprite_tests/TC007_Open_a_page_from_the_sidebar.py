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
        
        # -> Open the login page (navigate to /login) and wait for the login form to appear.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Submit the login form by clicking the '登 录' button after entering username, password, and the captcha shown on the page.
        # 请输入用户名 text field
        elem = page.get_by_placeholder('请输入用户名', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("admin")
        
        # -> Submit the login form by clicking the '登 录' button after entering username, password, and the captcha shown on the page.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Submit the login form by clicking the '登 录' button after entering username, password, and the captcha shown on the page.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("brm4")
        
        # -> Submit the login form by clicking the '登 录' button after entering username, password, and the captcha shown on the page.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' item in the left sidebar to open its admin page.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' item in the left sidebar to open the Role List admin page
        # 角色列表 menu item
        elem = page.get_by_role('menuitem', name='角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The '角色列表' admin page is open in the main content area and shows the roles table.
        await page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/table/thead/tr/th[1]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The roles table header '角色ID' is visible in the main content area.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/table/thead/tr/th[1]").nth(0)).to_be_visible(timeout=15000), "The roles table header '\u89d2\u8272ID' is visible in the main content area."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    