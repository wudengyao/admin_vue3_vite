<template>
	<div class="container">
		<editor
			:detail="detail"
			@onSuccess="onSuccess"
		></editor>
	</div>
</template>
<script setup>
import Editor from "../components/Editor.vue";
import { ref } from "vue";
const detail = ref({});

detail.value = "富文本编辑器测试输入";
// 创建成功
const onSuccess = () => {
	console.log("onSuccess");
};

</script>