<template>
  <div class="c">
    <ul class="menu-hover-fill">
      <li><a href="#" data-text="home">home</a></li>
      <li><a href="#" data-text="archives">archives</a></li>
      <li><a href="#" data-text="tags">tags</a></li>
      <li><a href="#" data-text="categories">categories</a></li>
      <li><a href="#" data-text="about">about</a></li>
    </ul>

  </div>

</template>

<script>
export default {
  name: "hoverSlideMenu"
}
</script>

<style lang="scss" scoped>

.c {
  --grey-color: #7f8c8d;
  --primary-color: hsl(196, 78%, 61%);
  --secondary-color: hsl(217, 15%, 83%);
  --success-color: hsl(165, 58%, 55%);
  --info-color: hsl(214, 79%, 65%);
  --warning-color: hsl(43, 100%, 66%);
  --danger-color: hsl(354, 81%, 63%);
  --primary-color-darker: hsl(196, 68%, 54%);
  --secondary-color-darker: hsl(215, 13%, 70%);
  --success-color-darker: hsl(165, 55%, 48%);
  --info-color-darker: hsl(214, 68%, 58%);
  --warning-color-darker: hsl(39, 97%, 62%);
  --danger-color-darker: hsl(354, 67%, 56%);
  --primary-color-lighter: hsl(196, 78%, 81%);
  --secondary-color-lighter: hsl(214, 16%, 92%);
  --success-color-lighter: hsl(165, 58%, 75%);
  --info-color-lighter: hsl(214, 79%, 85%);
  --warning-color-lighter: hsl(43, 100%, 86%);
  --danger-color-lighter: hsl(354, 81%, 83%);
  --secondary-color-darkest: hsl(215, 11%, 30%);
  --secondary-color-lightest: hsl(220, 1%, 98%);
  --grey-color: #7f8c8d;
  display: flex;
  min-height: 100vh;
  background: black;
  position: fixed;
  z-index: 0;
  width: 100%;
  padding-top: 100px;
  padding-left: 300px;
}

ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
}

a {
  text-decoration: none;
  height: 100px;
}

$menu-link-active-colors: var(--primary-color), var(--info-color),
var(--success-color), var(--warning-color), var(--danger-color);

.menu-hover-fill {
  font-size: 1.5rem;
  text-transform: uppercase;
  line-height: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;

li {
  position: relative;
  margin-top: 20px;

&::before {
   position: absolute;
   content: "";
   top: 0;
   left: -1rem;
   width: 0.25rem;
   height: 100%;
   background: var(--menu-link-active-color);
   transition: 0.6s;
 }

a {
  --menu-link-color:  var(--grey-color);
  position: relative;
  background: linear-gradient(var(--menu-link-active-color) 0 100%) left / 0
  no-repeat;
  color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  transition: background-size 0.45s 0.04s;

&::before {
   position: absolute;
   content: attr(data-text);
   z-index: -1;
   color: var(--grey-color);
 }
}

@for $i from 1 through length($menu-link-active-colors) {
&:nth-child(#{$i}) {
  --menu-link-active-color: #{nth($menu-link-active-colors, $i)};
}
}

&:hover {
&::before {
   left: calc(100% + 1rem);
 }

a {
  background-size: 100%;
}
}
}
}


</style>