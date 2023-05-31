<template>
  <div class="">
    <p>后台管理系统通用架构，开箱即用！</p>
    <p style="margin-top: 10px">项目技术栈：Vue3 + JavaScript + Vite4 + Element-plus2.3.5</p>
    <p style="margin-top: 10px">项目主要技术方案：</p>
    <p>1、接口模块封装方案</p>
    <p>2、请求动作封装方案</p>
    <p>3、token 处理方案</p>
    <p>4、动态路由表处理方案</p>
    <p>5、动态菜单项处理方案</p>
    <p>6、动态面包屑处理方案</p>
    <p>7、历史打开页面TagsView 处理方案</p>
    <p>8、RBAC 的权限分控体系</p>
    <p>9、页面权限处理方案</p>
    <p>10、功能权限处理方案</p>
    <p>11、辅助库选择标准</p>
    <p>12、富文本编辑器处理方案</p>
    <p style="color: red">最新内容持续更新中...</p>
    <p style="margin-top: 10px;">博客主页：前端小三爷_</p>
    <a href="https://juejin.cn/user/1310273591836957" target="_blank">链接：https://juejin.cn/user/1310273591836957</a>
    <p>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。</p>



  </div>
</template>

<script setup>
  import { getPermission } from '@/api/api'
  import {ref, onMounted} from 'vue'


  onMounted(() => {
    // getPermissionList()

  })

  const getPermissionList = () => {
    getPermission({})
      .then(data => {


      })
      .catch(err => {
      })
  }


</script>

<style lang="scss" scoped>
p{
  font-size: 16px;
  line-height: 30px;
  font-family: PingFangSC-Regular, PingFang SC;
  font-weight: 400;
  color: #333333;
}
a{
  text-decoration: underline;
  font-size: 16px;
  line-height: 30px;
  font-family: PingFangSC-Regular, PingFang SC;
  font-weight: 400;
  color: blue;

}
</style>
