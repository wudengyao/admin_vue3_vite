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
        
        # -> Navigate to the '/login' page and load the login form (Login)
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill '123456' into the password field, fill '8x1i' into the captcha field, and click the '登 录' button to submit the login form.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Fill '123456' into the password field, fill '8x1i' into the captcha field, and click the '登 录' button to submit the login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("8x1i")
        
        # -> Fill '123456' into the password field, fill '8x1i' into the captcha field, and click the '登 录' button to submit the login form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' (Permission Management) menu item in the left sidebar to open its submenu.
        # 权限管理
        elem = page.locator('xpath=/html/body/div/div/div/div[2]/div/div/ul/li/div/div')
        await elem.click(timeout=10000)
        
        # -> Click the '账号列表' (Account List) link in the left sidebar to open the account list page.
        # 账号列表 menu item
        elem = page.get_by_role('menuitem', name='账号列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'admin' account row to open its details and verify account information is displayed
        # admin
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[2]')
        await elem.click(timeout=10000)
        
        # -> Click the admin user's avatar in the account list to try opening the account details view.
        # Click the admin user's avatar in the account list to try opening the account details view.
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[4]/div/div/img')
        await elem.click(timeout=10000)
        
        # -> Click the admin user's avatar in the account list to open the account details view.
        # Click the admin user's avatar in the account list to open the account details view.
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[4]/div/div/img')
        await elem.click(timeout=10000)
        
        # -> Click the admin user's avatar image in the account list to open the account details view.
        # Click the admin user's avatar image in the account list to open the account details view.
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[4]/div/div/img')
        await elem.click(timeout=10000)
        
        # -> Click the admin user's avatar image to open the account details view and verify the account information is displayed.
        # Click the admin user's avatar image to open the account details view and verify the account information is displayed.
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[4]/div/div/img')
        await elem.click(timeout=10000)
        
        # -> Click the '1' ID cell in the account list (the admin row) to open the account details view and verify account information is displayed.
        # 1
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td')
        await elem.click(timeout=10000)
        
        # -> Click the '2023-03-27 13:58:15' operation time cell in the admin row to try opening the account details view.
        # 2023-03-27 13:58:15
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[6]')
        await elem.click(timeout=10000)
        
        # -> Click the per-row '查看' button in the admin row to open the account details view and verify account information is displayed.
        # 查看 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='查看', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The account details view opened and displays the account information.
        # Assert-outcome: passed
        # Assert: The '用户ID' label is visible in the account details table.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/table/tbody/tr[1]/td[1]").nth(0)).to_have_text("\u7528\u6237ID", timeout=15000), "The '\u7528\u6237ID' label is visible in the account details table."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    