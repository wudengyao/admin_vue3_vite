<template>
  <div class="c">
    <div class="clock-loader"></div>

  </div>
</template>

<script>
export default {
  name: "clock"
}
</script>

<style lang="scss" scoped>
.c {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 85vh;
  margin: 0;
  background: black;
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
}

.clock-loader {
  --clock-color: var(--primary-color);
  --clock-width: 4rem;
  --clock-radius: calc(var(--clock-width) / 2);
  --clock-minute-length: calc(var(--clock-width) * 0.4);
  --clock-hour-length: calc(var(--clock-width) * 0.2);
  --clock-thickness: 0.2rem;

  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: var(--clock-width);
  height: var(--clock-width);
  border: 3px solid var(--clock-color);
  border-radius: 50%;

  &::before,
  &::after {
    position: absolute;
    content: "";
    top: calc(var(--clock-radius) * 0.25);
    width: var(--clock-thickness);
    background: var(--clock-color);
    border-radius: 10px;
    transform-origin: center calc(100% - calc(var(--clock-thickness) / 2));
    animation: spin infinite linear;
  }

  &::before {
    height: var(--clock-minute-length);
    animation-duration: 2s;
  }

  &::after {
    top: calc(var(--clock-radius) * 0.25 + var(--clock-hour-length));
    height: var(--clock-hour-length);
    animation-duration: 15s;
  }
}

@keyframes spin {
  to {
    transform: rotate(1turn);
  }
}

</style>