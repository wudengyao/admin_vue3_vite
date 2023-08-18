<template>
  <div>
    <div style="position: fixed;top: 200px;z-index: 9999;color: white;left: 300px">
      <div>请上下滚动鼠标</div>
      <div>是否开始加载下一屏的数据：<span style="color:red;">{{ targetIsVisible ? '是' : '否' }}</span></div>
    </div>
    <!--   模拟 第一屏-->
    <div style="background: #304156;height: 100vh"></div>
    <!--   模拟 第二屏-->
    <div ref="target" style="background: #001528;height: 100vh"></div>

  </div>
</template>

<script>
export default {
  name: "useIntersectionObserver"
}
</script>
<script setup>
import {ref} from 'vue'
import {useIntersectionObserver} from '@vueuse/core'

// target表示组件的最外层div元素
const target = ref(null)
const targetIsVisible = ref(false)
// 监听组件是否进入可视区
const {stop} = useIntersectionObserver(target, ([{isIntersecting}], observerElement) => {
      // 如果target对应的DOM进入可视区，那么该回调函数就触发
      if (isIntersecting) {
        // 被监听的DOM进入了可视区:此时调用接口获取数据；停止继续监听
        stop()
        targetIsVisible.value = isIntersecting
        console.log("useElementVisibility==", targetIsVisible.value)
        //这里可以进性网络请求
      }


    },
)


</script>

<style scoped>

</style>