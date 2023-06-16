<template>
  <div class="home-box">
    <el-form :inline="true" :model="searchForm" v-show="showSearch">
      <el-form-item label="角色ID" prop="id">
        <el-input-number v-model="searchForm.id" controls-position="right" :min="0" />
      </el-form-item>
      <el-form-item label="角色名称">
        <el-input v-model="searchForm.name" placeholder="角色名称" clearable></el-input>
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
            @click="searchEvent"
            type="primary"
            v-auth="'/adminAuth/getRoleList'"
            style="margin-left: -16px"
        >查询
        </el-button>

      </el-form-item>
    </el-form>

    <right-toolbar v-model:showSearch="showSearch" @queryTable="getListData" :haveImport="false"
                   @onOutClick="onDownTemplate"
                   @onAddClick="onDownTemplate"></right-toolbar>
    <el-card>
      <el-table :data="tableData"
                v-loading="loading"
                element-loading-text="加载中..."
                border>
        <el-table-column prop="id" label="角色ID" width="180">
        </el-table-column>
        <el-table-column prop="name" label="角色名称" width="180">
        </el-table-column>

        <el-table-column label="操作时间" min-width="160">
          <template #default="{ row }">
            {{ $filters.dateFilter(row.operator, 'YYYY-MM-DD HH:mm:ss') }}
          </template>
        </el-table-column>

        <el-table-column prop="address" label="操作" min-width="160">
          <template #default="{ row }">
            <el-button
                type="primary"
                size="small"
                v-auth="'/adminAuth/setting'"
                @click="handleEdit(row)">配置权限
            </el-button>
          </template>
        </el-table-column>
      </el-table>


      <pagination
          v-show="total > 0"
          :total="total"
          v-model:page="searchForm.page"
          v-model:limit="searchForm.page_size"
          @pagination="getListData"
      />
    </el-card>

    <distribute-permission
        v-model="distributePermissionVisible"
        :roleId="selectRoleId">
    </distribute-permission>


  </div>

</template>
<script>
export default {
  name: "getRoleList",
};
</script>
<script setup>
import DistributePermission from './components/distributePermission.vue'

import {ref, onMounted, reactive} from "vue";
import {getRoleList} from "@/api/api";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import {ElMessage} from "element-plus";

const showSearch = ref(true);

onMounted(() => {
  getListData();
});

//数据源
const searchForm = ref({
  id:0,
  name: "",
  date:'',
  page: 1,
  page_size: 10,
});

const tableData = ref([]);
const total = ref(0);
const loading = ref(false)
/**
 * 获取角色列表
 */
const getListData = async () => {
  loading.value = true

  await getRoleList(searchForm.value)
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
 * 分配权限
 */
const distributePermissionVisible = ref(false)
const selectRoleId = ref('')
const handleEdit = row => {
  selectRoleId.value = row.id
  distributePermissionVisible.value = true
}

const searchEvent = () => {
  searchForm.value.page = 1;
  getListData();
};
const onDownTemplate = () => {
  ElMessage.error("演示模式")
}

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

  .pagination {
    margin-top: 20px;
    display: flex;
    justify-content: end;
  }

}
</style>
