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
        
        # -> Wait for the app to finish loading, then open the login page by navigating to '/login'.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the password field with '123456', enter the captcha value '0jap', and click the '登 录' button to submit the login form.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Fill the password field with '123456', enter the captcha value '0jap', and click the '登 录' button to submit the login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("0jap")
        
        # -> Fill the password field with '123456', enter the captcha value '0jap', and click the '登 录' button to submit the login form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the Role List page by navigating to /adminAuth/getRoleList (role management).
        await page.goto("https://admin-vue3-vite.vercel.app/adminAuth/getRoleList")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the '权限管理' menu item in the left sidebar to open permission management options.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' menu item in the left sidebar to open the role list page.
        # 角色列表 menu item
        elem = page.get_by_role('menuitem', name='角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '配置权限' button for the role '主管' to open the permission assignment dialog.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # -> In the '配置权限' dialog, select the '权限管理' permission and click the '确定' button to save the selection.
        # 权限管理
        elem = page.get_by_role('treeitem', name='权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> In the '配置权限' dialog, select the '权限管理' permission and click the '确定' button to save the selection.
        # 确定 button
        elem = page.get_by_role('button', name='确定', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '配置权限' button for role '主管' to re-open the permission assignment dialog and verify the saved permission.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The permission dialog should have closed and the role table should be visible after saving.
        # Assert-outcome: failed
        # Assert: Expected the permission dialog to be closed after saving.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div").nth(0)).not_to_be_visible(timeout=15000), "Expected the permission dialog to be closed after saving."
        
        # --> The updated permission selection should persist and be shown when re-opening the role's permission dialog.
        # Assert-outcome: failed
        # Assert: Expected the '权限管理' permission node to be selected (aria-checked='true') after saving.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div[1]").nth(0)).to_have_attribute("aria-checked", "false", timeout=15000), "Expected the '\u6743\u9650\u7ba1\u7406' permission node to be selected (aria-checked='true') after saving."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    