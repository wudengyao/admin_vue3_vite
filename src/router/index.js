import {
	createRouter,
	createWebHashHistory
} from "vue-router";
import store from "@/store";

import layout from "@/layout";
import permissions from "./modules/permissions";
import third from "./modules/third";
import cssAnimation from "./modules/cssAnimation";
import vueUse from "./modules/vueUse";

/**
 * 私有路由表
 */
export const privateRoutes = [
	permissions,
	third,
	cssAnimation,
	vueUse
];
/**
 * 公开路由表
 */
export const publicRoutes = [
	{
		path: "/login",
		component: () => import("@/views/login/index")
	},
	{
		path: "/",
		// 注意：带有路径“/”的记录中的组件“默认”是一个不返回 Promise 的函数
		component: layout,
		redirect: "/home",
		children: [
			{
				path: "/home",
				name: "home",
				component: () => import("@/views/home/index"),
				meta: { title: "首页", icon: "home", affix: true }, // affix=true,tagViews右侧没有关闭按钮
				hidden: true// true不显示在侧边栏
			},
			{
				path: "/404",
				name: "404",
				component: () => import("@/views/error-page/404")
			},
			{
				path: "/401",
				name: "401",
				component: () => import("@/views/error-page/401")
			}
		]
	}
	// 测试页面
	// {
	//     path: '/test',
	//     component: () => import('@/views/test-page/test'),
	//
	// },
];

/**
 * 初始化路由表
 */
export function resetRouter() {
	if (store.getters.hasRoles) {
		const menus = store.getters.roles;
		// removeRoute是根据路由的name去删除路由的，所以我们要对路由的名字进行截取
		// const menus = ['getRoleList','admintorList','adminAuth']
		// console.log("menus==",menus)
		// console.log("router==",router.getRoutes())
		menus.forEach(menu => {
			const url = menu.url;
			const i = url.lastIndexOf("/");
			const name = url.substring(i + 1, url.length);
			router.removeRoute(name);
		});
	}
}

const router = createRouter({
	history: createWebHashHistory(),
	// routes: [...publicRoutes, ...privateRoutes]
	routes: publicRoutes

});

export default router;