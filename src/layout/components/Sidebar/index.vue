<template>
  <div class="">
    <div class="logo-container">
      <el-avatar
        :size="logoHeight"
        shape="square"
        src="https://osstest.eetop.com/bewt365/578d0d88e7ad2f9ae99f10eee8e08d9c.jpg"
      />
      <h1 class="logo-title" v-if="$store.getters.sidebarOpened">
        Vue3后台系统
      </h1>
    </div>
    <el-scrollbar>
      <sidebar-menu></sidebar-menu>
    </el-scrollbar>
  </div>
</template>

<script setup>
import SidebarMenu from "./SidebarMenu";
import {} from "vue";

const logoHeight = 32;
</script>

<style lang="scss" scoped>
.logo-container {
  height: v-bind(logoHeight) + "px";
  padding: 10px 0 22px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  .logo-title {
    margin-left: 10px;
    color: #fff;
    font-weight: 600;
    line-height: 50px;
    font-size: 16px;
    white-space: nowrap;
  }
}
</style>
