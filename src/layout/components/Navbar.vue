<template>
	<div class="navbar">
		<!--菜单栏伸缩组件-->
		<hamburger class="hamburger-container" />
		<!--面包屑组件-->
		<breadcrumb class="breadcrumb-container" />
		<div class="right-menu">
			<!-- 引导组件-->
			<guide class="right-menu-item hover-effect" />
			<!--页面搜索组件-->
			<header-search class="right-menu-item hover-effect"></header-search>
			<!--全屏组件-->
			<screenfull class="right-menu-item hover-effect" />
			<!-- 登录账号信息 -->
			<el-dropdown class="avatar-container" trigger="click">
				<div class="avatar-wrapper">
					<el-image
						class="avatar"
						:src="$store.getters.userInfo.avatar"
					></el-image>
					<div>{{$store.getters.userInfo.admin_nick_name}}</div>
					<CaretBottom style=" margin-left: 4px;width: 1em; height: 1em;" />
				</div>
				<template #dropdown>
					<el-dropdown-menu class="user-dropdown">
						<router-link to="/">
							<el-dropdown-item> 首页</el-dropdown-item>
						</router-link>
						<el-dropdown-item @click="editCropper">
							修改头像
						</el-dropdown-item>
						<el-dropdown-item @click="logout">
							退出登录
						</el-dropdown-item>
					</el-dropdown-menu>
				</template>
			</el-dropdown>
		</div>

		<el-dialog
			v-model="open" :title="title"
			align-center width="800px" append-to-body @opened="modalOpened" @close="closeDialog"
		>
			<el-row>
				<el-col :xs="24" :md="12" :style="{ height: '350px' }">
					<vue-cropper
						v-if="visible"
						ref="cropper"
						:img="options.img"
						:info="true"
						:auto-crop="options.autoCrop"
						:auto-crop-width="options.autoCropWidth"
						:auto-crop-height="options.autoCropHeight"
						:fixed-box="options.fixedBox"
						:output-type="options.outputType"
						@realTime="realTime"
					/>
				</el-col>
				<el-col :xs="24" :md="12" :style="{ height: '350px' }">
					<div class="avatar-upload-preview">
						<img :src="options.previews.url" :style="options.previews.img" />
					</div>
				</el-col>
			</el-row>
			<br />
			<el-row>
				<el-col :lg="2" :md="2">
					<el-upload
						action="#"
						:http-request="requestUpload"
						:show-file-list="false"
						:before-upload="beforeUpload"
					>
						<el-button>
							选择
							<el-icon class="el-icon--right"><Upload /></el-icon>
						</el-button>
					</el-upload>
				</el-col>
				<el-col :lg="{ span: 1, offset: 2 }" :md="2">
					<el-button icon="Plus" @click="changeScale(1)"></el-button>
				</el-col>
				<el-col :lg="{ span: 1, offset: 1 }" :md="2">
					<el-button icon="Minus" @click="changeScale(-1)"></el-button>
				</el-col>
				<el-col :lg="{ span: 1, offset: 1 }" :md="2">
					<el-button icon="RefreshLeft" @click="rotateLeft()"></el-button>
				</el-col>
				<el-col :lg="{ span: 1, offset: 1 }" :md="2">
					<el-button icon="RefreshRight" @click="rotateRight()"></el-button>
				</el-col>
				<el-col :lg="{ span: 2, offset: 6 }" :md="2">
					<el-button type="primary" @click="uploadImg()">提 交</el-button>
				</el-col>
			</el-row>
		</el-dialog>
	</div>
</template>

<style lang="scss" scoped>
.navbar {
  overflow: hidden;
  position: relative;
  height: 50px;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  .breadcrumb-container {
    float: left;
  }
  .right-menu {
    display: flex;
    float: right;
    align-items: center;
    padding-right: 16px;
    ::v-deep .right-menu-item {
      display: inline-block;
      padding: 0 18px 0 0;
      vertical-align: text-bottom;
      font-size: 24px;
      color: #5a5e66;
      &.hover-effect {
        cursor: pointer;
        transition: background 0.3s;
        &:hover {
          background: rgba(0, 0, 0, 0.025);
        }
      }
    }
    ::v-deep .avatar-container {
      cursor: pointer;
      .avatar-wrapper {
        display: flex;
        position: relative;
        align-items: center;
        margin-top: 5px;
        height: 50px;
        line-height: 50px;

      }
    }
  }
  .hamburger-container {
    float: left;
    height: 100%;
    cursor: pointer;
    line-height: 46px;
    // hover 动画
    transition: background 0.5s;
    &:hover {
      background: rgba(0, 0, 0, 0.1);
    }
  }
  ::v-deep .avatar {
    margin-right: 5px;
    border-radius: 50%;
    width: 30px;
    height: 30px;
  }
}
</style>

<script setup>
import "vue-cropper/dist/index.css";
import { VueCropper } from "vue-cropper";
import { CaretBottom } from "@element-plus/icons";
import { ref, reactive } from "vue";
import { useStore } from "vuex";
import Hamburger from "@/components/Hamburger";
import Breadcrumb from "@/components/Breadcrumb";
import Screenfull from "@/components/Screenfull";
import Guide from "@/components/Guide";
import HeaderSearch from "@/components/HeaderSearch";
import { ElMessage } from "element-plus";

const store = useStore();

const open = ref(false);
const visible = ref(false);
const title = ref("修改头像");
const cropper = ref(null);

// 图片裁剪数据
const options = reactive({
	img: store.getters.userInfo.avatar, // 裁剪图片的地址
	autoCrop: true, // 是否默认生成截图框
	autoCropWidth: 200, // 默认生成截图框宽度
	autoCropHeight: 200, // 默认生成截图框高度
	fixedBox: true, // 固定截图框大小 不允许改变
	outputType: "png", // 默认生成截图为PNG格式
	previews: {} // 预览数据
});

/** 编辑头像 */
function editCropper() {
	open.value = true;
}
/** 打开弹出层结束时的回调 */
function modalOpened() {
	visible.value = true;
}
/** 覆盖默认上传行为 */
function requestUpload() {}
/** 向左旋转 */
function rotateLeft() {
	cropper.value.rotateLeft();
}
/** 向右旋转 */
function rotateRight() {
	cropper.value.rotateRight();
}
/** 图片缩放 */
function changeScale(num) {
	num = num || 1;
	cropper.value.changeScale(num);
}
/** 上传预处理 */
function beforeUpload(file) {
	if (file.type.indexOf("image/") == -1) {
		ElMessage.error("文件格式错误，请上传图片类型,如：JPG，PNG后缀的文件。");
	} else {
		const reader = new FileReader();
		reader.readAsDataURL(file);
		reader.onload = () => {
			options.img = reader.result;
		};
	}
}
/** 上传图片 */
function uploadImg() {
	cropper.value.getCropBlob(data => {
		const formData = new FormData();
		console.log("uploadImg", data);
		formData.append("avatarfile", data);
		// uploadAvatar(formData).then(response => {
		open.value = false;
		//   options.img = import.meta.env.VITE_APP_BASE_API + response.imgUrl;
		//   userStore.avatar = options.img;
		ElMessage.success("修改成功");
		//
		visible.value = false;
		// });
	});
}
/** 实时预览 */
function realTime(data) {
	options.previews = data;
}
/** 关闭窗口 */
function closeDialog() {
	options.img = store.getters.userInfo.avatar;
	options.visible = false;
}

const logout = () => {
	store.dispatch("user/logout");
};
</script>