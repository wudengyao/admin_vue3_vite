<template>
	<el-dialog
		title="配置权限"
		:model-value="modelValue"
		width="30%"
		align-center
		draggable
		@close="onClose"
	>
		<el-tree
			ref="treeRef"
			:data="allPermission"
			show-checkbox
			node-key="id"
			default-expand-all
			:props="defaultProps"
		>
		</el-tree>

		<template #footer>
			<span class="dialog-footer">
				<el-button @click="onClose">取消</el-button>
				<el-button type="primary" @click="onConfirm">确定</el-button>
			</span>
		</template>
	</el-dialog>
</template>

<style lang="scss" scoped></style>

<script setup>
import { defineProps, defineEmits, ref, watch, nextTick } from "vue";
import { getPermission } from "@/api/api";
import { ElMessage } from "element-plus";

const props = defineProps({
	modelValue: {
		type: Boolean,
		required: true
	},
	roleId: {
		type: String,
		required: true
	}
});
const emits = defineEmits(["update:modelValue"]);

// 所有权限
const allPermission = ref([]);
const getPermissionList = async() => {
	const data = await getPermission();

	allPermission.value = data.obj;
};
getPermissionList();

// 属性结构配置
const defaultProps = {
	children: "secondMenuList",
	label: "name"
};

// tree 节点
const treeRef = ref(null);
// 获取当前用户角色的权限
const getRolePermission = async() => {
	// 真实情况这里是接口获取，我们这里模拟一个数组
	const treeData = ["1", "1-1", "1-2", "2", "2-1", "2-2", "3", "3-1", "3-2"];
	// 随机从数组中获取一个值
	const key = treeData[Math.floor((Math.random() * treeData.length))];
	const checkedKeys = [key];
	// el-tree数据渲染完成
	await nextTick();
	treeRef.value.setCheckedKeys(checkedKeys);
};
//
watch(
	() => props.roleId,
	val => {
		if (val) getRolePermission();
	}
);

/**
  确定按钮点击事件
 */
const onConfirm = () => {
	// await distributePermission({
	//   roleId: props.roleId,
	//   permissions: treeRef.value.getCheckedKeys()
	// })
	console.log(treeRef.value.getCheckedKeys());
	ElMessage.success("用户角色更新成功");
	onClose();
};

/**
 * 关闭
 */
const onClose = () => {
	emits("update:modelValue", false);
};
</script>