import { createApp } from 'vue'
import App from './App.vue'
import installElementPlus from './plugins/element'
import router from './router'
import store from './store'


const app = createApp(App)
// 导入权限控制模块
import './permission'

import installDirective from '@/directives'
import "@/styles/index.scss"
import axios from '@/utils/axios'
app.config.globalProperties.$axios = axios // 使用globalProperties挂载


installElementPlus(app)
installDirective(app)

// 将自动注册所有组件为全局组件


import svgIcon from "@/components/SvgIcon/index.vue";
import 'virtual:svg-icons-register'  // 新增

app
  .use(store)
  .use(router)
    .component('svg-icon', svgIcon)
    .mount('#app')
