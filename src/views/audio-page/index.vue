<template>
  <div class="container">
    <canvas class="cvs"
            id="myCanvas"></canvas>
    <audio
        class="audio"
        src="../src/assets/demo.wav"
        controls
        @play="onPlay"
        id="myAudio">
    </audio>


  </div>
</template>

<script setup>
import {onMounted, onUnmounted, ref, watch} from "vue";
import {useRoute} from "vue-router";

const route = useRoute()

onMounted(() => {
  initCanvas()
  draw();
})

/**
 * 监听路由变化
 */
watch(
    route,
    (to, from) => {
      const { fullPath, meta, name, params, path, query } = to
      if(path=='/audio/view' ){
        location.reload();

      }
    }
)
onUnmounted(() => {
  console.log("onUnmounted")

});

const isInit = ref(false)
const dataArray = ref(null)
let analyser = null


// 当音频播放
const onPlay = () => {
  if (isInit.value) {
    return;
  }

  let audioEle = document.getElementById("myAudio");
  //初始化
  let audCtx = new AudioContext(); //创建音频上下文
  analyser = audCtx.createAnalyser();
  let source = audCtx.createMediaElementSource(audioEle); //创建音频源节点
  analyser.fftSize = 512; //一个无符号长整形 (unsigned long) 的值，代表了快速傅里叶变换(分析器)的窗口大小
  //创建数组，用于接受节点分析器分析的数据
  dataArray.value = new Uint8Array(analyser.frequencyBinCount); //这里并不是声明一个普通数组，而是需要声明一个无符号的八位整数，刚好是一个字节。并且数组长度需要刚好等于频谱图横坐标长度
  source.connect(analyser);
  analyser.connect(audCtx.destination);
  isInit.value = true;
}

//把分析器分析的数据不断绘制到canvas
const draw = () => {
  let cvs = document.getElementById("myCanvas");
   if(!cvs){
     return;
   }
  let ctx = cvs.getContext("2d");
  requestAnimationFrame(draw);
  //清空画布
  const {width, height} = cvs;
  ctx.clearRect(0, 0, width, height);
  //判断分析器是否初始化
  if (!isInit.value) {
    return;
  }
  //分析器节点分析出数据到数组中
  analyser.getByteFrequencyData(dataArray.value); //让分析器节点分析当前音频源数据，把分析结果添加到数组
  const len = dataArray.value.length / 2.5;
  const barWidth = width / len;

  //创建矩形渐变
  let grd=ctx.createLinearGradient(0, 0, width, 0);
  grd.addColorStop(0.1,'red');
  grd.addColorStop(0.2,'orange');
  grd.addColorStop(0.4,'yellow');
  grd.addColorStop(0.5,'green');
  grd.addColorStop(0.6,'cyan');
  grd.addColorStop(0.7,'blue');
  grd.addColorStop(0.8,'purple');


  ctx.fillStyle = grd;
  // 柱状频谱图
  for (let i = 0; i < len; i++) {
    const data = dataArray.value[i]; //<256
    const barHeight = (data / 255) * height;
    const y = height - barHeight;
    ctx.fillRect(i*4, y, barWidth , barHeight);

  }


}


const initCanvas = () => {
  let canvas = document.getElementById("myCanvas");
  let ctx = canvas.getContext("2d");
  ctx.fillRect(10, 10, 280, 100);
}


</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;

  .cvs {
    width: 600px;
    height: 200px
  }

  .audio {
    margin-top: 10px;
  }
}
</style>