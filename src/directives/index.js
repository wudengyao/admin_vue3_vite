import permission from './permission'
import print from 'vue3-print-nb'

export default app => {
  app.use(print)
  app.directive('auth', permission)



}
