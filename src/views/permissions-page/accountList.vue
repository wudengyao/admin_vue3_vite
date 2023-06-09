<template>
  <div class="home-box">
    <el-form :inline="true" :model="searchForm">
      <el-form-item label="账号">
        <el-input v-model="searchForm.account" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item label="角色">

        <el-select v-model="searchForm.role" placeholder="角色">
          <el-option
              v-for="item in roleList"
              :key="item.id"
              :label="item.name"
              :value="item.id"
          />
        </el-select>
      </el-form-item>

      <el-form-item>
        <el-button
            type="primary"
            @click="searchEvent"
            v-auth="'/adminAuth/adminList'"
            style="margin-left: -16px"
        >查询
        </el-button>
      </el-form-item>
    </el-form>
    <el-card>
      <el-table :data="tableData"
                v-loading="loading"
                element-loading-text="加载中..."
                border>
        <el-table-column prop="id" label="ID" width="180"></el-table-column>
        <el-table-column prop="account" label="账号" width="180">
        </el-table-column>
        <el-table-column label="角色" width="180">
          <template #default="{ row }">
            <el-tag type="danger">{{ row.role_name }}</el-tag>
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
            <span>{{ row.is_lock == "1" ? "冻结" : "正常" }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="date" label="操作时间" width="280">
        </el-table-column>


        <el-table-column prop="address" label="操作" min-width="160">
          <template #default="{ row }">
            <el-button
                type="primary"
                size="small"
                @click="onShowClick(row._id)">查看
            </el-button>
            <el-button
                type="info"
                size="small"
                @click="onShowRoleClick(row)">角色
            </el-button>
            <el-button
                type="danger"
                size="small"
                @click="onRemoveClick(row)">删除
            </el-button>

          </template>
        </el-table-column>
      </el-table>
      <el-pagination
          class="pagination"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="searchForm.page"
          :page-sizes="[10, 20, 30, 50, 100]"
          :page-size="searchForm.page_size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
      >
      </el-pagination>
    </el-card>

    <roles-dialog
        v-model="roleDialogVisible"
        :userId="selectUserId"
        @updateRole="getListData"
    ></roles-dialog>

  </div>
</template>
<script>
export default {
  name: "adminList",
};
</script>
<script setup>
import RolesDialog from './components/roles.vue'

import {ref, onMounted, watch} from "vue";
import {getAdmintorList, getRoleList} from "@/api/api";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import {
  Delete,
  Edit,
  Search
} from '@element-plus/icons-vue'
import {ElMessageBox, ElMessage} from 'element-plus'

const router = useRouter()

//数据源
const searchForm = ref({
  account: "",
  role: '',
  page: 1,
  page_size: 20,
});

const tableData = ref([]);
const total = ref(0);
const loading = ref(false)
const roleList = ref([]);

onMounted(() => {
  getListData();
  getRoleData()
});

/**
 * 获取账号列表
 */
const getListData = async () => {
  loading.value = true
  await getAdmintorList(searchForm.value)
      .then(data => {
        setTimeout(() => {
          tableData.value = data.bizobj
          total.value = Number(data.page_info.total_items);
          loading.value = false
        }, 1000)
      })
      .catch(err => {
        loading.value = false

      })
};

/**
 * 获取角色列表
 */
const getRoleData = async () => {
  await getRoleList()
      .then(data => {
        roleList.value = data.bizobj

      })
      .catch(err => {

      })
};
/**
 * 查看按钮点击事件
 */
const onShowClick = id => {
  router.push(`/user/info/${id}`)
}


/**
 * 删除按钮点击事件
 */
const onRemoveClick = row => {
  ElMessageBox.confirm(
      "确定要删除" + row.account + "吗",
      {type: 'warning'}
  ).then(async () => {
    // await deleteUser(row._id)
    ElMessage.success("删除成功")
    // 重新渲染数据
    await getListData()
  })
}

/**
 * 查看角色的点击事件
 */
const selectUserId = ref('')
const roleDialogVisible = ref(false)
const onShowRoleClick = row => {
  //真实环境应该获取用户id，但这里mock数据我们直接使用角色名字去匹配
  selectUserId.value = row.role_name
  roleDialogVisible.value = true
}

// 保证每次打开重新获取用户角色数据
watch(roleDialogVisible, val => {
  if (!val) selectUserId.value = ''
})

const handleSizeChange = (val) => {
  searchForm.value.page_size = val;
  getListData();
};
const handleCurrentChange = (val) => {
  searchForm.value.page = val;
  getListData();
};

const searchEvent = () => {
  console.log(searchForm.value)
  searchForm.value.page = 1;
  getListData();
};
</script>

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
    width: 60px;
    height: 60px;
    border-radius: 50%;
  }

  .pagination {
    margin-top: 20px;
    display: flex;
    justify-content: end;
  }
}
</style>
