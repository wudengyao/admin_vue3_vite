<template>
	<div class="editor-container">
		<div id="editor-box"></div>
		<div class="bottom">
			<el-button type="primary" @click="onSubmitClick">提交</el-button>
		</div>
	</div>
</template>

<style lang="scss" scoped>
.editor-container {
  .bottom {
    margin-top: 20px;
    text-align: right;
  }
}
</style>

<script setup>
import E from "wangeditor";
import { onMounted, defineProps, defineEmits, watch } from "vue";

const props = defineProps({
	// title: {
	//   required: true,
	//   type: String
	// },
	detail: {
		type: String,
		default: ""
	}
});

const emits = defineEmits(["onSuccess"]);

// Editor实例
let editor;
// 处理离开页面切换语言导致 dom 无法被获取
let el;
onMounted(() => {
	el = document.querySelector("#editor-box");
	initEditor();
	editor.txt.html(props.detail);
});

const initEditor = () => {
	editor = new E(el);
	editor.config.zIndex = 1;
	// 菜单栏提示
	editor.config.showMenuTooltips = true;
	editor.config.menuTooltipPosition = "down";
	// 一次最多上传图片的数量
	editor.config.uploadImgMaxLength = 1;
	// 设置编辑区域高度为 500px
	editor.config.height = 700;
	// 限制上传图片格式
	editor.config.uploadImgAccept = ["jpg", "jpeg", "png", "gif", "bmp"];
	editor.config.showLinkImg = false;
	// 默认情况下，显示所有菜单
	editor.config.menus = [
		"head",
		"bold",
		"fontSize",
		"fontName",
		"italic",
		"underline",
		"strikeThrough",
		"indent",
		"lineHeight",
		"foreColor",
		"backColor",
		"link",
		"list",
		"todo",
		"justify",
		"quote",
		"emoticon",
		"image",
		// 'video',
		"table",
		"code",
		"splitLine",
		"undo",
		"redo"
	];
	// 自定义上传图片
	editor.config.customUploadImg = (resultFiles, insertImgFn) => {
		// resultFiles 是 input 中选中的文件列表
		// insertImgFn 是获取图片 url 后，插入到编辑器的方法
		resultFiles.forEach((item, i) => {
			const formData = new FormData();
			formData.append("file", item);
			console.log("----模拟【图片上传接口】,真实数据需要填写constant.js里的接口域名------");
			// 图片上传接口
			// publicUploadFile(formData)
			//   .then(res => {
			//         insertImgFn(res.obj.src)
			//   })
			//   .catch(err => {
			//   })
		});
	};

	editor.create();
};

// 编辑相关
watch(
	() => props.detail,
	val => {
		if (val) {
			editor.txt.html(val);
		}
	}

);

const onSubmitClick = async() => {
	console.log(editor.txt.html());
	if (props.detail && props.detail._id) {

		// 编辑文章
		// await editArticle({
		//   id: props.detail._id,
		//   title: props.title,
		//   content: editor.txt.html()
		// })
	} else {
		// 创建文章
		// await commitArticle({
		//   title: props.title,
		//   content: editor.txt.html()
		// })
	}

	editor.txt.html("");
	emits("onSuccess");
};
</script>