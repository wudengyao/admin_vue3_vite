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

        <el-table-column prop="buttonList" label="所在页面的按钮权限" min-width="280">
          <template #default="{ row }">
            <el-tag
                class="remark"
                size="small"
                type="danger"
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
/**
 * 权限分级：
 * 1. 一级权限为页面权限
 *  permissionMark 对应 路由名称
 * 2. 二级权限为功能权限
 *  permissionMark 对应 功能权限表
 */
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