<template>
	<!-- 支持渲染多级 menu 菜单 -->
	<el-sub-menu v-if="route.children.length > 0" :index="route.path">
		<template #title>
			<menu-item :title="route.meta.title" :icon="route.meta.icon"></menu-item>
		</template>
		<!-- 循环渲染 -->
		<sidebar-item
			v-for="item in route.children"
			:key="item.path"
			:route="item"
		></sidebar-item>
	</el-sub-menu>
	<!-- 渲染 item 项 -->
	<template v-else>
		<el-menu-item v-if="!route.hidden" :index="route.path">
			<menu-item :title="route.meta.title" :icon="route.meta.icon"></menu-item>
		</el-menu-item>
	</template>
</template>

<script setup>
import MenuItem from "./MenuItem";
import { defineProps } from "vue";
// 定义 props
defineProps({
	route: {
		type: Object,
		required: true
	}
});
</script>