<template>
	<div>
		<!--  定义一个公用布局-->
		<DefineBiz v-slot="{ msg, $slots }">
			<!--    具名插槽-->
			<component :is="$slots.header" />
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>内容: {{msg}}</div>
			<div>可能还有更多...</div>
			<!--    默认插槽-->
			<component :is="$slots.default" />
		</DefineBiz>

		<!--  第一个例子-->
		<ReuseBiz msg="example 1">
			<template #header>
				<div>我是第一个header</div>
			</template>
			<div>我是第一个默认插槽</div>
		</ReuseBiz>

		<br>

		<!--  第二个例子-->
		<ReuseBiz msg="example 2">
			<template #header>
				<div>我是第二个header</div>
			</template>
			<div>我是第二个默认插槽</div>
		</ReuseBiz>
	</div>
</template>

<style scoped>

</style>
<script>
</script>

<script setup>
import { createReusableTemplate } from "@vueuse/core";

const [DefineBiz, ReuseBiz] = createReusableTemplate();

</script>