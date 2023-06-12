<template>
  <div>
    <el-card>
      <el-table
          :data="allPermission"
          style="width: 100%; margin-bottom: 20px"
          row-key="id"
          border
          default-expand-all
          :tree-props="{ children: 'secondMenuList', hasChildren: 'hasChildren' }">
        <el-table-column
            prop="name"
            label="权限名称"
            width="180">
        </el-table-column>
        <el-table-column
            prop="url"
            label="权限标志"
            width="280">
        </el-table-column>

        <el-table-column
            prop="hidden"
            label="是否显示在菜单列表"
            width="280">
          <template #default="{ row }">
            <el-tag v-if="row.hidden" type="danger">否</el-tag>
            <el-tag v-else  type="success">是</el-tag>
          </template>
        </el-table-column>

        <el-table-column prop="buttonList" label="所在页面的按钮权限" min-width="280">
          <template #default="{ row }">
            <el-tag
                class="remark"
                size="small"
                v-for="(item, index) in row.buttonList"
                :key="index">{{ item.name }}</el-tag>
          </template>
        </el-table-column>

      </el-table>
    </el-card>

  </div>

</template>

<script>
export default {
  name: "permissionList"
}
</script>
<script setup>
import {getPermission} from "@/api/api";
import { ref } from 'vue'

// 所有权限
const allPermission = ref([])
const getPermissionListData = async () => {
  const obj = await getPermission()
  allPermission.value = obj.bizobj
}
getPermissionListData()
</script>
<style lang="scss" scoped>
.remark {
  margin-right: 12px;
}
</style>