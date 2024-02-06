<template>
	<el-dialog
		title="设置角色"
		:model-value="modelValue"
		width="30%"
		align-center
		draggable
		@close="closed"
	>
		<el-checkbox-group v-model="userRoleTitleList">
			<el-checkbox
				v-for="item in allRoleList"
				:key="item.id"
				:label="item.name"
			></el-checkbox>
		</el-checkbox-group>

		<template #footer>
			<span class="dialog-footer">
				<el-button @click="closed">取消</el-button>
				<el-button type="primary" @click="onConfirm">确认</el-button>
			</span>
		</template>
	</el-dialog>
</template>

<style lang="scss" scoped></style>

<script setup>
import { defineProps, defineEmits, ref, watch, nextTick } from "vue";
import { getRoleList } from "@/api/api";
import { ElMessage } from "element-plus";

const props = defineProps({
	modelValue: {
		type: Boolean,
		required: true
	},
	userId: {
		type: String,
		required: true
	}
});

const emits = defineEmits(["update:modelValue", "updateRole"]);

// 当前用户角色
const userRoleTitleList = ref([]);
// 获取当前用户角色
const getUserRoles = async() => {
	// const res = await userRoles(props.userId)
	// userRoleTitleList.value = res.role.map(item => item.title)

	await nextTick();
	userRoleTitleList.value = [props.userId];
};
// 所有角色
const allRoleList = ref([]);
// 获取所有角色数据的方法
const getListData = async() => {
	const data = await getRoleList();
	allRoleList.value = data.objs;
	await getUserRoles();
};

watch(
	() => props.userId,
	val => {
		if (val) {
			getListData();
		}
	}
);

/**
  确定按钮点击事件
 */
const onConfirm = async() => {
	// 处理数据结构
	// const roles = userRoleTitleList.value.map(title => {
	//   return allRoleList.value.find(role => role.title === title)
	// })
	// await updateRole(props.userId, roles)

	ElMessage.success("角色更新成功");
	closed();
	// 角色更新成功,去请求父组件列表数据
	emits("updateRole");
};

/**
 * 关闭
 */
const closed = () => {
	emits("update:modelValue", false);
};
</script>