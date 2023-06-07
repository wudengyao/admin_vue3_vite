import permission from './permission'

export default app => {
  app.directive('auth', permission)

  // 使 v-focus 在所有组件中都可用
  app.directive('focus', {
    mounted: (el) => el.focus()
  })

}
