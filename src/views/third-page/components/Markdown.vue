<template>
	<div class="markdown-container">
		<!-- 渲染区 -->
		<div id="markdown-box"></div>
		<div class="bottom">
			<el-button type="primary" @click="onSubmitClick">提交</el-button>
		</div>
	</div>
</template>

<style lang="scss" scoped>
.markdown-container {
  .bottom {
    margin-top: 20px;
    text-align: right;
  }
}
</style>

<script setup>
import MkEditor from "@toast-ui/editor";
import "@toast-ui/editor/dist/toastui-editor.css";
import { onMounted, defineProps, defineEmits, watch } from "vue";
import { useStore } from "vuex";
const props = defineProps({
	detail: {
		type: String,
		default: ""
	}
});

const emits = defineEmits(["onSuccess"]);

// 初始化editor
// Editor实例
let mkEditor;
// 处理离开页面切换语言导致 dom 无法被获取
let el;
onMounted(() => {
	el = document.querySelector("#markdown-box");
	initEditor();
	mkEditor.setHTML(props.detail);
});

const store = useStore();
const initEditor = () => {
	mkEditor = new MkEditor({
		el,
		height: "500px",
		previewStyle: "vertical",
		language: store.getters.language === "zh" ? "zh-CN" : "en"
	});

	mkEditor.getMarkdown();
};

// 编辑相关
watch(
	() => props.detail,
	val => {
		if (val) {
			mkEditor.setHTML(val);
		}
	},
	{
		immediate: false
	}
);

// 处理提交
const onSubmitClick = async() => {
	console.log(mkEditor.getHTML());

	if (props.detail && props.detail._id) {
		// // 编辑文章
		// await editArticle({
		//   id: props.detail._id,
		//   title: props.title,
		//   content: mkEditor.getHTML()
		// })
	} else {
		// 创建文章
		// await commitArticle({
		//   title: props.title,
		//   content: mkEditor.getHTML()
		// })
	}

	mkEditor.reset();
	emits("onSuccess");
};
</script>