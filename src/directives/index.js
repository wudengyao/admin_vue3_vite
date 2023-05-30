import permission from './permission'

export default app => {
  app.directive('auth', permission)

}
