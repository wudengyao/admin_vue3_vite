import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
// import path from 'path-browserify'
import path from 'path'

import { viteMockServe } from 'vite-plugin-mock'
import getGitInfo from './src/plugins/getGitInfo.js';


// svg-icon插件
import { createSvgIconsPlugin } from 'vite-plugin-svg-icons'
export default defineConfig({
    plugins: [
        vue(),
        createSvgIconsPlugin({
            // 指定要缓存的图标文件夹
            iconDirs: [path.resolve('./src/icons/svg')],
            // 执行icon name的格式
            symbolId: 'icon-[name]',
        }),
        viteMockServe({
            supportTs:false,
            logger: true,
            enable:false,
            mockPath: "./src/mock/",

        }),
        getGitInfo()

    ],
    base: "./", //打包路径
    resolve: {
        alias: {
            '@':  path.resolve('./src')
        },
        extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue']
    },
    server: {
        host: '0.0.0.0',
        port: 9999, // 服务端口号
        open: true, // 服务启动时是否自动打开浏览器
        cors: true, // 允许跨域
        proxy: {
            "/api": {
                target: 'http://127.0.0.1:9999/',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, ""),
            },
        },

    },


})
