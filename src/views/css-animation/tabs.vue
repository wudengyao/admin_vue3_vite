<template>
  <div class="c">
    <div class="tabs">
      <ul class="tabs__links">
        <li>
          <button class="tabs__link">
            <span class="tabs__link__text" data-text="Tab 1">Tab 1</span>
          </button>
        </li>
        <li>
          <button class="tabs__link">
            <span class="tabs__link__text" data-text="Tab 2">Tab 2</span>
          </button>
        </li>
        <li>
          <button class="tabs__link">
            <span class="tabs__link__text" data-text="Tab 3">Tab 3</span>
          </button>
        </li>
        <li>
          <button class="tabs__link">
            <span class="tabs__link__text" data-text="Tab 4">Tab 4</span>
          </button>
        </li>
      </ul>
      <ul class="tabs__contents">
        <li>
          <div class="tabs__content">
           tab1的内容
          </div>
        </li>
        <li>
          <div class="tabs__content">
            tab2的内容
          </div>
        </li>
        <li>
          <div class="tabs__content">
            tab3的内容
          </div>
        </li>
        <li>
          <div class="tabs__content">
            tab4的内容
          </div>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: "tabs"
}
</script>
<script setup>
import {ref, onMounted} from 'vue'


onMounted(() => {
  let tabLinks = document.querySelectorAll(".tabs__link");
  let tabContents = document.querySelectorAll(".tabs__content");
  tabLinks[0].classList.add("active");
  tabContents[0].classList.add("active");
  tabLinks.forEach((tabLink, i) => {
    tabLink.addEventListener("click", () => {
      tabLinks.forEach(tabLink => tabLink.classList.remove("active"));
      tabContents.forEach(tabContent => tabContent.classList.remove("active"));
      tabLink.classList.add("active");
      tabContents[i].classList.add("active");
    });
  });
})

</script>

<style lang="scss" scoped>
// gradient: https://webgradients.com
@import url("https://fonts.googleapis.com/css?family=Lato:400,300");

@mixin sp-layout {
  @media screen and (max-width: 750px) {
    @content;
  }
}

.c {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #1A1E23;
}

.tabs {
  --tab-links-height: 80px;
  --tab-links-bg: linear-gradient(135deg, #e5eaf1 0%, #b9c5d8 100%);
  --tab-links-overlay: linear-gradient(
          135deg,
          #2cd8d5 0%,
          #6b8dd6 48%,
          #8e37d7 100%
  );
  --tab-link-bg: linear-gradient(
          90deg,
          transparent 70%,
          rgba(255, 255, 255, 0.2) 100%
  );
  width: 100%;
  max-width: 600px;
  min-width: 300px;
  font-family: Lato, sans-serif;

  .tabs__links {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: var(--tab-links-height);
    background: var(--tab-links-bg);
    list-style-type: none;

    @include sp-layout {
      height: calc(var(--tab-links-height) / 2);
    }

    li {
      flex: 1;

      .tabs__link {
        all: unset;
        position: relative;
        height: var(--tab-links-height);
        width: 100%;
        background: var(--tab-link-bg);
        cursor: pointer;
        overflow: hidden;
        transition: 0.3s;

        @include sp-layout {
          height: calc(var(--tab-links-height) / 2);
          font-size: 12px;
        }

        &::before {
          position: absolute;
          content: "";
          top: 0;
          left: 0;
          z-index: 2;
          width: 100%;
          height: 100%;
          background: var(--tab-links-overlay);
          transform: scaleY(0);
          transform-origin: top;
          transition: 0.3s ease-in-out;
        }

        .tabs__link__text {
          position: relative;
          z-index: 2;
          display: flex;
          justify-content: center;
          align-items: center;
          opacity: 0.6;
          transition: 0.5s;

          // big-text
          &::before {
            position: absolute;
            content: attr(data-text);
            top: 160%;
            z-index: -1;
            font-size: 40px;
            font-weight: 600;
            color: white;
            opacity: 0.1;
            transition: 1.2s ease-out;

            @include sp-layout {
              display: none;
            }
          }
        }

        &:hover {
          &::before {
            transform: scaleY(1);
          }

          .tabs__link__text {
            color: white;
            opacity: 1;

            &::before {
              transform: translateY(-300%);
            }
          }
        }

        &.active {
          transform: scaleY(1.4);
          background: white;

          &::before {
            transform: scaleY(0.05);
          }

          .tabs__link__text {
            transform: scaleY(0.714);
          }
        }

        &.active .tabs__link__text,
        &.active:hover .tabs__link__text {
          background: var(--tab-links-overlay);
          background-clip: text;
          -webkit-background-clip:text;
          color: transparent;
          opacity: 1;
        }
      }
    }
  }

  .tabs__contents {
    position: relative;
    margin-top: 0;
    padding: 40px 60px;
    background: white;
    list-style-type: none;
    transition: 1s;

    // bottom-line
    &::after {
      position: absolute;
      content: "";
      left: 0;
      bottom: 0;
      width: 100%;
      height: 5px;
      background: var(--tab-links-overlay);
    }

    .tabs__content {
      display: none;
      min-height: 200px;
      font-weight: 300;
      line-height: 1.8;
      opacity: 0;
      transform: translateY(30%);
      animation: fadeIn 0.6s forwards;

      &.active {
        display: block;
      }
    }
  }
}

@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


</style>