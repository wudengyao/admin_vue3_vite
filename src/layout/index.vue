<template>
	<div
		class="app-wrapper"
		:class="[$store.getters.sidebarOpened ? 'openSidebar' : 'hideSidebar']"
	>
		<!-- 左侧 menu -->
		<sidebar
			id="guide-sidebar"
			class="sidebar-container"
			:style="{ backgroundColor: variables.menuBg }"
		/>
		<div class="main-container">
			<div class="fixed-header">
				<!-- 顶部的 navbar -->
				<navbar />
				<!-- tags -->
				<tags-view></tags-view>
			</div>
			<!-- 内容区 -->
			<app-main />
		</div>
	</div>
</template>

<style lang="scss" scoped>
@import '@/styles/mixin.scss';
@import '@/styles/variables.module.scss';
  .app-wrapper {
    @include clearfix;
    position: relative;
    width: 100%;
    height: 100%;
  }
  .fixed-header {
    position: fixed;
    right: 0;
    top: 0;
    z-index: 9;
    width: calc(100% - #{$sideBarWidth});
    transition: width #{$sideBarDuration};  }
  .hideSidebar .fixed-header {
    width: calc(100% - #{$hideSideBarWidth});
  }
</style>

<script setup>
import {} from "vue";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import AppMain from "./components/AppMain";
import variables from "@/styles/variables.module.scss";
import TagsView from "@/components/TagsView";
import store from "@/store";

</script>