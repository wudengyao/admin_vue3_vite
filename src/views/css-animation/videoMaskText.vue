<template>
<div class="c">
  <video autoplay muted loop preload poster="https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/oceanshot.jpg">
    <source src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/ocean-small.webm" />
    <source src="http://thenewcode.com/assets/videos/ocean-small.mp4" />
  </video>
  <h1>ocean</h1>
</div>
</template>

<script>
export default {
  name: "VideMaskText"
}
</script>

<style lang="scss" scoped>
@font-face {
  font-family: Biko;
  src: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/biko-black.woff");
}

.c {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

video,
h1 {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  margin: 0;
}

video {
  object-fit: cover;
}

h1 {
  font-size: 20vw;
  font-family: Biko, sans-serif;
  font-weight: 700;
  line-height: 100vh;
  text-transform: uppercase;
  text-align: center;
  background: white;
  mix-blend-mode: screen;
}

</style>