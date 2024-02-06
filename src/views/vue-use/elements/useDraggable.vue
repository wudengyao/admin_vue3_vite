<template>
	<div style="position: relative">
		<div ref="el" :style="style" style="position: fixed;padding: 20px;width: 100px;height: 100px;background: #304156;line-height: 22px;color: white">
			拖动我
			<p>x：{{x}}</p>
			<p>y：{{y}}</p>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import { useDraggable } from "@vueuse/core";
const el = ref(null);
const { x, y, style } = useDraggable(el, {
	initialValue: { x: 500, y: 200 }
});
</script>

<script>
export default {
	name: "use-draggable"
};
</script>