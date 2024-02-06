<template>
	<el-breadcrumb class="breadcrumb" separator="/">
		<transition-group name="breadcrumb">
			<el-breadcrumb-item
				v-for="(item, index) in breadcrumbData"
				:key="item.path"
			>
				<!-- 不可点击项 -->
				<span v-if="index === breadcrumbData.length - 1" class="no-redirect">{{item.meta.title}}</span>
				<!-- 可点击项 -->
				<a v-else class="redirect" @click.prevent="onLinkClick(item)">{{item.meta.title}}</a>
			</el-breadcrumb-item>
		</transition-group>
	</el-breadcrumb>
</template>

<style lang="scss" scoped>
  .breadcrumb {
    display: inline-block;
    margin-left: 8px;
    line-height: 50px;
    font-size: 14px;
    .no-redirect {
      cursor: text;
      color: #97a8be;
    }
    .redirect {
      font-weight: 600;
      color: #666;
    }
    .redirect:hover {
      text-decoration:underline;
      font-weight: 900;
      // 如果将来需要进行主题替换，所以这里不去写死样式
      color: v-bind(linkhovercolor)

    }
  }
</style>

<script setup>
import { ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";

const route = useRoute();
// 生成数组数据
const breadcrumbData = ref([]);
const getBreadcrumbData = () => {
	breadcrumbData.value = route.matched.filter(
		item => item.meta && item.meta.title
	);
};
// 监听路由变化时触发
watch(
	route,
	() => {
		getBreadcrumbData();
	},
	{
		immediate: true
	}
);

// 处理点击事件
const router = useRouter();
const onLinkClick = item => {
	// console.log(item)
	router.push(item.path);
};

// 如果将来需要进行主题替换，所以这里获取下动态样式
// const store = useStore();
// const linkHoverColor = ref(store.getters.cssVar.menuBg);
</script>