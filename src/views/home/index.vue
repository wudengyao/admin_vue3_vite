<template>
  <el-row :gutter="20" class="fdr">
    <el-col :span="6">
      <el-timeline>
        <el-timeline-item center placement="top">
          <el-card class="c4">
            <h3>一个极简的后台基础模板，企业级！开箱即用！</h3>
            <div style="margin-top: 10px">项目技术栈：Vue3 + JavaScript + Vite4 + Element-plus2.3.5</div>
          </el-card>
        </el-timeline-item>
        <el-timeline-item placement="top">
          <el-card class="c4">
            <h3>项目主要技术方案：</h3>
            <div v-for="item in list">
              <div style="padding: 8px 0">{{ item }}</div>
            </div>
          </el-card>
        </el-timeline-item>

        <el-timeline-item center placement="top">
          <el-link style="font-size: 20px" type="danger" href="https://juejin.cn/user/1310273591836957" target="_blank">
            博客主页：前端小三爷_
          </el-link>
        </el-timeline-item>

      </el-timeline>
    </el-col>
    <el-col :span="18">
      <el-container class="fdc">
        <el-row :gutter="20" class="fdr">
          <el-col :span="8">
            <el-card shadow="hover" class="box-card c1">
              <template #header>
                <h3 class="t1">Vue</h3>
              </template>
              <el-progress type="dashboard" :percentage="51.6" status="success">
                <template #default="{ percentage }">
                  <span class="percentage-value t1">{{ percentage }}%</span>
                </template>
              </el-progress>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover" class="box-card c2">
              <template #header>
                <h3 class="t2">JavaScript</h3>
              </template>
              <el-progress type="dashboard" :percentage="40.7">
                <template #default="{ percentage }">
                  <span class="percentage-value t2">{{ percentage }}%</span>
                </template>
              </el-progress>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover" class="box-card c3">
              <template #header>
                <h3 class="t3">HTML+CSS</h3>
              </template>
              <el-progress type="dashboard" :percentage="7.7" status="warning">
                <template #default="{ percentage }">
                  <span class="percentage-value t3">{{ percentage }}%</span>
                </template>
              </el-progress>
            </el-card>
          </el-col>
        </el-row>

       <!--图表-->
        <div style="display: flex;flex: 1;width: 100%">
          <div id="main"></div>

        </div>

      </el-container>

    </el-col>


  </el-row>

</template>

<script setup>
import {getPermission} from '@/api/api'
import {ref, onMounted, computed ,watch} from 'vue'
import * as echarts from 'echarts';
import {useStore} from 'vuex'
const store = useStore()

// const sidebarOpened = computed(() =>
//     store.getters.sidebarOpened ? 'hamburger-opened' : 'hamburger-closed'
// )
//
// watch(sidebarOpened, val => {
//  console.log("sidebarOpened = ",sidebarOpened.value)
//
// })


const list = ref([
  '1、接口模块封装方案',
  '2、请求动作封装方案',
  '3、token 处理方案',
  '4、动态路由表处理方案',
  '5、动态菜单项处理方案',
  '6、动态面包屑处理方案',
  '7、历史打开页面TagsView 处理方案',
  '8、RBAC 的权限分控体系',
  '9、页面权限处理方案',
  '10、功能权限处理方案',
  '11、辅助库选择标准',
  '12、富文本编辑器处理方案',
  '13、keepAlive页面缓存处理方案'

])

onMounted(() => {
  initChart()

});

const initChart = () => {
  let chartDom = document.getElementById('main');
  let myChart = echarts.init(chartDom);
  let option;
  option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        crossStyle: {
          color: '#999'
        }
      }
    },
    toolbox: {
      feature: {
        magicType: { show: true, type: ['line', 'bar'] },
        restore: { show: true },
        saveAsImage: { show: true }
      }
    },
    legend: {
      data: ['Evaporation', 'Precipitation', 'Temperature']
    },
    xAxis: [
      {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        axisPointer: {
          type: 'shadow'
        }
      }
    ],
    yAxis: [
      {
        type: 'value',
        name: 'Precipitation',
        min: 0,
        max: 250,
        interval: 50,
        axisLabel: {
          formatter: '{value} ml'
        }
      },
      {
        type: 'value',
        name: 'Temperature',
        min: 0,
        max: 25,
        interval: 5,
        axisLabel: {
          formatter: '{value} °C'
        }
      }
    ],
    series: [
      {
        name: 'Evaporation',
        type: 'bar',
        tooltip: {
          valueFormatter: function (value) {
            return value + ' ml';
          }
        },
        data: [
          2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
        ]
      },
      {
        name: 'Precipitation',
        type: 'bar',
        tooltip: {
          valueFormatter: function (value) {
            return value + ' ml';
          }
        },
        data: [
          2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
        ]
      },
      {
        name: 'Temperature',
        type: 'line',
        yAxisIndex: 1,
        tooltip: {
          valueFormatter: function (value) {
            return value + ' °C';
          }
        },
        data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
      }
    ]
  };
  option && myChart.setOption(option);

}

</script>

<style lang="scss" scoped>
@import '@/styles/mixin.scss';
@import '@/styles/variables.module.scss';

$success: #67c23a;
$warning: #e6a23c;
$danger: #f56c6c;
$primary: #409eff;

p {
  font-size: 16px;
  line-height: 30px;
  font-family: PingFangSC-Regular, PingFang SC;
  font-weight: 400;
  color: #333333;
}


.box-card {
  margin-bottom: 13px;
  height: 10rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;


}

.c1 {
  -webkit-box-shadow: 3px 3px 10px $success;
  box-shadow: 3px 3px 10px $success;
}

.c2 {
  -webkit-box-shadow: 3px 3px 10px;
  box-shadow: 3px 3px 10px $primary;
}

.c3 {
  -webkit-box-shadow: 3px 3px 10px $warning;
  box-shadow: 3px 3px 10px $warning;
}

.c4 {
  -webkit-box-shadow: 3px 3px 10px #909399;
  box-shadow: 3px 3px 10px #909399;
}

.c5 {
  -webkit-box-shadow: 3px 3px 10px $danger;
  box-shadow: 3px 3px 10px $danger;
}

.fdr {
  display: flex;
  flex-direction: row;
}

.fdc {
  display: flex;
  flex-direction: column;
}

.t1 {
  color: $success;
  width: 1rem;
}

.t2 {
  color: $primary;
  width: 1rem;


}

.t3 {
  color: $warning;
  width: 1rem;


}


#main {
  min-height: 40rem;
  width: 100%;

}

</style>
