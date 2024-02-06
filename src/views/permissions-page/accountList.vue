<template>
	<div class="home-box">
		<el-form v-show="showSearch" :inline="true" :model="searchForm">
			<el-form-item label="账号ID" prop="id">
				<el-input-number v-model="searchForm.id" controls-position="right" :min="0" />
			</el-form-item>
			<el-form-item label="账号">
				<el-input v-model="searchForm.account" placeholder="账号" clearable></el-input>
			</el-form-item>
			<el-form-item label="角色">
				<el-select v-model="searchForm.role" placeholder="角色" clearable>
					<el-option
						v-for="item in roleList"
						:key="item.id"
						:label="item.name"
						:value="item.id"
					/>
				</el-select>
			</el-form-item>

			<el-form-item label="操作时间" style="width: 308px;">
				<el-date-picker
					v-model="searchForm.date"
					value-format="YYYY-MM-DD"
					type="daterange"
					range-separator="-"
					start-placeholder="开始日期"
					end-placeholder="结束日期"
				></el-date-picker>
			</el-form-item>

			<el-form-item>
				<el-button
					v-auth="'/adminAuth/list'"
					type="primary"
					style="margin-left: -16px"
					@click="searchEvent"
				>
					查询
				</el-button>
			</el-form-item>
		</el-form>

		<right-toolbar
			v-model:showSearch="showSearch"
			@queryTable="getListData"
			@onImportClick="handleImport"
			@onOutClick="onDownTemplate"
			@onAddClick="onDownTemplate"
		></right-toolbar>
		<el-card>
			<el-table
				v-loading="loading"
				:data="tableData"
				element-loading-text="加载中..."
				border
			>
				<el-table-column prop="id" label="ID" width="180"></el-table-column>
				<el-table-column prop="account" label="账号" width="180">
				</el-table-column>
				<el-table-column label="角色" width="180">
					<template #default="{ row }">
						<el-tag type="danger">{{row.role_name}}</el-tag>
					</template>
				</el-table-column>
				<el-table-column label="头像" align="center">
					<template #default="{ row }">
						<el-image
							class="avatar"
							:src="row.avatar"
						></el-image>
					</template>
				</el-table-column>
				<el-table-column label="状态" width="180">
					<template #default="{ row }">
						<span>{{row.is_lock == "1" ? "冻结" : "正常"}}</span>
					</template>
				</el-table-column>
				<el-table-column prop="date" label="操作时间" width="280">
				</el-table-column>

				<el-table-column prop="address" label="操作" min-width="280">
					<template #default="{ row }">
						<el-button
							v-auth="'/adminAuth/look'"
							type="primary"
							size="small"
							@click="onShowClick(row)"
						>
							查看
						</el-button>
						<el-button
							v-auth="'/adminAuth/role'"
							type="info"
							size="small"

							@click="onShowRoleClick(row)"
						>
							角色
						</el-button>
						<el-button
							v-auth="'/adminAuth/del'"
							type="danger"
							size="small"

							@click="onRemoveClick(row)"
						>
							删除
						</el-button>
					</template>
				</el-table-column>
			</el-table>

			<!--分页组件-->
			<pagination
				v-show="total > 0"
				v-model:page="searchForm.page"
				v-model:limit="searchForm.page_size"
				:total="total"
				@pagination="getListData"
			/>
		</el-card>

		<!--角色组件-->
		<roles-dialog
			v-model="roleDialogVisible"
			:user-id="selectUserId"
			@updateRole="getListData"
		>
		</roles-dialog>

		<!-- 用户导入对话框 -->
		<UploadExcel
			v-model="upload.open"
			:title="upload.upLoadTitle"
			:url="switchServerUrl()+ '/public/uploadFile'"
			@onSuccess="onSuccess"
			@onDownTemplate="onDownTemplate"
		>
		</UploadExcel>
	</div>
</template>
<style lang="scss" scoped>
.home-box {
  .header {
    margin-bottom: 22px;
    text-align: right;
  }
  ::v-deep .el-tag {
    margin-right: 6px;
  }
  ::v-deep .avatar {
    border-radius: 50%;
    width: 60px;
    height: 60px;
  }

}
</style>

<script setup>
import RolesDialog from "./components/roles.vue";
import UploadExcel from "@/components/UploadExcel";

import { ref, onMounted, watch } from "vue";
import { getAdmintorList, getRoleList } from "@/api/api";
import { useRouter } from "vue-router";
import { ElMessageBox, ElMessage } from "element-plus";
import { switchServerUrl } from "@/utils/index";

const router = useRouter();

const showSearch = ref(true);

// 数据源
const searchForm = ref({
	id: 0,
	account: "",
	role: "",
	date: "",
	page: 1,
	page_size: 20
});

const tableData = ref([]);
const total = ref(0);
const loading = ref(false);
const roleList = ref([]);

onMounted(() => {
	getListData();
	getRoleData();
});

/**
 * 获取账号列表
 */
const getListData = async() => {
	loading.value = true;
	await getAdmintorList(searchForm.value)
		.then(data => {
			setTimeout(() => {
				tableData.value = data.obj;
				total.value = Number(data.page_info.total_items);
				loading.value = false;
			}, 1000);
		})
		.catch(() => {
			loading.value = false;
		});
};

/**
 * 获取角色列表
 */
const getRoleData = async() => {
	await getRoleList()
		.then(data => {
			roleList.value = data.obj;
		})
		.catch(() => {

		});
};
/**
 * 查看按钮点击事件
 */
const onShowClick = row => {
	router.push({
		path: "/account/detail",
		query: row
	});
};
/**
 * 删除按钮点击事件
 */
const onRemoveClick = row => {
	ElMessageBox.confirm(
		"确定要删除" + row.account + "吗",
		{ type: "warning" }
	).then(async() => {
		// await deleteUser(row._id)
		ElMessage.success("删除成功");
		// 重新渲染数据
		await getListData();
	});
};

/**
 * 查看角色的点击事件
 */
const selectUserId = ref("");
const roleDialogVisible = ref(false);
const onShowRoleClick = row => {
	// 真实环境应该获取用户id，但这里mock数据我们直接使用角色名字去匹配
	selectUserId.value = row.role_name;
	roleDialogVisible.value = true;
};

// 保证每次打开重新获取用户角色数据
watch(roleDialogVisible, val => {
	if (!val) selectUserId.value = "";
});

const searchEvent = () => {
	console.log(searchForm.value);
	searchForm.value.page = 1;
	getListData();
};

/** * 用户导入参数 */
const upload = ref({
	// 是否显示弹出层（用户导入）
	open: false,
	// 弹出层标题（用户导入）
	upLoadTitle: "账号导入"
});

/** 导入按钮操作 */
function handleImport() {
	upload.value.open = true;
}
/** 文件上传成功处理 */
const onSuccess = (response, file, fileList) => {
	upload.value.open = false;
	getListData();
};
const onDownTemplate = () => {
	ElMessage.error("演示模式");
};
</script>

<script>
export default {
	name: "admin-list"
};
</script>