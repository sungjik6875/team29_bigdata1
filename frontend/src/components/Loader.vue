<template>
  <div class="loader-div">
    <div ref="loader" class="loader">
      <span class="square square1"></span>
      <span class="square square2"></span>
      <span class="square square3"></span>
    </div>
  </div>
</template>

<script>
export default {

}
</script>


<style scoped lang="scss">
.loader-div {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
}

.loader {
  position: fixed;
  display: flex;
  justify-content: center;
  top: 50vh;
  margin: 0 auto;
  width: 100%;
}

.square {
  margin: 0 1vw;
  background-color: #3F51B5;
  width: 75px;
  height: 75px;
  animation-name: loader;
  animation-duration: 1.5s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-fill-mode: backwards;
}

.square2 {
  animation-delay: 0.5s;
}
.square3 {
  animation-delay: 1s;
}

@keyframes loader {
  0% {
    transform: scale(0, 0);
    opacity:0.8;
  }
  100% {
    transform: scale(1, 1);
    opacity:0;
  }
}
</style>