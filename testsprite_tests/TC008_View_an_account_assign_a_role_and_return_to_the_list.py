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
        
        # -> Open the site's Login page (the login screen) so the username, password, and captcha fields appear.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the captcha input with the shown text '1nk6' and click the '登 录' (Login) button to submit the form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("1nk6")
        
        # -> Fill the captcha input with the shown text '1nk6' and click the '登 录' (Login) button to submit the form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' (Permission Management) menu item in the left sidebar to reveal its submenu.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '账号列表' (Account List) menu item in the left sidebar to open the account list page.
        # 账号列表
        elem = page.get_by_text('账号列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'admin' account name in the table to open the account detail view.
        # admin
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[2]')
        await elem.click(timeout=10000)
        
        # -> Click the 'admin' account row in the account list to open its detail view.
        # admin
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[2]')
        await elem.click(timeout=10000)
        
        # -> Click the '1' ID cell for the 'admin' account in the table to open the account detail view.
        # 1
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td')
        await elem.click(timeout=10000)
        
        # -> Click the admin account's avatar image to open the account detail view.
        # Click the admin account's avatar image to open the account detail view.
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[4]/div/div/img')
        await elem.click(timeout=10000)
        
        # -> Scroll the account list table down to reveal any hidden '编辑' or '详情' action buttons, then list all buttons/links inside table rows.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'admin' table row to open the account detail view.
        # 1 admin 主管 正常 2023-03-27 13:58:15 查看 角色 删除
        elem = page.get_by_text('1 admin 主管 正常 2023-03-27 13:58:15 查看 角色 删除', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The admin account row displays a role in the role column on the account list.
        await page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[3]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The role cell for the first (admin) row is visible.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[3]").nth(0)).to_be_visible(timeout=15000), "The role cell for the first (admin) row is visible."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    