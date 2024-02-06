<template>
	<div>
		<el-row :gutter="20">
			<!--部门数据-->
			<el-col :span="4" :xs="24">
				<div class="head-container">
					<el-input
						v-model="authName"
						placeholder="请输入权限名称搜索"
						clearable
						prefix-icon="Search"
						style="margin-bottom: 20px"
					/>
				</div>
				<div class="head-container">
					<el-tree
						ref="authTreeRef"
						:data="allPermission"
						:props="{ label: 'name', children: 'children' }"
						:expand-on-click-node="false"
						:filter-node-method="filterNode"
						node-key="id"
						highlight-current
						default-expand-all
						@node-click="handleNodeClick"
					/>
				</div>
			</el-col>
			<!--用户数据-->
			<el-col :span="20" :xs="24">
				<el-card>
					<el-table
						:data="allPermission"
						style=" margin-bottom: 20px;width: 100%"
						row-key="id"
						border
						default-expand-all
						:tree-props="{ children: 'children', hasChildren: 'hasChildren' }"
					>
						<el-table-column
							prop="name"
							label="权限名称"
							width="200"
						>
						</el-table-column>
						<el-table-column
							prop="url"
							label="权限标志"
							width="300"
						>
							<template #default="{ row }">
								<div style="display: flex;justify-content: space-between;align-items: center;">
									<div>{{row.url}}</div>
									<el-link
										v-copyText="row.url" v-copyText:callback="copyTextSuccess" :underline="false"
										:icon="CopyDocument" type="warning"
									>
										复制
									</el-link>
								</div>
							</template>
						</el-table-column>

						<el-table-column
							prop="hidden"
							label="是否显示在菜单列表"
							width="280"
						>
							<template #default="{ row }">
								<el-tag v-if="row.hidden" type="danger">否</el-tag>
								<el-tag v-else type="success">是</el-tag>
							</template>
						</el-table-column>

						<el-table-column prop="buttonList" label="所在页面的按钮权限" min-width="280">
							<template #default="{ row }">
								<el-tag
									v-for="(item, index) in row.buttonList"
									:key="index"
									class="remark"
									size="small"
								>
									{{item.name}}
								</el-tag>
							</template>
						</el-table-column>
					</el-table>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<style lang="scss" scoped>
.remark {
  margin-right: 12px;
}
</style>

<script setup>
import { getPermission } from "@/api/api";
import { ref, watch } from "vue";
import { ElMessage } from "element-plus";
import { CopyDocument } from "@element-plus/icons";

// 所有权限
const allPermission = ref([]);
const getPermissionListData = async() => {
	const data = await getPermission();
	allPermission.value = data.obj;
};
getPermissionListData();
/** 复制代码成功 */
const copyTextSuccess = () => {
	ElMessage.success("复制成功");
};

const authName = ref("");
const authTreeRef = ref(null);
/** 根据名称筛选部门树 */
watch(authName, val => {
	authTreeRef.value.filter(val);
});

/** 通过条件过滤节点  */
const filterNode = (value, data) => {
	if (!value) return true;
	return data.name.indexOf(value) !== -1;
};

/** 节点单击事件 */
function handleNodeClick(data) {
	ElMessage.success("测试输出结点id：" + data.id);
}

</script>

<script>
export default {
	name: "permission-list"
};
</script>