<template>
  <div class="c">
    <main class="container">
      <section class="slide sticky" id="slide1">
        <h1>鼠标滑轮向下滚动</h1>
      </section>
      <section class="slide sticky" id="slide2">
        <h1>鼠标滑轮向下（上）滚动</h1>
      </section>
      <section class="slide sticky" id="slide3">
        <h1>鼠标滑轮向下（上）滚动</h1>
      </section>
      <section class="slide sticky" id="slide4">
        <h1>End</h1>
      </section>
    </main>

  </div>

</template>

<script>
export default {
  name: "slidePic"
}
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Lora:400,400i,700");

.c {
  margin: 0;
  padding: 0;
}

.container {
  height: 80vh;
  font-family: Lora, serif;
  overflow-x: hidden;
}

.slide {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  letter-spacing: 0.2em;
  color: white;
  background-size: cover;
  background-position: center;

  h1 {
    font-size: 250%;
    text-shadow: 0 2px 2px black;
  }
}

#slide1 {
  background-image: url("https://i.loli.net/2019/11/23/cnKl1Ykd5rZCVwm.jpg");
}

#slide2 {
  background-image: url("https://i.loli.net/2019/10/18/uXF1Kx7lzELB6wf.jpg");
}

#slide3 {
  background-image: url("https://i.loli.net/2019/11/16/FLnzi5Kq4tkRZSm.jpg");
}

#slide4 {
  background-image: url("https://i.loli.net/2019/10/18/buDT4YS6zUMfHst.jpg");
}

</style>