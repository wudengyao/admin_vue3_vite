import router from './router'
import store from './store'

// 白名单
const whiteList = ['/login']
/**
 * 路由前置守卫
 */
router.beforeEach(async (to, from, next) => {
  // 存在 token ，进入主页
  if (store.getters.token) {//当前存在token，如果此时去登录界面，自动跳转到主页
    if (to.path === '/login') {
      next('/')
    } else {//如果此时，去除了登录页面的其他页面，就去要去的目标页面
      if (!store.getters.hasRoles) {
        const {roles} = await store.dispatch('user/getPermissionData')
        // 处理用户权限，筛选出需要添加的权限
        const accessRoutes = await store.dispatch('permission/generateRoutes', roles)

        console.log("筛选出需要addRoute的路由",accessRoutes)
        // 利用 addRoute 循环添加
        accessRoutes.forEach(item => {
          router.addRoute(item)
        })
        // router.addRoutes(accessRoutes)
          // hack method to ensure that addRoutes is complete
          // set the replace: true, so the navigation will not leave a history record
        next({...to, replace: true})

      }
      next()
    }
  } else {
    // 没有token的情况下，可以进入白名单（不需要登录的界面）
    if (whiteList.indexOf(to.path) > -1) {
      next()
    } else {//，如果是需要登录的界面，去登录界面
      next('/login')
    }
  }
})

