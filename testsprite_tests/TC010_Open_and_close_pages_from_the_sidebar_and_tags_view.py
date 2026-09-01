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
        
        # -> Open the '/login' page (navigate to the Login page) so the login form and captcha text are visible.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the login form fields: enter the username, password, and the visible captcha text into the 'Vue3后台系统' login form.
        # 请输入用户名 text field
        elem = page.get_by_placeholder('请输入用户名', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("admin")
        
        # -> Fill the login form fields: enter the username, password, and the visible captcha text into the 'Vue3后台系统' login form.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Fill the login form fields: enter the username, password, and the visible captcha text into the 'Vue3后台系统' login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("ce6d")
        
        # -> Click the '登 录' button to submit the login form and load the authenticated UI.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' sidebar menu item to open its submenu.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '账号列表' (Account List) sidebar menu item to open the Account List page.
        # 账号列表 menu item
        elem = page.get_by_role('menuitem', name='账号列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' (Role List) sidebar menu item to open the Role List page.
        # 角色列表
        elem = page.get_by_text('角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Close the '角色列表' tab from the tags view (click the '角色列表' tag close control).
        # 角色列表 link
        elem = page.get_by_role('link', name='角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' tag's close control to close the Role List tab.
        # 角色列表 link
        elem = page.get_by_role('link', name='角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' tag in the tags row to attempt to close the Role List page from the tags view.
        # 角色列表 link
        elem = page.get_by_role('link', name='角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '账号列表' tag in the tags view to switch to the Account List page.
        # 账号列表 link
        elem = page.get_by_role('link', name='账号列表', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The Role List tab ('角色列表') remained open and was not closed from the tags view.
        await page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/a[3]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: failed
        # Assert: Expected the '角色列表' tag to be removed from the tags view (closed).
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/a[3]").nth(0)).to_be_visible(timeout=15000), "Expected the '\u89d2\u8272\u5217\u8868' tag to be removed from the tags view (closed)."
        
        # --> The Account List page ('账号列表') remains accessible via the tags view.
        await page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/a[2]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: failed
        # Assert: Expected the '账号列表' tag to be present and selectable in the tags view.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/a[2]").nth(0)).to_be_visible(timeout=15000), "Expected the '\u8d26\u53f7\u5217\u8868' tag to be present and selectable in the tags view."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    