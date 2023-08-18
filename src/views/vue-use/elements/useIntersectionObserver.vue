<template>
  <div>
    <div style="position: fixed;top: 200px;z-index: 9999;color: white;left: 300px">
      <div>请上下滚动鼠标</div>
      <div>是否开始加载下一屏的数据：<span style="color:red;">{{targetIsVisible?'是':'否'}}</span></div>
    </div>
    <div style="background: #304156;height: 100vh"></div>
    <div ref="target" style="background: #001528;height: 100vh"></div>

<!--    <h1 ref="target">Hello world</h1>-->
  </div>
</template>

<script>
export default {
  name: "useIntersectionObserver"
}
</script>
<script setup>
import { ref } from 'vue'
import { useIntersectionObserver  } from '@vueuse/core'



const target = ref(null)
const targetIsVisible = ref(false)

const { stop } = useIntersectionObserver(
    target,
    ([{ isIntersecting }], observerElement) => {
      targetIsVisible.value = isIntersecting
      console.log("useElementVisibility==",targetIsVisible.value)

    },
)


</script>

<style scoped>

</style>