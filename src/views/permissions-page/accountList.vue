<template>
    <div class="home-box">
        <el-form :inline="true" :model="searchForm">
            <el-form-item label="账号">
                <el-input v-model="searchForm.account" placeholder="账号"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="searchEvent" v-auth="'/adminAuth/adminList'">查询
                </el-button>
            </el-form-item>
        </el-form>

        <el-card>
            <el-table :data="tableData" border>
                <el-table-column prop="id" label="ID" width="180"></el-table-column>
                <el-table-column prop="account" label="账号" width="180">
                </el-table-column>
                <el-table-column label="角色" width="100">
                    <template #default="{ row }">
                        <el-tag type="danger" size="mini">{{row.role_name }}</el-tag>
                    </template>
                </el-table-column>
                <el-table-column label="状态" width="100">
                    <template #default="{ row }">
                        <span>{{row.is_lock == '1'?'冻结':'正常' }}</span>
                    </template>
                </el-table-column>
                <el-table-column prop="date" label="操作时间" width="180">
                </el-table-column>
                <el-table-column prop="address" label="操作">
                    <template #default="{ row }">
                        <el-button type="text" size="small" @click="handleEdit(row)" v-auth="'/adminAuth/modifyAdmin'">
                            修改
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
                    :total="total">
            </el-pagination>
        </el-card>

    </div>
</template>
<script>
    export default {
        name: 'admintorList',
    };
</script>
<script setup>

    import {ref, onMounted} from 'vue'
    import {getAdmintorList} from '@/api/api'
    import {useStore} from 'vuex'
    import {useRouter} from 'vue-router'


    onMounted(() => {
        getListData()
    })

    //数据源
    const searchForm = ref({
        account: '',
        page: 1,
        page_size: 10,

    })

    const tableData = ref([])
    const total = ref(0)


    const handleSizeChange = (val) => {
        searchForm.value.page_size = val;
        getListData();
    }
    const handleCurrentChange = (val) => {
        searchForm.value.page = val;
        getListData();
    }

    const searchEvent = () => {
        searchForm.value.page = 1
        getListData();

    }

    const handleEdit = (row) => {
        console.log(row)

    }
    /**
     * 获取账号列表
     */
    const getListData = () => {
        //本地数据
        console.log("----模拟获取【账号列表】数据,真实数据需要填写constant.js里的接口域名------")
        const accountList = import.meta.glob('@/api/accountList.json', {eager: true})
        let list = accountList['/src/api/accountList.json'].default
        tableData.value = list.data
        total.value = Number(list.page_info.total_items);
        //真实接口
        // getAdmintorList(searchForm.value)
        //   .then(data => {
        //     tableData.value = data.bizobj
        //     total.value = Number(data.page_info.total_items);
        //
        //   })
        //   .catch(err => {
        //   })
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
            text-align: end;
        }
    }

</style>
