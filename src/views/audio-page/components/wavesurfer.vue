<template>
  <div>
    <div ref="waveformRef"></div>
    <div ref="waveTimelineRef"></div>
    <el-button type="primary" @click="wavesurfer.skip(-1)">后退</el-button>
    <el-button type="primary" @click="wavesurfer.playPause()">
      <i class="el-icon-video-play" />
      播放 / 暂停
    </el-button> <el-button type="primary" @click="wavesurfer.skip(1)">前进</el-button>
    <el-button type="primary" @click="rebroadcast">重播</el-button>
    <el-button type="primary" @click="handleStop">停止</el-button>
  </div>
</template>

<script>
import WaveSurfer from 'wavesurfer.js'
import Timeline from 'wavesurfer.js/dist/plugin/wavesurfer.timeline'

export default {
  props: {
    voiceSrc:{
      type: String,
      default: ''
    }
  },
  data() {
    return { wavesurfer: null }
  },
  mounted() {
    this.init()
  },
  beforeDestroy() {
    this.wavesurfer && this.wavesurfer.destroy()
    this.wavesurfer = null
  },
  methods: {
    init() {
      const container = this.$refs.waveformRef
      container.addEventListener('click', () => {
        console.log('点击容器')
      })
      this.wavesurfer = WaveSurfer.create({
        container, // 容器，唯一一个必须参数
        cursorColor: '#304156', // 音频光标颜色
        waveColor: '#ddd', // 波形颜色
        progressColor: '#304156', // 已完成播放的波形颜色 当progressColor和waveColor相同时，完全不渲染进度波
        backend: 'MediaElement',
        autoCenter: false,
        plugins: [
            Timeline.create({ container: this.$refs.waveTimelineRef })
        ]
      })

      this.wavesurfer.load(this.voiceSrc) // 加载音频url



    },



    // 重放
    rebroadcast() {
      this.wavesurfer.play(0)
    },
    // 停止
    handleStop() {
      this.wavesurfer.stop()
    },

  }
}
</script>