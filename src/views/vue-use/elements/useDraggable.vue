<template>
 <div style="position: relative">
   <div ref="el" :style="style" style="position: fixed;background: #304156;height: 100px;width: 100px;color: white">
     Drag me! I am at {{x}}, {{y}}
   </div>
 </div>
</template>

<script>
export default {
  name: "useDraggable"
}
</script>
<script setup>
import { ref } from 'vue'
import { useDraggable } from '@vueuse/core'
const el = ref(null)
const { x, y, style } = useDraggable (el, {
  initialValue: { x: 500, y: 200 },
})
</script>

<style scoped>

</style>