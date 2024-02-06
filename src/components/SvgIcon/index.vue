<template>
	<div
		v-if="isExternal"
		:style="styleExternalIcon"
		class="svg-external-icon svg-icon"
		:class="className"
	/>
	<svg v-else class="svg-icon" :class="className" aria-hidden="true">
		<use :xlink:href="iconName" />
	</svg>
</template>

<style scoped>
.svg-icon {
  overflow: hidden;
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentcolor;
}
.svg-external-icon {
  display: inline-block;
  background-color: currentcolor;
  mask-size: cover !important;
}
</style>

<script setup>
import { isExternal as external } from "@/utils/validate";
import { defineProps, computed } from "vue";
const props = defineProps({
	// icon 图标
	icon: {
		type: String,
		required: true
	},
	// 图标类名
	className: {
		type: String,
		default: ""
	}
});

/**
 * 判断是否为外部图标
 */
const isExternal = computed(() => external(props.icon));
/**
 * 外部图标样式
 */
const styleExternalIcon = computed(() => ({
	mask: `url(${props.icon}) no-repeat 50% 50%`,
	"-webkit-mask": `url(${props.icon}) no-repeat 50% 50%`
}));
/**
 * 项目内图标
 */
const iconName = computed(() => `#icon-${props.icon}`);
</script>