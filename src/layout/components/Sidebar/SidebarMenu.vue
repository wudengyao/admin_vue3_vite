<template>
	<!-- 一级 menu 菜单 -->
	<el-menu
		:default-active="activeMenu"
		:collapse="!$store.getters.sidebarOpened"
		:background-color="$store.getters.cssVar.menuBg"
		:text-color="$store.getters.cssVar.menuText"
		:active-text-color="$store.getters.cssVar.menuActiveText"
		:unique-opened="true"
		router
	>
		<sidebar-item
			v-for="item in routes"
			:key="item.path"
			:route="item"
		></sidebar-item>
	</el-menu>
</template>

<style lang="scss" scoped></style>

<script setup>
import { computed } from "vue";
import SidebarItem from "./SidebarItem";
import { useRouter, useRoute } from "vue-router";
import { filterRouters, generateMenus } from "@/utils/route";

// 计算路由表结构
const router = useRouter();
const routes = computed(() => {
	const filterRoutes = filterRouters(router.getRoutes());
	return generateMenus(filterRoutes);
});

// 计算高亮 menu 的方法
const route = useRoute();
const activeMenu = computed(() => {
	const { meta, path } = route;
	if (meta.activeMenu) {
	  return meta.activeMenu;
	}
	return path;
});
</script>