<template>
<div class="c">
  <ul>
    <li><a href="#">home</a></li>
    <li><a href="#">product</a></li>
    <li><a href="#">order</a></li>
    <li><a href="#">categories</a></li>
    <li><a href="#">about</a></li>
  </ul>
</div>
</template>

<script>
export default {
  name: "hoverFillText"
}
</script>

<style lang="scss" scoped>
// https://picular.co/bluemoon

@import url("https://fonts.googleapis.com/css?family=Raleway:400,400i,700");

.c {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: #1A1E23;
}

ul {
  display: flex;
  flex-direction: column;
  align-items: start;
  list-style-type: none;

  li {
    padding: 6px 0;

    a {
      --fill-color: #198CE6;
      position: relative;
      display: block;
      padding: 4px 0;
      font: 700 3rem Raleway, sans-serif;
      text-decoration: none;
      text-transform: uppercase;
      -webkit-text-stroke: 2px var(--fill-color);
      background: linear-gradient(var(--fill-color) 0 100%) left / 0 no-repeat;
      color: transparent;
      background-clip: text;
      -webkit-background-clip:text;
      transition: 0.5s linear;

      &:hover {
        background-size: 100%;
      }
    }
  }
}
</style>