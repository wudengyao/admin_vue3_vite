<template>
<div class="c">
  <button class="btn btn-primary btn-ghost btn-shine">
    hover me
  </button>
</div>
</template>

<script>
export default {
  name: "hoverShiningBtn"
}
</script>

<style lang="scss" scoped>
@import url(https://fonts.googleapis.com/css?family=Lato);

.c {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  background: #1A1E23;
}

.btn {
  --hue: 190;
  position: relative;
  padding: 1rem 3rem;
  font-size: 1rem;
  line-height: 1.5;
  color: white;
  text-decoration: none;
  text-transform: uppercase;
  background-color: hsl(var(--hue), 100%, 41%);
  border: 1px solid hsl(var(--hue), 100%, 41%);
  outline: transparent;
  overflow: hidden;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
  transition: 0.25s;

&:hover {
   background: hsl(var(--hue), 100%, 31%);
 }

&-primary {
   --hue: 187;
 }

&-ghost {
   color: hsl(var(--hue), 100%, 41%);
   background-color: transparent;
   border-color: hsl(var(--hue), 100%, 41%);

&:hover {
   color: white;
 }
}

&-shine {
   color: white;

&::before {
   position: absolute;
   content: "";
   top: 0;
   left: 0;
   width: 100%;
   height: 100%;
   background: linear-gradient(
       120deg,
       transparent,
       hsla(var(--hue), 100%, 41%, 0.5),
       transparent
   );
   transform: translateX(-100%);
   transition: 0.6s;
 }

&:hover {
   background: transparent;
   box-shadow: 0 0 20px 10px hsla(var(--hue), 100%, 41%, 0.5);
 }

&:hover::before {
   transform: translateX(100%);
 }
}
}

</style>