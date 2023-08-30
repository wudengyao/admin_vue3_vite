import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
const app = createApp(App)

// 导入权限控制模块
import './permission'
import "@/styles/index.scss"

// import axios from '@/utils/axios'
// app.config.globalProperties.$axios = axios // 使用globalProperties挂载

//element
import installElementPlus from './plugins/element'
installElementPlus(app)
//directives
import installDirective from '@/directives'
installDirective(app)
// filter
import installFilter from '@/filters'
installFilter(app)

// 自定义表格工具组件
import RightToolbar from '@/components/RightToolbar'
// 分页组件
import Pagination from '@/components/Pagination'
// svg组件
import svgIcon from "@/components/SvgIcon/index.vue";
// 全局组件挂载
app.component('RightToolbar', RightToolbar)
app.component('Pagination', Pagination)
app.component('svg-icon', svgIcon)


app
    .use(store)
    .use(router)
    .mount('#app')
