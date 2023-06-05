<template>
  <div class="home-box">
    <el-form :inline="true" :model="searchForm">
      <el-form-item label="角色名称">
        <el-input v-model="searchForm.name" placeholder="角色名称"></el-input>
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
    <el-card>
      <el-table :data="tableData"
                v-loading="loading"
                element-loading-text="加载中..."
                border>
        <el-table-column prop="id" label="角色ID" width="180">
        </el-table-column>
        <el-table-column prop="name" label="角色名称" width="180">
        </el-table-column>
        <el-table-column prop="operator" label="操作信息"></el-table-column>
        <el-table-column prop="address" label="操作">
          <template #default="{ row }">
            <el-button
              type="text"
              size="small"
              @click="handleEdit(row, 'see')"
              v-auth="'/adminAuth/lookRole'"
              >查看
            </el-button>
            <el-button
              type="text"
              size="small"
              @click="handleEdit(row)"
              v-auth="'/adminAuth/saveRole'"
              >修改
            </el-button>
            <el-button
              style="color: #e98f8c"
              type="text"
              size="small"
              @click="handleDel(row)"
              v-auth="'/adminAuth/delRole'"
              >刪除
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
  </div>
</template>
<script>
export default {
  name: "getRoleList",
};
</script>
<script setup>
import { ref, onMounted } from "vue";
import { getRoleList } from "@/api/api";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

onMounted(() => {
  getListData();
});

//数据源
const searchForm = ref({
  name: "",
  page: 1,
  page_size: 10,
});

const tableData = ref([]);
const total = ref(0);
const loading = ref(false)

const handleSizeChange = (val) => {
  searchForm.value.page_size = val;
  getListData();
};
const handleCurrentChange = (val) => {
  searchForm.value.page = val;
  getListData();
};

const searchEvent = () => {
  searchForm.value.page = 1;
  getListData();
};

const handleEdit = (row) => {
  console.log(row);
};

const handleDel = (row) => {
  console.log(row);
};

/**
 * 获取角色列表
 */
const getListData = () => {
  loading.value = true
  getRoleList(searchForm.value)
    .then(data => {
      tableData.value = data.bizobj
      total.value = Number(data.page_info.total_items);
      loading.value = false

    })
    .catch(err => {
      loading.value = false

    })
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

  .pagination {
    margin-top: 20px;
    text-align: end;
  }
}
</style>
