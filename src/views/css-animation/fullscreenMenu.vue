<template>
<div class="c">
  <h1>点击左上角的菜单按钮看看效果吧</h1>
  <input type="checkbox" id="burger-toggle">
  <label for="burger-toggle" class="burger-menu">
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
  </label>

  <div class="menu">
    <div class="menu-inner">
      <ul class="menu-nav">
        <li class="menu-nav-item"><a class="menu-nav-link" href="#"><span>
            <div>主页</div>
          </span></a></li>
        <li class="menu-nav-item"><a class="menu-nav-link" href="#"><span>
            <div>关于</div>
          </span></a></li>
        <li class="menu-nav-item"><a class="menu-nav-link" href="#"><span>
            <div>产品</div>
          </span></a></li>
        <li class="menu-nav-item"><a class="menu-nav-link" href="#"><span>
            <div>我的</div>
          </span></a></li>
      </ul>
      <div class="gallery">
        <div class="title">
          <p>公司简介</p>
        </div>
        <div class="images">
          <a class="image-link" href="#">
            <div class="image" data-label="星空"><img src="https://i.loli.net/2019/11/23/cnKl1Ykd5rZCVwm.jpg" alt=""></div>
          </a>
          <a class="image-link" href="#">
            <div class="image" data-label="阳光"><img src="https://i.loli.net/2019/11/16/FLnzi5Kq4tkRZSm.jpg" alt=""></div>
          </a>
          <a class="image-link" href="#">
            <div class="image" data-label="极光"><img src="https://i.loli.net/2019/10/18/uXF1Kx7lzELB6wf.jpg" alt=""></div>
          </a>
          <a class="image-link" href="#">
            <div class="image" data-label="天空"><img src="https://i.loli.net/2019/10/18/buDT4YS6zUMfHst.jpg" alt=""></div>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "fullscreenMenu"
}
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Lora:400,400i,700");

@mixin sp-layout {
  @media screen and (max-width: 750px) {
    @content;
  }
}

@mixin pc-layout {
  @media screen and (min-width: 751px) {
    @content;
  }
}

.c {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 85vh;
  margin: 0;
  font-family: Lora, sans-serif;
}

p {
  margin: 0;
}

#burger-toggle {
  position: absolute;
  appearance: none;
  opacity: 0;

  &:checked {
    & ~ .menu {
      opacity: 1;
      visibility: visible;

      .menu-nav-link span div,
      img,
      .title p {
        transform: translateY(0);
        transition: 1.2s 0.1s cubic-bezier(0.35, 0, 0.07, 1);
      }

      .image-link {
        @for $i from 1 through 4 {
          &:nth-child(#{$i}) img {
            transition-delay: 0.1s + 0.08s * $i;
          }
        }
      }
    }

    & ~ .burger-menu {
      .line {
        &::after {
          transform: translateX(0);
        }

        &:nth-child(1) {
          transform: translateY(calc(var(--burger-menu-radius) / 5))
          rotate(45deg);
        }

        &:nth-child(2) {
          transform: scaleX(0);
        }

        &:nth-child(3) {
          transform: translateY(calc(var(--burger-menu-radius) / -5))
          rotate(-45deg);
        }
      }
    }
  }
}

.burger-menu {
  --burger-menu-radius: 4em;

  position: fixed;
  top: 15vh;
  left: 15vw;
  z-index: 100;
  display: block;
  width: var(--burger-menu-radius);
  height: var(--burger-menu-radius);
  outline: none;
  cursor: pointer;

  .line {
    position: absolute;
    left: 25%;
    width: 50%;
    height: 3px;
    background:rgba(43, 61, 79, 0.3);
    border-radius: 10px;
    overflow: hidden;
    transition: 0.5s;

    &:nth-child(1) {
      top: 30%;
    }

    &:nth-child(2) {
      top: 50%;
    }

    &:nth-child(3) {
      top: 70%;
    }

    &::after {
      position: absolute;
      content: "";
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: hsl(195.75deg 67.23% 53.33%);
      transform: translateX(-100%);
      transition: 0.25s;
    }

    @for $i from 2 through 3 {
      &:nth-child(#{$i})::after {
        transition-delay: 0.1s * ($i - 1);
      }
    }
  }

  &:hover {
    .line::after {
      transform: translateX(0);
    }
  }
}

.menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #1a1e23;
  opacity: 0;
  overflow-x: hidden;
  visibility: hidden;
  transition: 0.3s;

  @include sp-layout {
    display: block;
  }

  &-nav {
    display: flex;
    flex-wrap: wrap;
    margin: 0;
    padding: 0;
    text-align: center;
    list-style-type: none;

    @include sp-layout {
      flex-direction: column;
    }

    &-item {
      flex: 1;
    }

    &-link {
      position: relative;
      display: inline-flex;
      font-size: 2rem;
      color: white;
      text-decoration: none;

      span {
        overflow: hidden;

        div {
          transform: translateY(102%);
        }
      }

      &::after {
        position: absolute;
        content: "";
        top: 100%;
        left: 0;
        width: 100%;
        height: 3px;
        background: hsl(195.75deg 67.23% 53.33%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.5s;
      }

      &:hover::after {
        transform: scaleX(1);
        transform-origin: left;
      }
    }
  }

  .gallery {
    margin-top: 60px;
    text-align: center;
  }

  .title {
    font-size: 24px;
    color: white;
    overflow: hidden;

    p {
      font-size: 12px;
      letter-spacing: 2px;
      text-transform: uppercase;
      transform: translateY(102%);
    }
  }

  .images {
    margin-top: 36px;
    display: flex;
    flex-wrap: wrap;

    @include sp-layout {
      justify-content: center;
    }

    .image-link {
      width: 15vw;
      margin: 0 12px;
      overflow: hidden;

      @include sp-layout {
        width: 40vw;
        margin: 0 12px 12px 0;
      }

      .image {
        position: relative;
        transition: 0.6s;

        &::before {
          position: absolute;
          content: attr(data-label);
          top: 0;
          left: 0;
          z-index: 1;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 100%;
          color: white;
          background: rgba(0, 0, 0, 0.6);
          opacity: 0;
          transition: 0.4s;
        }
      }

      &:hover .image {
        transform: scale(1.2);

        &::before {
          opacity: 1;
        }
      }
    }

    img {
      height: 250px;
      transform: translateY(102%);
    }
  }
}

</style>