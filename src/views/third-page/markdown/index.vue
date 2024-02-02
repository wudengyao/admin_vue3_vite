<template>
	<div class="container">
		<Markdown
			:detail="detail"
			@onSuccess="onSuccess"
		></Markdown>
	</div>
</template>

<style lang="scss" scoped>
.container {
  background: white;
}
</style>

<script setup>
import Markdown from "../components/Markdown.vue";
import { ref } from "vue";
const detail = ref({});

detail.value = "markdown编辑器测试输入";
// 创建成功
const onSuccess = () => {
	console.log("onSuccess");
};

</script>