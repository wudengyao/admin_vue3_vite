/** When your routing table is too long, you can split it into small modules**/

import Layout from "@/layout";
import layout from "@/layout";

export default {
	path: "/third",
	component: layout,
	redirect: "/third/editor",
	alwaysShow: true, // will always show the root menu
	name: "third",
	meta: {
		title: "三方库",
		icon: "article"
	},
	children: [
		{
			path: "/third/editor",
			component: () => import("@/views/third-page/editor/index.vue"),
			name: "editor",
			meta: {
				title: "富文本", icon: "article-ranking"
			}
		},
		{
			path: "/third/markdown",
			component: () => import("@/views/third-page/markdown/index.vue"),
			name: "markdown",
			meta: {
				title: "markdown", icon: "article-create"
			}
		}

	]
};