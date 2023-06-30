<template>
  <div class="navbar">
    <!--菜单栏伸缩组件-->
    <hamburger class="hamburger-container"/>
    <!--面包屑组件-->
    <breadcrumb id="guide-breadcrumb" class="breadcrumb-container"/>
    <div class="right-menu">
      <!-- 引导组件-->
      <guide class="right-menu-item hover-effect" />
      <!--全屏组件-->
      <screenfull class="right-menu-item hover-effect"/>
      <!-- 登录账号信息 -->
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
          <el-image
              class="avatar"
              :src="$store.getters.userInfo.avatar"></el-image>
          <div>{{ $store.getters.userInfo.admin_nick_name }}</div>
          <CaretBottom style="width: 1em; height: 1em; margin-left: 4px;"/>

        </div>
        <template #dropdown>
          <el-dropdown-menu class="user-dropdown">
            <router-link to="/">
              <el-dropdown-item> 首页</el-dropdown-item>
            </router-link>
            <el-dropdown-item @click="logout">
              退出登录
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup>
import {CaretBottom} from '@element-plus/icons'
import {} from 'vue'
import {useStore} from 'vuex'
import Hamburger from '@/components/Hamburger'
import Breadcrumb from '@/components/Breadcrumb'
import Screenfull from '@/components/Screenfull'
import Guide from '@/components/Guide'

const store = useStore()

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

