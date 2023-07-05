<template>
  <div class="navbar">
    <!--菜单栏伸缩组件-->
    <hamburger class="hamburger-container"/>
    <!--面包屑组件-->
    <breadcrumb class="breadcrumb-container"/>
    <div class="right-menu">
      <!-- 引导组件-->
      <guide class="right-menu-item hover-effect" />
      <!--页面搜索组件-->
      <header-search class="right-menu-item hover-effect"></header-search>
      <!--全屏组件-->
      <screenfull class="right-menu-item hover-effect"/>
      <!-- 登录账号信息 -->
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
          <el-image
              class="avatar"
              :src="$store.getters.userInfo.avatar"
          ></el-image>
          <div>{{ $store.getters.userInfo.admin_nick_name }}</div>
          <CaretBottom style="width: 1em; height: 1em; margin-left: 4px;"/>

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

    <el-dialog :title="title"     align-center
               v-model="open" width="800px" append-to-body @opened="modalOpened" @close="closeDialog">
      <el-row>
        <el-col :xs="24" :md="12" :style="{ height: '350px' }">
          <vue-cropper
              ref="cropper"
              :img="options.img"
              :info="true"
              :autoCrop="options.autoCrop"
              :autoCropWidth="options.autoCropWidth"
              :autoCropHeight="options.autoCropHeight"
              :fixedBox="options.fixedBox"
              :outputType="options.outputType"
              @realTime="realTime"
              v-if="visible"
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

<script setup>
import "vue-cropper/dist/index.css";
import { VueCropper } from "vue-cropper";
import {CaretBottom} from '@element-plus/icons'
import {} from 'vue'
import {ref,reactive} from 'vue'
import {useStore} from 'vuex'
import Hamburger from '@/components/Hamburger'
import Breadcrumb from '@/components/Breadcrumb'
import Screenfull from '@/components/Screenfull'
import {ElMessage} from "element-plus";

const store = useStore()

const open = ref(false);
const visible = ref(false);
const title = ref("修改头像");
const cropper = ref(null)

//图片裁剪数据
const options = reactive({
  img: store.getters.userInfo.avatar, // 裁剪图片的地址
  autoCrop: true, // 是否默认生成截图框
  autoCropWidth: 200, // 默认生成截图框宽度
  autoCropHeight: 200, // 默认生成截图框高度
  fixedBox: true, // 固定截图框大小 不允许改变
  outputType: "png", // 默认生成截图为PNG格式
  previews: {} //预览数据
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
    ElMessage.error("文件格式错误，请上传图片类型,如：JPG，PNG后缀的文件。")

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
    let formData = new FormData();
    console.log("uploadImg",data)
    formData.append("avatarfile", data);
    // uploadAvatar(formData).then(response => {
    open.value = false;
    //   options.img = import.meta.env.VITE_APP_BASE_API + response.imgUrl;
    //   userStore.avatar = options.img;
    ElMessage.success("修改成功")
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
  options.img = store.getters.userInfo.avatar
  options.visible = false;
}


const logout = () => {
  store.dispatch('user/logout')
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);

  .breadcrumb-container {
    float: left;
  }

  .right-menu {
    display: flex;
    align-items: center;
    float: right;
    padding-right: 16px;

    ::v-deep .right-menu-item {
      display: inline-block;
      padding: 0 18px 0 0;
      font-size: 24px;
      color: #5a5e66;
      vertical-align: text-bottom;

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
        margin-top: 5px;
        position: relative;
        display: flex;
        align-items: center;
        height: 50px;
        line-height: 50px;

      }
    }
  }

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    // hover 动画
    transition: background 0.5s;

    &:hover {
      background: rgba(0, 0, 0, 0.1);
    }
  }

  ::v-deep .avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 5px;
  }
}
</style>


