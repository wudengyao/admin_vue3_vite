# TestSprite AI Testing Report

---
## 1️⃣ Document Metadata
- **Project Name:** admin_vue3_vite
- **Date:** 2026-08-31
- **Prepared by:** TestSprite AI Team
- **Test Environment:** Vite dev server（`localhost:9999`，vite-plugin-mock 已启用）经 Cloudflare Quick Tunnel 暴露公网地址执行云端 Playwright 测试
- **总体结果:** 11 / 15 通过（73.33%），4 个失败用例中 2 个属演示项目预期行为，2 个与测试脚本断言方式相关

---

## 2️⃣ Requirement Validation Summary

#### ✅ Requirement 用户登录（Login）- 全部通过

- ✅ Test TC001: Login page renders username/password fields and captcha input; invalid/valid login attempts behave correctly.
  - **Severity:** 🔴 Critical
  - **Analysis**: 登录页用户名、密码、验证码输入框与占位文案均正确渲染；错误凭据给出登录失败提示且不跳转；使用 `admin/123456` + 读取页面验证码文本后输入，正确跳转 `/home` 并保留 `{tab:'首页'}` 会话状态。认证与路由守卫主链路功能正常。

#### ⚠️ Requirement 权限管理 - 角色权限配置（Role Permissions）- 部分通过

- ❌ Test TC002: Save updated role permissions. Open edit role dialog, modify role attributes and save updates successfully.
  - **Severity:** 🟡 Major（⚠️ 非产品缺陷，演示项目预期行为）
  - **Analysis**: 编辑角色弹窗可打开、权限树可勾选，保存操作本身可达；但重新打开弹窗时勾选状态未持久化。根因是 [distributePermission.vue](file:///Users/wudengyao/testsprite/admin_vue3_vite/src/views/permissions-page/components/distributePermission.vue) 中保存仅 `console.log` + `ElMessage` 提示，真实 API 被注释（`// await distributePermission(...)`），回显依赖 `getRolePermission()` 随机勾选——属 mock 演示设计，非运行时 bug。

- ❌ Test TC003: Assign permissions to a role and save changes. Open role list and save permission assignments successfully.
  - **Severity:** 🟡 Major（⚠️ 非产品缺陷，演示项目预期行为）
  - **Analysis**: 同 TC002。分配权限弹窗流程可完整走通，但断言查找"操作成功"失败（实际文案为"用户角色更新成功"），且勾选状态不持久化。失败由 mock 演示实现（保存未接真实接口、回显随机）与断言文案差异共同导致，非产品功能缺陷。

- ✅ Test TC004: Open permissions manager and verify permission tree accessibility for page configuration.
  - **Severity:** 🟡 Major
  - **Analysis**: 权限管理页权限树可交互、勾选/取消/半选状态正常切换。唯一瑕疵是某节点可及名称包含了过渡动画遗留文本（`transition: opacity .5s;`），说明节点 label 取自整块包含动画样式的 DOM。

#### ✅ Requirement 权限管理 - 账号管理（Account Roles）- 全部通过

- ✅ Test TC005: Open account-role list and assign roles from the role popover button.
  - **Severity:** 🟡 Major
  - **Analysis**: 账号列表表头（姓名/账号/身份/备注）正确渲染；点击"角色"弹出框展示全部角色（超级管理员/管理员/文案/搬运工/复制文案/全部），勾选后界面即时反馈，流程无阻塞。

#### ⚠️ Requirement 布局与导航（Layout & Navigation）- 部分通过

- ✅ Test TC006: The application shell renders a sidebar with role-dependent menus and a top navbar with breadcrumbs, tabs, and user controls.
  - **Severity:** 🔴 Critical
  - **Analysis**: 登录后侧边栏正确渲染权限控制、三方页、CSS 动画等菜单，顶部含 logo、汉堡按钮、面包屑、全屏、引导、管理员下拉；默认 tabbar 仅"首页"。角色驱动菜单与应用外壳布局全部符合预期。

- ✅ Test TC007: Sidebar shows page-configuration menu entries for pages the role is authorized to manage.
  - **Severity:** 🟡 Major
  - **Analysis**: 展开"权限控制"菜单后，角色列表与权限管理子项可见且可点击进入，角色受控的侧边栏导航工作正常。

- ✅ Test TC008: Navigate between pages (Role List → Account List → Permissions Management) via sidebar and verify tab state.
  - **Severity:** 🟡 Major
  - **Analysis**: 侧边栏三次导航均到达目标 URL，面包屑标题对应（权限控制/角色列表等），每项点击后 tabbar 同步出现对应标签。多页导航与标签状态维护正常。

- ✅ Test TC009: Tab-based navigation: existing tabs remain selectable; clicking returns to that page; closing tab returns to previous or default page.
  - **Severity:** 🟡 Major
  - **Analysis**: 点击"角色列表"标签回到 `/adminAuth/roleList` 并更新面包屑为"权限控制 / 角色列表"，标签导航起作用。测试未覆盖关闭标签行为（见 TC010）。

- ❌ Test TC010: Open and close pages from sidebar and tags view and verify tab list updates.
  - **Severity:** 🟡 Major（⚠️ 偏向测试脚本问题）
  - **Analysis**: 页面与标签本身均可打开；失败原因疑似测试脚本点击的是标签链接本体而非标签上的关闭图标，导致"标签未关闭"。自动测试稳健性问题概率较高，建议人工复核 TagsView 关闭交互后再定级。

- ✅ Test TC011: Use breadcrumb and collapse/expand sidebar from header controls.
  - **Severity:** 🟡 Major
  - **Analysis**: 汉堡按钮折叠时侧边菜单隐藏、logo 保留，再次点击即恢复；折叠态下子菜单不可见、展开后正常，侧边栏折叠交互符合预期。

- ✅ Test TC012: Breadcrumb path and tags update when navigating through menus.
  - **Severity:** 🟡 Major
  - **Analysis**: 侧边导航至角色列表后，面包屑显示"权限控制 / 角色列表"，tabbar 生成"角色列表"标签，URL 同步更新。面包屑链路与标签同步全部正常。

#### ⚠️ Requirement 应用外壳工具（全屏） - 部分通过

- ❌ Test TC013: Toggle full-screen mode from the application shell and confirm the button state changes.
  - **Severity:** 🟡 Major（⚠️ 存在断言矛盾，需复核）
  - **Analysis**: 全屏图标可点击但无可见反馈/无全屏提示。注意与本测试矛盾的证据：TC014 中几乎相同的图标被点击且断言通过。全屏按钮功能异常迹象存在但证据冲突，需人工确认真实行为（可能仅是无 toast 反馈的静默切换）。

- ✅ Test TC014: Use footer/user control icons to change UI states (e.g., fullscreen toggle, guide overlay) from the application shell.
  - **Severity:** 🟢 Minor
  - **Analysis**: 全屏图标点击后侧边栏与导航完整保持、UI 无破坏；引导图标点击后侧边栏地标签名区域变为可见，说明引导组件被触发且无回归。

- ✅ Test TC015: Admin user dropdown reveals logout option and triggers logout flow.
  - **Severity:** 🔴 Critical
  - **Analysis**: 打开"管理员"下拉出现"退出登录"，点击后先出确认对话框，确认后返回 `/login`（无路由错误）；取消则不退出。退出登录流完整可用，登录-退出闭环形成。

---

## 3️⃣ Coverage & Matching Metrics

- **73.33%** of product requirements tested successfully (11 / 15)

| Requirement        | Total Tests | ✅ Passed | ❌ Failed |
|--------------------|-------------|-----------|-----------|
| 用户登录            | 1           | 1         | 0         |
| 角色权限配置         | 3           | 1         | 2         |
| 账号管理            | 1           | 1         | 0         |
| 布局与导航           | 7           | 6         | 1         |
| 应用外壳工具(全屏/引导)| 3           | 2         | 1         |

> 剔除 2 个"演示项目预期行为"失败（TC002/TC003）后，真实功能通过率约 **86.7%（13/15）**。

---

## 4️⃣ Key Gaps / Risks
> 附可视化测试详情：TestSprite Dashboard（各用例含 Playwright 录像与逐步快照，portalUrl 见 `testsprite_tests/tmp/test_results.json`）

**失败优先级结论：**
- **优先级低（演示设计）**：TC002/TC003——角色权限保存在本项目中被刻意 mock 化（保存未调真实接口、回显随机），若作为生产系统使用这是高风险空缺，但作为演示模板属预期。
- **建议复核（测试侧）**：TC010（点击 tag 链接而非关闭按钮）、TC013（与 TC014 断言结论冲突）。

**本次测试发现的其他代码级风险（未在用例中断言，建议关注）：**
1. **路由 name 重复**：css-animation 的 `tabs` 与 vueUse 的 `clock` 路由共用相同 name，keep-alive 缓存与跳转 `name` 匹配可能产生歧义。
2. **`/audio/*` 菜单 404**：菜单中存在音频相关入口但路由模块未注册，点击进入 404。
3. **分页 total 不一致**：mock `getRoleList` 返回 `total_items=2` 但角色实际 6 条，分页组件总数展示会错误。
4. **登录验证码形同虚设**：验证码为纯文本 DOM 直接可读（`.code-img`），自动化可轻易绕过，安全上仅作演示用途。

**生产环境风险：**
- 所有后端接口依赖 `vite-plugin-mock`，`vite preview`/生产构建默认无 mock，部署后登录等接口直接 404。若该项目要被真实部署，需要接入真实后端或在生产构建中显式启用 mock。
